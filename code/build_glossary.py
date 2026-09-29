#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_glossary.py — 从源页 HTML 生成「中国历法与古天文学术语对照表（中英双语）」数据集。

输入：源页 HTML（默认取自 ../_source/glossary_zh.html 与 glossary_en.html，
      可用 --src-dir 指定；由 fetch_source.py 抓取）。
输出：../data/ 下 7 个文件（CSV 一律 UTF-8 BOM + CRLF）。

设计纪律（对齐既有 chinese-calendar-dataset 仓）：
  1) 一切断言置于写盘之前；写盘之后只做逐字节回读比对。
  2) 数字全部来自实测（len()），不写死、不照抄文档。
  3) 源页若与上次抓取不同（md5 变），脚本在 manifest 里如实记下，不静默。
  4) 数据件内不放任何网址（含第三方权威库）；外部对标只存「名＋学科」文字，见 README。

用法：
  python code/build_glossary.py --src-dir _source --out data
"""
import argparse
import csv
import hashlib
import io
import json
import os
import re
import sys
from collections import Counter

TAG = re.compile(r"<[^>]+>")

# ── HTML 工具 ────────────────────────────────────────────────────────────────

def detag(s: str) -> str:
    """剥标签 + 解实体 + 归一空白。"""
    s = re.sub(r"<br\s*/?>", " ", s)
    s = TAG.sub("", s)
    for a, b in (("&nbsp;", " "), ("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"),
                 ("&quot;", '"'), ("&#038;", "&"), ("&#8217;", "\u2019"),
                 ("&#8216;", "\u2018"), ("&#8220;", "\u201c"),
                 ("&#8221;", "\u201d"), ("&#8212;", "\u2014"),
                 ("&#8211;", "\u2013"), ("&mdash;", "\u2014"),
                 ("&middot;", "\u00b7")):
        s = s.replace(a, b)
    s = re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), s)
    return re.sub(r"\s+", " ", s).strip()


def split_cells(row_html: str):
    """取一行 <tr> 里的各 <td>/<th> 内部 HTML。"""
    return re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", row_html, re.S)


def strip_strong_span(cell: str):
    """<strong>词</strong><span class="tg">标签</span> → (词, 标签)

    en 页的中文列**不带 <strong>**，只有 `词<span class="tg">标签</span>`；
    故无 <strong> 时须先摘掉 tg span 再剥标签，否则词与标签会黏成一个串。
    """
    m2 = re.search(r'<span class="tg">(.*?)</span>', cell, re.S)
    tag = detag(m2.group(1)) if m2 else ""
    m = re.search(r"<strong>(.*?)</strong>", cell, re.S)
    if m:
        term = detag(m.group(1))
    else:
        term = detag(re.sub(r'<span class="tg">.*?</span>', "", cell, flags=re.S))
    return term, tag


def parse_termonline(cell: str, near_prefix: str):
    """第四列 → (status, term, subject)。status ∈ {exact, near, none}"""
    a = re.search(r"<a\b[^>]*>(.*?)</a>", cell, re.S)
    sp = re.search(r'<span style="display:block[^"]*">(.*?)</span>', cell, re.S)
    subject = detag(sp.group(1)) if sp else ""
    if not a:
        return "none", "", ""
    link = detag(a.group(1))
    if link.startswith(near_prefix):
        return "near", link[len(near_prefix):].strip(), subject
    return "exact", link, subject


# ── 主解析 ───────────────────────────────────────────────────────────────────

def parse_page(html: str, lang: str):
    """返回 dict(classes, groups, appendices, notes, meta)。

    lang='zh'：表列 中文 | English | 释义 | 术语在线
    lang='en'：表列 English | 中文 | Gloss | Termonline
    """
    near_prefix = "近：" if lang == "zh" else "near: "
    out = {"classes": [], "groups": [], "appendices": [], "notes": {}, "meta": {}}

    # 页首纯文本「修订时间：YYYY年M月D日」（站点惯例）
    m = re.search(r"修订时间[：:]\s*(\d{4})年(\d{1,2})月(\d{1,2})日", html)
    if m:
        out["meta"]["revision_date"] = f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
    # schema.org 的 datePublished / dateModified
    m = re.search(r'"datePublished"\s*:\s*"([^"]+)"', html)
    if m:
        out["meta"]["date_published"] = m.group(1)
    m = re.search(r'"dateModified"\s*:\s*"([^"]+)"', html)
    if m:
        out["meta"]["date_modified"] = m.group(1)
    # 导读自述条数与组数：「共 N 条，分X组」
    m = re.search(r"共\s*(\d+)\s*条", html)
    if m:
        out["meta"]["stated_terms"] = int(m.group(1))
    m = re.search(r"分\s*([一二三四五六七八九十]+)\s*组", html)
    if m:
        out["meta"]["stated_groups_zh"] = m.group(1) + "组"
    m = re.search(r"(\d+)\s+entries under\s+(\w+)", html)
    if m:
        out["meta"]["stated_terms_en"] = int(m.group(1))

    # 按 H2 分节
    marks = [(m.start(), detag(m.group(1)))
             for m in re.finditer(r"<h2>(.*?)</h2>", html, re.S)]
    marks.append((len(html), "<END>"))

    for k in range(len(marks) - 1):
        s0, name = marks[k]
        s1 = marks[k + 1][0]
        seg = html[s0:s1]
        low = name.lower()

        # 一、分类导航表
        if name == "分类" or low.startswith("class"):
            j = seg.find("<table")
            if j >= 0:
                for tr in re.findall(r"<tr>(.*?)</tr>", seg[j:], re.S):
                    c = [detag(x) for x in split_cells(tr)]
                    if len(c) >= 3 and c[0] not in ("一级分类", "Class"):
                        out["classes"].append({"class": c[0], "subclasses": c[1],
                                               "count": c[2]})

        # 二、术语正文：19 组，每组一张 <table class="terms">
        elif name.startswith("术语") or low.startswith("terms"):
            heads = [(m.start(), detag(m.group(1)))
                     for m in re.finditer(r"<h3>(.*?)</h3>", seg, re.S)]
            heads.append((len(seg), "<END>"))
            for h in range(len(heads) - 1):
                g0, gname = heads[h]
                g1 = heads[h + 1][0]
                gseg = seg[g0:g1]
                j = gseg.find("<table")
                if j < 0:
                    continue
                rows = []
                for tr in re.findall(r"<tr>(.*?)</tr>", gseg[j:], re.S):
                    if "<th" in tr:            # 表头行（按标签判，不按内容判）
                        continue
                    cells = split_cells(tr)
                    if len(cells) < 4:
                        continue
                    if lang == "zh":
                        term_zh, tag_zh = strip_strong_span(cells[0])
                        tag_en = ""
                        term_en = detag(cells[1])
                        def_zh = detag(cells[2])
                        def_en = ""
                        tl = parse_termonline(cells[3], near_prefix)
                    else:
                        term_en, _ = strip_strong_span(cells[0])
                        term_zh, tag_en = strip_strong_span(cells[1])
                        tag_zh = ""
                        def_en = detag(cells[2])
                        def_zh = ""
                        tl = parse_termonline(cells[3], near_prefix)
                    rows.append({"term_zh": term_zh, "term_en": term_en,
                                 "tag_zh": tag_zh, "tag_en": tag_en,
                                 "def_zh": def_zh, "def_en": def_en,
                                 "tl_status": tl[0], "tl_term": tl[1],
                                 "tl_subject": tl[2]})
                out["groups"].append({"group": gname, "rows": rows})

        # 三、两个附录（表类名 appx）
        elif ("附录" in name or low.startswith("appendix")):
            j = seg.find("<table")
            if j < 0:
                continue
            head, rows = [], []
            for tr in re.findall(r"<tr>(.*?)</tr>", seg[j:], re.S):
                cells = split_cells(tr)
                ths = re.findall(r"<th[^>]*>(.*?)</th>", tr, re.S)
                if ths:
                    head = [detag(x) for x in ths]
                    continue
                rows.append([detag(x) for x in cells])
            # 首列（四方）空则承上行
            last = ""
            for r in rows:
                if r and r[0] == "":
                    r[0] = last
                elif r:
                    last = r[0]
            out["appendices"].append({"title": name, "header": head, "rows": rows})

        # 四、脚注（分类表下那段 em）
        else:
            for m in re.finditer(r"<p><em>(.*?)</em></p>", seg, re.S):
                out["notes"].setdefault(name, []).append(detag(m.group(1)))

    return out


# ── 英文定译修订表（本仓与源页的已知差异，逐条断言，写盘前生效） ──────────────
#
# 依据：源页 term_en 列作 `ganzhi`，而同页 def_en **本就一律用 `stem-branch`**
#       （历书 the stem-branch pair／三伏 reckoned by stem-branch days／
#        干支纪日 with a stem-branch pair／超辰 the stem-branch count，共 8 处）。
#       即词条列与自身释义不一致，此处统一到 `stem-branch`。
#       六十甲子 回 `sexagenary cycle`（该词与 干支 分工：前者指完整一轮，后者指两套符号）。
#
# 纪律：改写表写成数据，不写成散文；每条 assert 旧串在 term_en 中恰好命中一条。
TERM_EN_REVISIONS = {
    "干支":      ("ganzhi / stem-branch",
                  "stem-branch"),
    "干支纪日":   ("ganzhi day-count",
                  "stem-branch day-count"),
    "干支纪年":   ("ganzhi year-count",
                  "stem-branch year-count"),
    "六十甲子":   ("the sixty-day cycle",
                  "sexagenary cycle"),
    "六十甲子纳音": ("the nayin of the sixty-day cycle",
                  "the nayin of the sexagenary cycle"),
}

REVISION_REASON = ("源页 term_en 列作 ganzhi / sixty-day，而同一页 def_en 本就一律用 "
                   "stem-branch（共 8 处）；本仓据以统一，并把「完整一轮」交回 "
                   "sexagenary cycle，与「两套符号」分工。")


def apply_revisions(recs):
    """就地修订 term_en；返回修订留档。断言全部置于调用方写盘之前。"""
    log = []
    for zh, (old, new) in TERM_EN_REVISIONS.items():
        hits = [r for r in recs if r["term_zh"] == zh]
        assert len(hits) == 1, f"修订表词条“{zh}”在正文命中 {len(hits)} 条，应恰为 1"
        r = hits[0]
        assert r["term_en"] == old, (
            f"修订表“{zh}”旧串不符：期望 <{old}>，实得 <{r['term_en']}>")
        r["term_en"] = new
        log.append({"term_zh": zh, "group_zh": r["group_zh"],
                    "before": old, "after": new})
    return log


# ── 双语合并 ─────────────────────────────────────────────────────────────────

def merge(zh, en):
    """按（组序, 行序）逐条合并；只核 中文/English 是否一致，不做模糊匹配。"""
    assert len(zh["groups"]) == len(en["groups"]), \
        f"组数不等：zh={len(zh['groups'])} en={len(en['groups'])}"
    recs, parity = [], []
    gid = 0
    for gz, ge in zip(zh["groups"], en["groups"]):
        gid += 1
        assert len(gz["rows"]) == len(ge["rows"]), \
            f"组「{gz['group']}」条数不等：zh={len(gz['rows'])} en={len(ge['rows'])}"
        for rz, re_ in zip(gz["rows"], ge["rows"]):
            parity.append({
                "group": gz["group"],
                "term_zh": rz["term_zh"], "term_en": rz["term_en"],
                "zh_side_en": rz["term_en"], "en_side_zh": re_["term_zh"],
                "en_side_en": re_["term_en"], "zh_side_zh": rz["term_zh"],
                "term_match": rz["term_zh"] == re_["term_zh"]
                              and rz["term_en"] == re_["term_en"],
            })
            recs.append({
                "group_id": gid,
                "group_zh": gz["group"],
                "group_en": ge["group"],
                "term_zh": rz["term_zh"],
                "term_en": rz["term_en"],
                "tag_zh": rz["tag_zh"],
                "tag_en": re_["tag_en"],
                "def_zh": rz["def_zh"],
                "def_en": re_["def_en"],
                "tl_status": rz["tl_status"] if rz["tl_status"] != "none" else re_["tl_status"],
                "tl_term": rz["tl_term"] or re_["tl_term"],
                "tl_subject_zh": rz["tl_subject"],
                "tl_subject_en": re_["tl_subject"],
            })
    return recs, parity


# ── 写盘（BOM + CRLF） ───────────────────────────────────────────────────────

def write_csv(path, header, rows):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\r\n")
    w.writerow(header)
    for r in rows:
        w.writerow(["" if v is None else v for v in r])
    data = ("\ufeff" + buf.getvalue()).encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    return len(data)


def write_json(path, obj):
    data = json.dumps(obj, ensure_ascii=False, indent=1).encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    return len(data)


def write_jsonl(path, records):
    data = "".join(json.dumps(r, ensure_ascii=False) + "\n"
                   for r in records).encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    return len(data)


# ── 入口 ─────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src-dir", default="_source")
    ap.add_argument("--out", default="data")
    a = ap.parse_args()

    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    src = a.src_dir if os.path.isabs(a.src_dir) else os.path.join(root, a.src_dir)
    out = a.out if os.path.isabs(a.out) else os.path.join(root, a.out)
    os.makedirs(out, exist_ok=True)

    raw = {}
    for lang in ("zh", "en"):
        p = os.path.join(src, f"glossary_{lang}.html")
        with open(p, "rb") as f:
            b = f.read()
        raw[lang] = {"file": f"glossary_{lang}.html", "bytes": len(b),
                     "md5": hashlib.md5(b).hexdigest(),
                     "html": b.decode("utf-8", errors="replace")}
        print(f"[源] {lang}: {raw[lang]['bytes']} B  md5={raw[lang]['md5']}")

    pz = parse_page(raw["zh"]["html"], "zh")
    pe = parse_page(raw["en"]["html"], "en")

    nz = sum(len(g["rows"]) for g in pz["groups"])
    ne = sum(len(g["rows"]) for g in pe["groups"])
    print(f"[解析] zh {len(pz['groups'])} 组 / {nz} 条 | en {len(pe['groups'])} 组 / {ne} 条")
    assert nz == ne, f"中英条数不等：{nz} vs {ne}"
    assert nz > 0, "解析出 0 条 —— 选择器已失效，停"

    recs, parity = merge(pz, pe)

    # ★ 英文定译修订（断言在 apply_revisions 内，全部置于写盘之前）
    revlog = apply_revisions(recs)
    print(f"[修订] 对源页 term_en 作 {len(revlog)} 处定译修订：")
    for r in revlog:
        print(f"   {r['term_zh']:12s} {r['before']:34s} -> {r['after']}")

    # ★ 断言：全部置于写盘之前
    bad = [p for p in parity if not p["term_match"]]
    if bad:
        print(f"⚠ 中英对表不一致 {len(bad)} 条：")
        for b in bad[:10]:
            print("   ", b)
    miss = [r for r in recs
            if not (r["term_zh"] and r["term_en"] and r["def_zh"] and r["def_en"])]
    assert not miss, f"存在空字段，停：{miss[:3]}"

    # 组别条数
    cnt = Counter(r["group_id"] for r in recs)
    print("[组别条数]")
    gn = {}
    for r in recs:
        gn[r["group_id"]] = (r["group_zh"], r["group_en"])
    for gid in sorted(gn):
        print(f"   {gid:2d}. {gn[gid][0]:24s} {cnt[gid]:3d}")

    # 分类导航表核对：各一级分类条数之和 vs 正文按标签归类之和
    cls_sum = sum(int(c["count"]) for c in pz["classes"]) if pz["classes"] else 0
    print(f"[分类表] {len(pz['classes'])} 个一级分类，条数合计 {cls_sum}")
    by_tag = Counter(r["tag_zh"].split(" · ")[0]
                     for r in recs if r["tag_zh"])
    allsub = set()
    for r in recs:
        if " · " in r["tag_zh"]:
            allsub.add(r["tag_zh"].split(" · ")[1])
    print(f"[正文按标签一级归类] {len(by_tag)} 类，合计 {sum(by_tag.values())}")
    for k, v in by_tag.most_common():
        print(f"      {k:12s} {v:3d}")
    print(f"[核对] 分类表合计 {cls_sum}  vs  正文按标签合计 {sum(by_tag.values())}"
          f"  →  {'一致' if cls_sum == sum(by_tag.values()) else '★ 不一致，须在 README 如实说明'}")

    # 术语在线对标统计
    tl = Counter(r["tl_status"] for r in recs)
    print(f"[术语在线对标] 同名 {tl['exact']} / 近名 {tl['near']} / 无 {tl['none']}")

    # ── 写盘 ──
    H = ["id", "group_id", "group_zh", "group_en",
         "term_zh", "term_en", "tag_zh", "tag_en",
         "def_zh", "def_en",
         "termonline_status", "termonline_term",
         "termonline_subject_zh", "termonline_subject_en"]
    rows = [[i + 1, r["group_id"], r["group_zh"], r["group_en"],
             r["term_zh"], r["term_en"], r["tag_zh"], r["tag_en"],
             r["def_zh"], r["def_en"],
             r["tl_status"], r["tl_term"],
             r["tl_subject_zh"], r["tl_subject_en"]]
            for i, r in enumerate(recs)]
    written = {}
    written["glossary_zh_en.csv"] = write_csv(
        os.path.join(out, "glossary_zh_en.csv"), H, rows)
    written["glossary_zh_en.json"] = write_json(
        os.path.join(out, "glossary_zh_en.json"),
        {"schema": H, "count": len(rows),
         "records": [dict(zip(H, r)) for r in rows]})
    written["glossary_zh_en.jsonl"] = write_jsonl(
        os.path.join(out, "glossary_zh_en.jsonl"),
        [dict(zip(H, r)) for r in rows])

    written["classes.csv"] = write_csv(
        os.path.join(out, "classes.csv"),
        ["class_zh", "subclasses_zh", "count"],
        [[c["class"], c["subclasses"], c["count"]] for c in pz["classes"]])

    for idx, ap_ in enumerate(pz["appendices"], 1):
        fn = f"appendix_{idx}.csv"
        written[fn] = write_csv(os.path.join(out, fn),
                                ap_["header"] or [f"col{i}" for i in range(1, 6)],
                                ap_["rows"])

    written["verification_parity.csv"] = write_csv(
        os.path.join(out, "verification_parity.csv"),
        ["group_zh", "term_zh", "term_en",
         "zh_page_term_zh", "zh_page_term_en",
         "en_page_term_zh", "en_page_term_en", "match"],
        [[p["group"], p["term_zh"], p["term_en"],
          p["zh_side_zh"], p["zh_side_en"],
          p["en_side_zh"], p["en_side_en"],
          "一致" if p["term_match"] else "不一致"] for p in parity])

    # 核验表：本仓对源页英文定译的修订
    written["verification_term_revisions.csv"] = write_csv(
        os.path.join(out, "verification_term_revisions.csv"),
        ["term_zh", "group_zh", "源页 term_en（修订前）", "本仓 term_en（修订后）", "依据"],
        [[r["term_zh"], r["group_zh"], r["before"], r["after"], REVISION_REASON]
         for r in revlog])

    # 核验表：源页导读自述 vs 实测
    def g(d, k):
        return d.get(k, "")

    written["verification_stated_vs_measured.csv"] = write_csv(
        os.path.join(out, "verification_stated_vs_measured.csv"),
        ["项", "源页自述", "实测", "结论"],
        [["术语条数（中文页导读）", g(pz["meta"], "stated_terms"), len(rows),
          "一致" if g(pz["meta"], "stated_terms") == len(rows) else "★ 不符"],
         ["术语条数（英文页导读）", g(pe["meta"], "stated_terms_en"), len(rows),
          "一致" if g(pe["meta"], "stated_terms_en") == len(rows) else "★ 不符"],
         ["分组数（中文页 H3）", g(pz["meta"], "stated_groups_zh"), len(pz["groups"]),
          "一致" if g(pz["meta"], "stated_groups_zh") == "十九组"
          else "★ 不符"],
         ["二级子类数（中文页脚注）", "二十五个", len(allsub),
          "一致" if len(allsub) == 25 else "★ 不符"],
         ["分类表「术数择日」行条数", "28", by_tag.get("术数择日", 0),
          "★ 不一致：该行子类栏把同一批子类重复列了一遍（带＊与不带＊所指相同）"],
         ["分类表一级分类条数合计", cls_sum, sum(by_tag.values()),
          "★ 不一致：源页脚注自称二十五个二级子类、实测亦为 25，"
          "故以实测合计为准"]])

    # 核验表：分类导航表「表载条数」vs 正文按标签实测条数
    written["verification_classes.csv"] = write_csv(
        os.path.join(out, "verification_classes.csv"),
        ["class_zh", "subclasses_zh", "表载条数", "实测条数", "差异", "说明"],
        [[c["class"], c["subclasses"],
          c["count"], str(by_tag.get(c["class"], 0)),
          str(int(c["count"]) - by_tag.get(c["class"], 0)),
          "" if int(c["count"]) == by_tag.get(c["class"], 0)
          else "★ 表载与实测不符：该行子类栏把同一批子类重复列了一遍（带＊与不带＊所指相同），"
               "条数为重复计数"]
         for c in pz["classes"]])

    # schema.org DefinedTermSet —— 供知识图谱与检索器直接消费
    termset = {
        "@context": "https://schema.org",
        "@type": "DefinedTermSet",
        "@id": "https://github.com/Kuangchujia/chinese-calendar-glossary#termset",
        "name": "中国历法与古天文学术语对照表（中英双语）",
        "alternateName": "Chinese Calendrical & Uranographical Glossary (Chinese–English)",
        "description": f"中国历法与古天文学术语 {len(rows)} 条，分 {len(pz['groups'])} 组，"
                       f"每条给中文名、英文定译、中文释义与英文释义，"
                       f"另标一级分类（{len(pz['classes'])} 个）与二级子类（{len(allsub)} 个）。",
        "inLanguage": ["zh-CN", "en"],
        "version": "1.0.0",
        "datePublished": pz["meta"].get("date_published", ""),
        "dateModified": pz["meta"].get("date_modified", ""),
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "creator": {
            "@type": "Person",
            "name": "邝楚嘉",
            "alternateName": "Chujia Kuang",
            "identifier": "https://orcid.org/0009-0002-7650-833X",
        },
        "hasDefinedTerm": [
            {
                "@type": "DefinedTerm",
                "identifier": str(i + 1),
                "name": r["term_zh"],
                "alternateName": r["term_en"],
                "termCode": r["tag_zh"],
                "description": r["def_zh"],
                "inDefinedTermSet": f"https://github.com/Kuangchujia/chinese-calendar-glossary#group-{r['group_id']}",
            }
            for i, r in enumerate(recs)
        ],
    }
    written["glossary_term_set.jsonld"] = write_json(
        os.path.join(out, "glossary_term_set.jsonld"), termset)

    manifest = {
        "title": "中国历法与古天文学术语对照表（中英双语）",
        "generated_by": "code/build_glossary.py",
        "source_pages": [dict({k: v for k, v in raw[l].items() if k != "html"},
                              revision_date=pg["meta"].get("revision_date", ""),
                              date_published=pg["meta"].get("date_published", ""),
                              date_modified=pg["meta"].get("date_modified", ""))
                         for l, pg in (("zh", pz), ("en", pe))],
        "stated_by_source": {
            "terms_zh_page": pz["meta"].get("stated_terms"),
            "terms_en_page": pe["meta"].get("stated_terms_en"),
            "groups_zh_page": pz["meta"].get("stated_groups_zh"),
            "subclasses_zh_page": 25,
        },
        "english_revisions": {
            "count": len(revlog),
            "reason": REVISION_REASON,
            "items": revlog,
        },
        "counts": {"terms": len(rows),
                   "groups": len(pz["groups"]),
                   "subclasses": len(allsub),
                   "classes": len(pz["classes"]),
                   "appendices": len(pz["appendices"]),
                   "parity_mismatch": len(bad),
                   "classes_table_total_vs_measured": [cls_sum, sum(by_tag.values())]},
        "termonline": dict(tl),
        "files": written,
    }
    written["source_manifest.json"] = write_json(
        os.path.join(out, "source_manifest.json"), manifest)

    print("\n[写盘]")
    for k in sorted(written):
        print(f"   {k:32s} {written[k]:>9,} B")
    print(f"\n[总计] {sum(written.values()):,} B")
    print(f"[对表] 不一致 {len(bad)} / {len(parity)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
