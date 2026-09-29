# Chinese Calendrical & Uranographical Glossary (Chinese–English)

**[中文](README.md) ｜ English**

<!-- badges -->

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23028692.svg)](https://doi.org/10.5281/zenodo.23028692) [![Data: CC BY 4.0](https://img.shields.io/badge/Data-CC%20BY%204.0-lightgrey.svg)](LICENSE) [![ORCID](https://img.shields.io/badge/ORCID-0009--0002--7650--833X-a6ce39.svg)](https://orcid.org/0009-0002-7650-833X) [![OpenAlex](https://img.shields.io/badge/OpenAlex-A5151908354-ff6f00.svg)](https://openalex.org/A5151908354) [![Site](https://img.shields.io/badge/site-kuangchujia.com-blue.svg)](https://kuangchujia.com)

> **A bilingual Chinese–English glossary of Chinese calendrical and uranographical terms — downloadable, citable and checkable.**
> **279 terms** in 19 groups; each gives a **Chinese name · a fixed English rendering · a Chinese definition · an English definition**, and marks its correspondence with Termonline (the terminology platform of China's National Committee for Terms in Sciences and Technologies).
> Two stand-alone correspondence tables are appended: the **determinative stars of the twenty-eight lunar mansions across three sources** (28 rows) and the **star officers and star counts of the twenty-eight mansions** (28 rows).
> DOI: 10.5281/zenodo.23028692 ｜ Licence CC BY 4.0 ｜ Version v1.0.1
> **Machine-readable edition (for AI agents and LLM crawlers):** [`README_AI_AGENT.md`](README_AI_AGENT.md) — structured statements of the same facts, field tables and a self-check list.

*A Chinese–English glossary of calendrical and uranographical terms — downloadable, citable and checkable. 279 terms in 19 groups, each with a Chinese name, a fixed English rendering and a definition in both languages, together with its correspondence to Termonline, the terminology platform of China's National Committee for Terms in Sciences and Technologies. Two stand-alone tables are appended: the determinative stars of the twenty-eight lunar mansions across three sources (28 rows), and the star officers and star counts of the twenty-eight mansions (28 rows). DOI: 10.5281/zenodo.23028692 · CC BY 4.0 · v1.0.1. A machine-readable edition is available in `README_AI_AGENT.md`.*

<!-- ANCHOR-BLOCK-BEGIN -->
## ★ Where this project sits in the academic network

> **Academic Lineage & Linked Identity**

| Item | Address |
|:---|:---|
| **Author (Creator)** | Chujia Kuang (邝楚嘉 / pen name Jiayan Yide 嘉言一得) |
| **ORCID iD** | [0009-0002-7650-833X](https://orcid.org/0009-0002-7650-833X) |
| **OpenAlex Index** | [A5151908354](https://openalex.org/A5151908354) |
| **Home site / umbrella entry point to all outputs (Verification Hub)** | <https://kuangchujia.com> |
| **This repository** | <https://github.com/Kuangchujia/chinese-calendar-glossary> |
| **Dataset DOI (Zenodo)** | [10.5281/zenodo.23028692](https://doi.org/10.5281/zenodo.23028692) |
| **Sibling dataset (the three-part calendar set)** | <https://github.com/Kuangchujia/chinese-calendar-dataset> |
| **Companion preprint mirror repository** | <https://github.com/Kuangchujia/kuangchujia-preprints> |

**What this repository is**: a **terminology correspondence table** — for a set of words in Chinese calendrics and uranography that cannot be avoided, it gives a Chinese name, a fixed English rendering and a definition in both languages, and marks item by item the correspondence with the national terminology database. **It is not a calendar-day computation table**; the three kinds of computed data — solar-term instants, the historical calendar chronology and the sexagenary day table — are in the sibling repository `chinese-calendar-dataset`.

**What the fixed renderings are for**: to be cited by Chinese–English writing and translation in sinology, the history of science and the history of astronomy; and to let AI agents and LLMs align concepts when reading Chinese astronomical and calendrical sources. **The English renderings aim only at "denoting the right thing and translating back either way"**, not at literary quality.
<!-- ANCHOR-BLOCK-END -->

---

## I. What is in this data

| # | Asset | File | Rows | Content |
|:--:|:---|:---|:--:|:---|
| **G1** | **Main term table** | `data/glossary_zh_en.csv`<br>`data/glossary_zh_en.json`<br>`data/glossary_zh_en.jsonl` | **279** | Chinese name / fixed English rendering / classification tag (zh and en) / Chinese definition / English definition / Termonline correspondence |
| **G2** | **Classification navigation table** | `data/classes.csv` | **6** first-level classes | First-level class · second-level subclasses and their counts · count |
| **G3** | **Appendix 1 · Determinative stars of the twenty-eight mansions** | `data/appendix_1.csv` | **28** rows | Quadrant / mansion / Tang *Kaiyuan Zhanjing* juan 106 / Yuan *Songshi · Tianwenzhi* / Ming–Qing to the present (in current use) |
| **G4** | **Appendix 2 · Star officers and star counts of the twenty-eight mansions** | `data/appendix_2.csv` | **28** rows | Quadrant / mansion / number of star officers / number of stars |
| **G5** | **Semantic file** | `data/glossary_term_set.jsonld` | **279** entries | schema.org `DefinedTermSet`, for direct consumption by knowledge graphs and retrievers |

The same directory holds five **verification files** (not the data itself, but for re-checking):

| File | Role |
|:---|:---|
| `data/verification_parity.csv` | Item-by-item comparison of the Chinese and English pages (279 rows) |
| `data/verification_term_revisions.csv` | The repository's **5 revisions** to the source page's `term_en` (before / after / grounds) |
| `data/verification_classes.csv` | Counts as stated in the classification table vs counts as measured, item by item |
| `data/verification_stated_vs_measured.csv` | What the source page **states** (introduction, footnote) vs what was measured |
| `data/source_manifest.json` | Source page files, byte counts, md5, **revision time**, publication and modification instants, and the various counts |

---

## II. G1 · Main term table

### Fields

| Field | Notes |
|:---|:---|
| `id` | Index, 1–279, in source-page order |
| `group_id` | Group number, 1–19 |
| `group_zh` / `group_en` | Group heading (Chinese / English) |
| `term_zh` | Chinese headword |
| `term_en` | Fixed English rendering |
| `tag_zh` / `tag_en` | Classification tag, of the form `历法术语 · 总论` / `Calendrical terms · general` |
| `def_zh` | Chinese definition (one sentence) |
| `def_en` | English definition (one sentence) |
| `termonline_status` | Correspondence with Termonline: `exact` (same name) / `near` (close name) / `none` (not recorded) |
| `termonline_term` | The headword recorded by Termonline (`exact` and `near` only) |
| `termonline_subject_zh` / `_en` | The subject classification of that Termonline entry (Chinese / English) |

### Groups and counts

| Group | Heading | Count |
|:--:|:---|:--:|
| 1 | I · Calendars and calendrical computation | 20 |
| 2 | II · The year-beginning, the month branch and intercalation | 16 |
| 3 | III · Solar terms and phenology | 17 |
| 4 | IV · Counting days, years and hours | 22 |
| 5 | V · New moon, full moon, lunar phases and eclipses | 17 |
| 6 | VI · The starry sky, coordinates and measurement | 25 |
| 7 | VII · Instruments, star officials and star charts | 13 |
| 8 | VIII · The calendar's history and use | 14 |
| 9 | IX · The five planets and planetary phenomena | 13 |
| 10 | X · The three enclosures and the circumpolar region | 8 |
| 11 | XI · The four images and the twenty-eight mansions | 32 |
| 12 | XII · Star names, star catalogues, the Milky Way and cosmology | 9 |
| 13 | XIII · Lunar phases (modern names) | 9 |
| 14 | XIV · Periods of year and month, and time systems (in modern use) | 15 |
| 15 | XV · The twelve double-hour names | 12 |
| 16 | XVI · Coordinates and culmination (in modern use) | 9 |
| 17 | XVII · Exceptional phenomena | 7 |
| 18 | XVIII · Observational instruments (supplement) | 7 |
| 19 | XIX · Divination and day-selection | 14 |
| | **Total** | **279** |

### Correspondence with Termonline

The fourth column group (`termonline_*`) gives the correspondence with [Termonline](https://www.termonline.cn/) (the National Committee for Terms in Sciences and Technologies). **Criterion**: a correspondence is marked only where that database holds an entry and its subject is classified under **astronomy**; where the entry it holds has a **different name**, the row is marked `near` and that other term is given in `termonline_term`.

| Correspondence | Count |
|:---|--:|
| `exact` same name | **147** |
| `near` close name | **21** |
| `none` not recorded | **111** |
| **Total** | **279** |

> **⚠ The `term_en` column is not a verbatim transcription of the source page**: **5 rows** have been revised (see section V), and the remaining 274 are byte-identical to the source. `def_zh` / `def_en` / `tag_*` / `termonline_*` are **reproduced verbatim with no change of any kind**.

> **No URLs are stored inside the data files** (a standing constraint of this repository). `termonline_term` holds the **headword** only and the subject as **text**; the search entry point for Termonline is <https://www.termonline.cn/>, where the headword can be looked up. This trade-off can be reversed in a single sentence: to store URLs directly in the data files, change the return value of `parse_termonline()` in `code/build_glossary.py`.

---

## III. G2–G4 · The classification table and the two appendices

### G2 Classification navigation table — one source-page defect that must be stated

`classes.csv` **reproduces the source page's** classification navigation table. On checking it, **5 of the 6 first-level classes match the body counts item by item; only the row for "术数择日" does not**.

| First-level class | Count in table | Count as measured | Difference |
|:---|--:|--:|--:|
| 天文基础 (Foundations of astronomy) | 90 | 90 | 0 |
| 历法术语 (Calendrical terms) | 56 | 56 | 0 |
| 天象类 (Celestial phenomena) | 36 | 36 | 0 |
| 星宿与星官 (Mansions and star officials) | 50 | 50 | 0 |
| 律历制度 (Pitch-pipes and calendar institutions) | 33 | 33 | 0 |
| **术数择日 (Divination and day-selection)** | **28** | **14** | **+14** |

**Cause**: that row's second-level subclass column lists **one and the same set of subclasses twice** — "择日 5、神煞 8、纳音 1、（＊）择日 5、神煞＊ 8、纳音＊ 1". The items with and without the asterisk refer to the same thing, so 28 = 14 × 2. The other five classes show no such repetition.

**Which figure is correct**: **279**. Four independent lines of evidence —
1. **The actual number of data rows in the body**: data rows inside `<table class="terms">`, re-counted separately on each of the Chinese and English pages, **279 in both**;
2. **Classifying every row by its classification tag**: the six first-level classes sum to **279** as measured;
3. **The source page's footnote states "twenty-five second-level subclasses"**, and exactly **25** are measured, summing to **279** — incompatible with 293;
4. **The source page's introduction states "279 entries in nineteen groups"** — the site's own figure is 279.

This repository **did not alter the source page** (site changes are by default reported, not made). `verification_classes.csv` and `verification_stated_vs_measured.csv` preserve the two figures side by side, **without offering a concluding "correct value"** — users may judge for themselves. If the source page is corrected later, re-running the generator is all that is needed.

### G3 Appendix 1 · Determinative stars of the twenty-eight mansions across three sources

28 rows, one mansion per row, listing **the different records three historical sources give of "which star is this mansion's determinative star"**, together with the star to which it corresponds in current usage.

| Quadrant | Mansion | Tang *Kaiyuan Zhanjing* juan 106 | Yuan *Songshi · Tianwenzhi* | Ming–Qing to the present (in current use) |
|:---|:---|:---|:---|:---|
| 东方苍龙 (Azure Dragon of the East) | 角宿 (Jiao) | 左角星 | 南星 | 角宿一（室女座 α） |

> The "quadrant" column is a merged cell in the original table; here it has been **filled in row by row** (each row repeats the name of its quadrant) for ease of programmatic use. The original table's "未记" (not recorded) is reproduced verbatim.

### G4 Appendix 2 · Star officers and star counts of the twenty-eight mansions

28 rows, one mansion per row, giving that mansion's **number of star officers and number of stars** (for example Jiao: 11 star officers, 45 stars).

---

## IV. Chinese–English parity

The source page states that "the entries correspond item by item with the English page, with nothing missing on either side". This repository **measured it item by item**:

| Metric | Result |
|:---|:---|
| Rows on the Chinese page | **279** |
| Rows on the English page | **279** |
| Groups | **19 / 19** |
| Rows whose `term_zh` + `term_en` match exactly | **279 / 279** |
| **Mismatches** | **0** |

The detailed comparison is in `data/verification_parity.csv`. The check compares rows **by position, in order** (no fuzzy matching, no name normalisation); a difference in either the Chinese or the English name of any row is recorded as a mismatch.

---

## V. English renderings: the repository's 5 revisions to the source page

**This must be said first**: the `term_en` column of G1 is **not** a verbatim transcription of the source page, but has been **revised in 5 places**. The revisions are logged item by item in `data/verification_term_revisions.csv`. Apart from those 5, the remaining 274 rows are byte-identical to the source.

### Why they were changed

The source page's **own English definitions (`def_en`) already use `stem-branch` throughout** — eight occurrences:

| Entry | Usage in the source page's English definition |
|:---|:---|
| 历书 (almanac) | each annotated with the phases, the solar terms, the **stem-branch** pair… |
| 历日 (day of the calendar) | A single day as recorded in the almanac, with its date and its **stem-branch** pair. |
| 大余・小余 (major and minor remainder) | the integer part, which yields the **stem-branch** day… |
| 三伏 (the three fu periods) | It is reckoned by **stem-branch** days… |
| 社日 (community altar day) | reckoned, like the *fu*, by **stem-branch** days. |
| 干支纪日 (stem-branch day-count) | Numbering every day with a **stem-branch** pair. |
| 干支纪年 (stem-branch year-count) | Numbering the years with **stem-branch** pairs. |
| 超辰 (leap of the year station) | This "leap" is one reason the **stem-branch** count displaced it. |

**Yet the same page's `term_en` (the headword column) uses `ganzhi`** — that is, the headword column contradicts the page's own definitions. This repository aligns it to `stem-branch`, on the evidence of those definitions.

### What was changed

| Chinese | Source page `term_en` | This repository's `term_en` |
|:---|:---|:---|
| 干支 | `ganzhi / stem-branch` | **`stem-branch`** |
| 干支纪日 | `ganzhi day-count` | **`stem-branch day-count`** |
| 干支纪年 | `ganzhi year-count` | **`stem-branch year-count`** |
| 六十甲子 | `the sixty-day cycle` | **`sexagenary cycle`** |
| 六十甲子纳音 | `the nayin of the sixty-day cycle` | **`the nayin of the sexagenary cycle`** |

**The division of labour between the two renderings**: `干支` denotes **two sets of signs** (the ten stems and the twelve branches, i.e. `stem-branch`); `六十甲子` denotes **one complete round formed by pairing those two sets** (i.e. `sexagenary cycle`). The source page renders `六十甲子` as `the sixty-day cycle`, where `day` is too narrow — a Jia-Zi designation counts years as well as days.

> **How the changes are implemented**: as an explicit revision table, `TERM_EN_REVISIONS`, in `code/build_glossary.py`, each entry carrying an `assert` (the old string must match exactly one row, and match what was expected); all assertions precede any disk write. **The changes are made at those 5 places and nowhere else, and each can be checked afterwards.**

### The remaining 5 two-source differences: unchanged

Another 5 terms are written differently on the source page and in a separate internal glossary (not part of this repository); **this repository keeps the source page's form**:

| Chinese | This repository (= the source page) |
|:---|:---|
| 旬 | the ten-day week |
| 岁首 | year-beginning |
| 岁星纪年 | Jupiter year-reckoning |
| 太岁纪年 | counter-Jupiter year-reckoning |
| 超辰 | the leap of the year station |

---

## VI. Rights and licence

Dataset DOI: `10.5281/zenodo.23028692` ｜ Permanent link: <https://doi.org/10.5281/zenodo.23028692>

- This dataset is released under **Creative Commons Attribution 4.0 International (CC BY 4.0)**. You are free to use, copy, modify and distribute it, including commercially, **on condition of attribution**.
- **Licence text**: the complete legal text is in [`LICENSE`](LICENSE) (the official English text of CC BY 4.0); [`NOTICE.md`](NOTICE.md) is a Chinese-language companion with the attribution format this repository requests.
- **Copyright status must be seen in two layers, which should not be conflated**:
  - **The terminology correspondences** (Chinese name to fixed English rendering, and the correspondence with Termonline) are of the nature of a **general table of data / general table**. Under **Article 5** of the *Copyright Law of the People's Republic of China*, such content is outside the scope of that law.
  - **The definitions (`def_zh` / `def_en`) are the author's original wording** and do not fall within the Article 5 exemption; they are protected by copyright. This repository licenses them under **CC BY 4.0** — freely usable with attribution.
- CC BY-SA was not chosen: its "share-alike" clause propagates to users and in fact reduces willingness to adopt.

**Attribution format (please cite as follows)**:

> Chujia Kuang (邝楚嘉). Chinese Calendrical & Uranographical Glossary (Chinese–English) [Dataset]. Zenodo. 2026. v1.0.1. CC BY 4.0. DOI: 10.5281/zenodo.23028692

---

## VII. Scope limits (please read alongside)

1. **The English renderings are working renderings, not the only correct answer.** Several of them have other established usages in the field (for example 五行 is given as `the five phases` rather than `the five elements`, a choice made in the history-of-science line). **The value of this table lies in being "consistent throughout and translatable back"**, and it claims no exclusivity.
2. **A definition is a one-sentence delimitation and does not develop the evidence.** Each aims only to mark out what is denoted; for the detailed documentary basis and discussion, see the companion preprints and the articles on the site.
3. **`tag_zh` is the source page's classification tag, which is not the same scheme as `group_zh`.** Groups follow the page's 19 H3 headings; classification tags follow the 6 first-level classes and 25 second-level subclasses. The two **form separate systems** and should not be applied to one another.
4. **The G2 classification table contains one source-page defect** (the repeated count in the "术数择日" row), stated in section III.
5. **Appendix 1's three-source comparison is a "comparison of what the documents record", not a "conclusion on the determinative stars".** This repository reproduces the three records together with the star in current use and **does not judge between them**.
6. **This repository contains no judgement, verdict, auspiciousness or inauspiciousness, and no reference to any individual.** Group XIX, "Divination and day-selection", collects the **term names and their definitions** (what "择日", "神煞" and the like denote), and **contains no day-selection method, no verdict on fortune, and no instruction for use**.

---

## VIII. Re-computation and regeneration

Three scripts under `code/` (Python 3, **standard library only**, no third-party package required):

| Script | Role |
|:---|:---|
| `code/fetch_source.py` | Fetches the source-page HTML into `_source/`, recording byte count and md5 |
| `code/build_glossary.py` | Parses the source pages → generates every file under `data/` |
| `code/verify_glossary.py` | **Independent verification** (criteria not sharing a source with the generator), 24 checks |

```bash
python code/fetch_source.py --out _source
python code/build_glossary.py --src-dir _source --out data
python code/verify_glossary.py
```

### The generator's three rules

1. **All assertions precede the disk write.** If the group count or the row count differs, or a field is empty, it stops — no half-finished output is left behind.
2. **Every number comes from measurement.** Counted with `len()`, not hard-coded and not copied from documentation.
3. **CSV files are uniformly UTF-8 with BOM and CRLF**, matching the specification of the existing files in the sibling repository `chinese-calendar-dataset`.

**Idempotence**: running the same source page twice leaves every file under `data/` with an identical md5.

### The verifier's criteria do not share a source with the generator

`verify_glossary.py` **does not import the generator**; instead it recounts from two places — the products and the source-page HTML — and compares. The generator saying "I wrote it correctly" does not count. It also self-checks three hard constraints: no URLs inside the data files, compliant CSV encoding and line endings, and no leftover placeholders.

**This run's result: OK 24 ｜ WARN 2 ｜ FAIL 0** (the two WARNs are the two faces of the source-page defect of section III).

### When the source page was revised

The source page carries, in plain text at the head, "修订时间：**2026年9月26日**" (revision time: 26 September 2026); the page's own JSON-LD records `datePublished` 2026-09-23 and `dateModified` 2026-09-26. The md5 of both pages is recorded in `data/source_manifest.json`, for determining which version of the source page this data corresponds to.

---

## IX. Relation to the sibling dataset

| Repository | Content | Relation |
|:---|:---|:---|
| **This repository**, `chinese-calendar-glossary` | **Terms** (279, Chinese–English) | the conceptual layer |
| `chinese-calendar-dataset` | **Computed data** (A1 solar-term instants 3,672 rows ／ A2 historical calendar chronology 52 calendars ／ A3 sexagenary day table 55,883 days) | the numeric layer |

The two are **companions, each standing as its own repository**: this one says what a word denotes, the sibling says what a number is. When citing, please cite them separately as needed.

---

## X. Revision history

| Date | Version | Notes |
|:---|:---|:---|
| 2026-09-29 | 1.0.0 | First release: 279 terms / 19 groups / 25 second-level subclasses; Chinese–English item-by-item parity 279/279 (0 mismatches); Termonline correspondence 147 same name / 21 close name / 111 not recorded; appendices giving the determinative stars of the twenty-eight mansions across three sources (28 rows) and star officers and star counts (28 rows); plus a schema.org `DefinedTermSet` semantic file. Zenodo DOI 10.5281/zenodo.23028692. Source page revised 2026-09-26. The repeated count in the classification table's "术数择日" row is stated as it stands (28 in table / 14 measured), with a table comparing what the source page states against what was measured. **Five English renderings were revised** (干支 → stem-branch, 六十甲子 → sexagenary cycle, etc.), unifying them on the evidence of the source page's own English definitions, which already used stem-branch; logged item by item in verification_term_revisions.csv. Generation, verification and licence all in place; the verifier is independent of the generator, OK 24 / WARN 2 / FAIL 0. |
| 2026-09-29 | 1.0.1 | **Correction of the published DOI convention.** v1.0.0's README and CITATION.cff published the **version-level record number** (not the concept number; per house rule the number is not repeated in this README), which contradicted §1 of the *Overseas Publication Rules · 2026-09-20* — "one concept DOI per collection, and that alone is published" — since a version number stops at the old version (a chain that lags behind). This version moves uniformly to the **concept DOI** `10.5281/zenodo.23028692` (collection-level, permanently pointing to the latest version), with version numbers kept to git commit messages only. `README_AI_AGENT.md` gained a line for the concept DOI, matching the sibling repository's style. The verifier gained a seventh group of criteria, "published DOI convention", with 2 items, so the count rose from 24 to 26; the `.zenodo.json` description, which still recorded OK 17 / WARN 1 (an old value from an early round), was corrected to this version's measured values. **Not one data file was touched**: 279 rows / 19 groups / two appendices of 28 × 2 are identical to v1.0.0. Verification OK 26 / WARN 2 / FAIL 0. |

---

*This is the English edition of the repository README. Where the two editions differ, the Chinese edition [`README.md`](README.md) governs the repository description; both carry the same tables, row for row.*
