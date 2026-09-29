#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch_source.py — 抓取源页 HTML 到 _source/（供 build_glossary.py 解析）。

源页：本站「术语」栏目中英两页，条目逐条对应。
本脚本只做「取回＋落盘＋记 md5」，不做任何改写。

用法：
  python code/fetch_source.py --out _source
"""
import argparse
import hashlib
import os
import sys
import time
import urllib.error
import urllib.request

PAGES = {
    "zh": "https://kuangchujia.com/glossary/zh/",
    "en": "https://kuangchujia.com/glossary/en/",
}
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122.0 Safari/537.36")


def fetch(url, tries=4):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA,
                                                       "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:       # 4xx/5xx 是语义结果，不重试
            return e.code, e.read()
        except Exception as e:                    # 只重试连接层抖动
            last = e
            time.sleep(1.5 * (i + 1))
    raise last


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="_source")
    a = ap.parse_args()
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    out = a.out if os.path.isabs(a.out) else os.path.join(root, a.out)
    os.makedirs(out, exist_ok=True)

    rows = []
    for lang, url in PAGES.items():
        code, body = fetch(url)
        assert code == 200, f"[{lang}] HTTP {code} —— 抓取失败，停"
        assert len(body) > 50_000, f"[{lang}] 仅 {len(body)} B，疑似未取到正文，停"
        p = os.path.join(out, f"glossary_{lang}.html")
        with open(p, "wb") as f:
            f.write(body)
        md5 = hashlib.md5(body).hexdigest()
        rows.append((lang, url, code, len(body), md5))
        print(f"[{lang}] HTTP {code}  {len(body):,} B  md5={md5}  -> {p}")
    print(f"\n共 {len(rows)} 页。接着跑：python code/build_glossary.py --src-dir {a.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
