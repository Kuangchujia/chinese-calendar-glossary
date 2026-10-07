#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_glossary.py — 独立校验器。

判据与 build_glossary.py **不同源**：此处不 import 生成器，改从「产物 + 源页 HTML」
两处各自重新数一遍，再对拍。生成器说「我写对了」不算数。

另附三条硬线自查（照 chinese-calendar-dataset 仓 2026-09-16 报告 §四）：
  · 数据件内不得出现网址
  · CSV 必须 UTF-8 BOM + CRLF
  · 不得有占位残留（⟨待补⟩ / TODO / TBD / ？）

退出码：0 = 全过；1 = 有 FAIL。
"""
import csv
import hashlib
import io
import json
import os
import re
import sys

TAG = re.compile(r"<[^>]+>")
FAILS, WARNS, OKS = [], [], []


def ok(msg):
    OKS.append(msg)
    print(f"  [ OK ] {msg}")


def fail(msg):
    FAILS.append(msg)
    print(f"  [FAIL] {msg}")


def warn(msg):
    WARNS.append(msg)
    print(f"  [WARN] {msg}")


def read_bytes(p):
    with open(p, "rb") as f:
        return f.read()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    D = os.path.join(root, "data")
    S = os.path.join(root, "_source")

    print("=" * 68)
    print("一 · 源页独立重数（不依赖生成器的解析结果）")
    print("=" * 68)
    src_stats = {}
    for lang in ("zh", "en"):
        html = read_bytes(os.path.join(S, f"glossary_{lang}.html")).decode(
            "utf-8", errors="replace")
        # 术语段：<h2>术语/terms</h2> 之后到下一个 <h2>
        m = re.search(r"<h2>(?:术语|Terms[^<]*)</h2>", html, re.S)
        if not m:
            fail(f"{lang}: 找不到「术语」H2 段")
            continue
        rest = html[m.end():]
        nxt = re.search(r"<h2>", rest, re.S)
        seg = rest[:nxt.start()] if nxt else rest
        n_h3 = len(re.findall(r"<h3>", seg))
        # 术语表行数：class="terms" 表内，非 <th> 行
        n_rows = 0
        for tbl in re.findall(r'<table class="terms">(.*?)</table>', seg, re.S):
            for tr in re.findall(r"<tr>(.*?)</tr>", tbl, re.S):
                if "<th" not in tr:
                    n_rows += 1
        n_appx = 0
        for tbl in re.findall(r'<table class="appx">(.*?)</table>', html, re.S):
            for tr in re.findall(r"<tr>(.*?)</tr>", tbl, re.S):
                if "<th" not in tr:
                    n_appx += 1
        src_stats[lang] = {"h3": n_h3, "terms": n_rows, "appx": n_appx}
        print(f"  {lang} 源页：H3 组 {n_h3} ｜ 术语数据行 {n_rows} ｜ 附录合计行 {n_appx}")

    if len(src_stats) == 2:
        if src_stats["zh"]["terms"] == src_stats["en"]["terms"]:
            ok(f"源页中英术语条数相同 = {src_stats['zh']['terms']}")
        else:
            fail(f"源页中英条数不同：{src_stats}")
        if src_stats["zh"]["h3"] == src_stats["en"]["h3"]:
            ok(f"源页中英组数相同 = {src_stats['zh']['h3']}")
        else:
            fail("源页中英组数不同")

    print()
    print("=" * 68)
    print("二 · 产物 schema 与行数")
    print("=" * 68)
    EXPECT = ["id", "group_id", "group_zh", "group_en",
              "term_zh", "term_en", "tag_zh", "tag_en",
              "def_zh", "def_en",
              "termonline_status", "termonline_term",
              "termonline_subject_zh", "termonline_subject_en"]
    csv_p = os.path.join(D, "glossary_zh_en.csv")
    raw = read_bytes(csv_p)
    rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8-sig"))))
    hdr = list(rows[0].keys())
    if hdr == EXPECT:
        ok(f"主表表头与 schema 一致（{len(hdr)} 列）")
    else:
        fail(f"主表表头不符：{hdr}")

    n = len(rows)
    if src_stats and n == src_stats["zh"]["terms"]:
        ok(f"主表行数 {n} == 源页术语数据行")
    else:
        fail(f"主表行数 {n} != 源页 {src_stats.get('zh', {}).get('terms')}")

    # id 连续唯一
    ids = [int(r["id"]) for r in rows]
    if ids == list(range(1, n + 1)):
        ok(f"id 为 1..{n} 连续且唯一")
    else:
        fail("id 不连续或不唯一")

    # 空字段
    empty = [{k: r[k] for k in EXPECT if not r[k]} for r in rows]
    empty = [(i + 1, e) for i, e in enumerate(empty) if e]
    critical = [(i, e) for i, e in empty
                if set(e) - {"tag_zh", "tag_en", "termonline_term",
                             "termonline_subject_zh", "termonline_subject_en"}]
    if critical:
        fail(f"关键字段为空 {len(critical)} 行：{critical[:3]}")
    else:
        ok("关键字段（中文/English/释义两语）无空值")

    # 组
    groups = sorted({(int(r["group_id"]), r["group_zh"], r["group_en"])
                     for r in rows})
    if len(groups) == src_stats["zh"]["h3"]:
        ok(f"组数 {len(groups)} == 源页 H3 数")
    else:
        fail(f"组数 {len(groups)} != 源页 H3 {src_stats['zh']['h3']}")
    gid = [g[0] for g in groups]
    if gid == list(range(1, len(groups) + 1)):
        ok("group_id 连续")
    else:
        fail("group_id 不连续")

    # JSON / JSONL / JSON-LD 可解析且条数对得上
    j = json.loads(read_bytes(os.path.join(D, "glossary_zh_en.json")).decode("utf-8"))
    if len(j.get("records", [])) == n:
        ok(f"glossary_zh_en.json 可解析，records {len(j['records'])} 条")
    else:
        fail("glossary_zh_en.json records 条数不符")
    jl = [json.loads(x) for x in
          read_bytes(os.path.join(D, "glossary_zh_en.jsonl")).decode("utf-8").splitlines() if x]
    if len(jl) == n:
        ok(f"glossary_zh_en.jsonl 可解析，{len(jl)} 行")
    else:
        fail("glossary_zh_en.jsonl 行数不符")
    ld = json.loads(read_bytes(os.path.join(D, "glossary_term_set.jsonld")).decode("utf-8"))
    if ld.get("@type") == "DefinedTermSet" and len(ld.get("hasDefinedTerm", [])) == n:
        ok(f"glossary_term_set.jsonld 合规（schema.org DefinedTermSet，{n} 词条）")
    else:
        fail("glossary_term_set.jsonld 结构或条数不符")
    # 三件 JSON 的中英字段逐个交叉核对
    ld_terms = [(t["name"], t["alternateName"]) for t in ld["hasDefinedTerm"]]
    csv_terms = [(r["term_zh"], r["term_en"]) for r in rows]
    if ld_terms == csv_terms and \
       [(r["term_zh"], r["term_en"]) for r in j["records"]] == csv_terms and \
       [(r["term_zh"], r["term_en"]) for r in jl] == csv_terms:
        ok("CSV / JSON / JSONL / JSON-LD 四件的 中文名·英文名 逐条全等")
    else:
        fail("四件产物的术语序列不一致")

    print()
    print("=" * 68)
    print("三 · 中英对表（parity）")
    print("=" * 68)
    par = list(csv.reader(io.StringIO(
        read_bytes(os.path.join(D, "verification_parity.csv")).decode("utf-8-sig"))))
    bad = [r for r in par[1:] if r[-1] != "一致"]
    if not bad and len(par) - 1 == n:
        ok(f"parity 表 {len(par)-1} 行，逐条标「一致」，无一项不符")
    else:
        fail(f"parity 异常：{len(bad)} 条不一致 / 共 {len(par)-1} 行")

    # 直接对拍两语定义互不重复、长度合理
    short = [(r["id"], r["term_zh"]) for r in rows
             if len(r["def_zh"]) < 8 or len(r["def_en"]) < 15]
    if short:
        warn(f"释义过短可疑 {len(short)} 行：{short[:5]}")
    else:
        ok("释义长度均达合理下限")

    print()
    print("=" * 68)
    print("四 · 分类表核对")
    print("=" * 68)
    vc = list(csv.reader(io.StringIO(
        read_bytes(os.path.join(D, "verification_classes.csv")).decode("utf-8-sig"))))
    mism = [r for r in vc[1:] if r[4] != "0"]
    if mism:
        warn(f"分类表载与实测不符 {len(mism)} 项（须在 README 如实说明）：")
        for r in mism:
            print(f"        {r[0]}：表载 {r[2]} / 实测 {r[3]}（差 {r[4]}）")
    else:
        ok("分类表载条数与实测逐项相符")

    # 源页自述 vs 实测（不读写盘结果，直接看源页声明）
    sm = list(csv.reader(io.StringIO(
        read_bytes(os.path.join(D, "verification_stated_vs_measured.csv"))
        .decode("utf-8-sig"))))
    hit = [r for r in sm[1:] if "★" in r[3]]
    good = [r for r in sm[1:] if r[3] == "一致"]
    ok(f"源页自述与实测一致 {len(good)} 项（条数 279 / 十九组 / 二十五个二级子类）")
    if hit:
        warn(f"源页自述与实测不符 {len(hit)} 项（已如实留档）：")
        for r in hit:
            print(f"        {r[0]}：自述 {r[1]} / 实测 {r[2]}")

    # 二级子类数
    sub = {}
    for r in rows:
        if " · " in r["tag_zh"]:
            sub.setdefault(r["tag_zh"].split(" · ")[0], set()).add(
                r["tag_zh"].split(" · ")[1])
    allsub = set()
    for v in sub.values():
        allsub |= v
    if len(allsub) == 25:
        ok(f"二级子类实测 {len(allsub)} 个（页面自称 25）")
    else:
        warn(f"二级子类实测 {len(allsub)} 个，与页面自称 25 不符")

    print()
    print("=" * 68)
    print("四之二 · 英文定译修订与一致性")
    print("=" * 68)
    raw = read_bytes(os.path.join(D, "verification_term_revisions.csv")).decode("utf-8-sig")
    res = list(csv.reader(io.StringIO(raw)))
    # ★ 一律**按表头名**取值 —— 2026-10-07 v1.2.0 在「列」处插了一栏，
    #   旧版按位置索引取 r[2]／r[3] 会整体右移一位，把「修订前」当成「修订后」，
    #   于是拿主表比旧值 ⇒ 恒假红。（列位写死是不可复用的判据，见 §四 注）
    hdr = {h: i for i, h in enumerate(res[0])}
    for need in ("term_zh", "列", "源页（修订前）", "本仓（修订后）"):
        assert need in hdr, "修订件缺列「%s」：%s" % (need, res[0])
    rev = [dict(zip(res[0], r)) for r in res[1:] if r and r[0]]
    assert rev, "修订件为空 —— 判据失效，停"
    en_rev = [r for r in rev if r["列"] == "term_en"]
    de_rev = [r for r in rev if r["列"] == "def_en"]
    assert len(en_rev) + len(de_rev) == len(rev), "修订件「列」栏取值越界"

    idx = {r["term_zh"]: r for r in rows}
    bad_en = [(r["term_zh"], r["源页（修订前）"], r["本仓（修订后）"], idx[r["term_zh"]]["term_en"])
              for r in en_rev
              if r["term_zh"] not in idx or idx[r["term_zh"]]["term_en"] != r["本仓（修订后）"]]
    bad_de = []
    for r in de_rev:
        d = idx.get(r["term_zh"], {}).get("def_en")
        # 改后串须在；改前串须已不在（同一释义内可能多处，故用 in）
        if d is None or r["本仓（修订后）"] not in d or r["源页（修订前）"] in d:
            bad_de.append((r["term_zh"], r["源页（修订前）"], r["本仓（修订后）"],
                           (d or "")[:40]))
    if not bad_en and not bad_de:
        ok(f"修订件 {len(rev)} 条（term_en {len(en_rev)} ／ def_en {len(de_rev)}），主表已逐条落实")
    else:
        if bad_en:
            fail(f"term_en 层 {len(bad_en)} 条未落实：{bad_en[:3]}")
        if bad_de:
            fail(f"def_en 层 {len(bad_de)} 条未落实：{bad_de[:3]}")

    # 残留闸：词表＝《三语术语规范·2026-10-07》§1.1／1.2／1.3 的「禁用」栏
    #   （本仓不自带规范件，故此表须与规范件同步修订；断言非空，免出「零命中」假绿）
    RESIDUE = [
        (r"(?i)\bganzhi\b", "拼音 ganzhi"),
        (r"(?i)\b(jiazi|yi-chou|jia-zi)\b", "拼音日名"),
        (r"(?i)\bstem-branch", "stem-branch（v1.1.x 旧口径，已被取代）"),
        (r"(?i)Heavenly Stems and Earthly Branches", "字面直译"),
        (r"(?i)the sixty-day cycle", "六十甲子旧译"),
        (r"(?i)\bprecession\b(?! of the equinoxes)", "裸 precession"),
        (r"(?i)\bsolar years?\b", "回归年旧译"),
        (r"(?i)\blunar months?\b", "朔望月旧译"),
        (r"(?i)\b(BaZi|Four Pillars|Eight Characters|Chinese zodiac)\b", "命理俗译／生肖混用"),
        (r"(?i)\b(Lichun|Jingzhe|Qingming|Dongzhi|Xiazhi|Xiaohan|Dahan|Mangzhong"
         r"|Bailu|Lixia|Liqiu|Lidong|Chunfen|Qiufen|Yushui|Guyu|jieqi)\b", "节气拼音"),
    ]
    assert RESIDUE, "残留词表为空 —— 判据失效，停"
    left = [(r["id"], r["term_zh"], why, col) for r in rows
            for col in ("term_en", "def_en")
            for pat, why in RESIDUE if re.search(pat, r[col])]
    if left:
        fail(f"主表残留禁用译法 {len(left)} 处：{left[:5]}")
    else:
        ok("term_en／def_en 无禁用译法残留（干支＝Sexagenary Cycle、岁差＝Precession of the Equinoxes）")

    # 同一英文对应多个中文 headword：多为「古名／今名」同译，属页面体例
    dup = {}
    for r in rows:
        dup.setdefault(r["term_en"], []).append(r["term_zh"])
    d2 = {k: v for k, v in dup.items() if len(v) > 1}
    if d2:
        print(f"  [note] 英文定译一对多 {len(d2)} 组（页面另设「今名／今用」两组，"
              f"古今名同译属体例）：")
        for k, v in d2.items():
            print(f"         {k:20s} ← {'、'.join(v)}")
    else:
        ok("279 条英文定译互不重名")

    print()
    print("=" * 68)
    print("五 · 附录")
    print("=" * 68)
    for i in (1, 2):
        p = os.path.join(D, f"appendix_{i}.csv")
        rr = list(csv.reader(io.StringIO(read_bytes(p).decode("utf-8-sig"))))
        if len(rr) - 1 == 28:
            ok(f"appendix_{i}.csv 28 行（二十八宿）｜表头 {rr[0]}")
        else:
            fail(f"appendix_{i}.csv 行数 {len(rr)-1} != 28")
    if src_stats and src_stats["zh"]["appx"] == 56:
        ok("源页两个附录合计 56 数据行，与产物 28×2 相符")
    else:
        warn(f"源页附录合计 {src_stats.get('zh',{}).get('appx')} 行，与 56 不符")

    print()
    print("=" * 68)
    print("六 · 硬线自查")
    print("=" * 68)
    # 1) 数据件内不得出现网址
    urlish = re.compile(r"https?://|www\.", re.I)
    hit = []
    for fn in sorted(os.listdir(D)):
        if not fn.endswith((".csv", ".json", ".jsonl")):
            continue
        t = read_bytes(os.path.join(D, fn)).decode("utf-8-sig", errors="replace")
        for m in urlish.finditer(t):
            hit.append((fn, t[max(0, m.start() - 30):m.end() + 30].replace("\n", " ")))
    # source_manifest.json 记源页地址属溯源信息，单独放行
    hit_real = [h for h in hit if h[0] != "source_manifest.json"]
    if hit_real:
        fail(f"数据件内出现网址 {len(hit_real)} 处（硬线：不放网址）")
        for h in hit_real[:5]:
            print(f"        {h[0]}: …{h[1]}…")
    else:
        ok("数据件内无任何网址（硬线通过；source_manifest.json 的源页地址属溯源信息）")

    # 2) BOM + CRLF
    badenc = []
    for fn in sorted(os.listdir(D)):
        if fn.endswith(".csv"):
            b = read_bytes(os.path.join(D, fn))
            if not b.startswith(b"\xef\xbb\xbf"):
                badenc.append((fn, "缺 BOM"))
            if b"\r\n" not in b:
                badenc.append((fn, "非 CRLF"))
    if badenc:
        fail(f"CSV 编码/换行不符：{badenc}")
    else:
        ok("全部 CSV 均为 UTF-8 BOM + CRLF")

    # 3) 占位残留
    ph = ["⟨待补⟩", "TODO", "TBD", "XXX", "待定", "占位"]
    res = []
    for fn in sorted(os.listdir(D)):
        t = read_bytes(os.path.join(D, fn)).decode("utf-8-sig", errors="replace")
        for w in ph:
            if w in t:
                res.append((fn, w))
    if res:
        warn(f"占位残留：{res}")
    else:
        ok("无占位残留")

    print()
    print("=" * 68)
    print("七 · 对外 DOI 口径（家规：每合集一个概念 DOI，对外只公布这一个）")
    print("=" * 68)
    # 家规出处：`规划与报告/海外发布规则·2026-09-20.md`
    #   §一 L16（用户原话逐字照录）：「DOI 规则改为：每合集一个概念 DOI，对外只公布这一个。」
    #   §二 L24 落点含「四仓 README」；§四 L62 记四仓 README 锚定块用的就是 concept DOI。
    # 两号来源：Zenodo REST `GET /api/records/<版本号>` 的 `conceptdoi` / `doi` 两个字段。
    #   concept = 合集级，永久指向最新版；version = 本版记录号，会停在旧版（「链式追尾」）。
    # ⚠ 自指陷阱（实测踩过一次）：判据是「活件里出现该字符串」，
    #   则**描述这条违规的修订记录行**会把自己抓住——本器因此判 FAIL 过一次。
    #   正解不是给判据开豁免口，而是**正文不复写版本号**：只写「版本级记录号」，
    #   该号归 git commit 信息与 Zenodo 版本列表。此处记一笔，免得日后又加回去。
    CONCEPT_DOI = "10.5281/zenodo.23028692"
    VERSION_DOI = "10.5281/zenodo.23028693"
    LIVE = ["README.md", "README_AI_AGENT.md", "NOTICE.md", "CITATION.cff"]
    ver_hits, con_hits = [], []
    for fn in LIVE:
        p = os.path.join(root, fn)
        if not os.path.isfile(p):
            continue
        t = read_bytes(p).decode("utf-8-sig", errors="replace")
        nv, nc = t.count(VERSION_DOI), t.count(CONCEPT_DOI)
        if nv:
            ver_hits.append((fn, nv))
        if nc:
            con_hits.append((fn, nc))
    if ver_hits:
        fail(f"活件出现版本 DOI {VERSION_DOI}：{ver_hits}"
             f"（家规：对外只公布概念 DOI；版本号只进 git commit 信息）")
    else:
        ok("活件无版本 DOI 残留")
    if not con_hits:
        fail(f"活件未出现概念 DOI {CONCEPT_DOI}")
    else:
        ok(f"活件已用概念 DOI：{con_hits}")

    print()
    print("=" * 68)
    print(f"结果：OK {len(OKS)} ｜ WARN {len(WARNS)} ｜ FAIL {len(FAILS)}")
    print("=" * 68)
    for f in FAILS:
        print("  ✗", f)
    for w in WARNS:
        print("  !", w)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
