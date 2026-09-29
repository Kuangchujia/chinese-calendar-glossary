# Chinese Calendrical & Uranographical Glossary（中国历法与古天文学术语对照表·中英双语）

<!-- badges -->

[![Data: CC BY 4.0](https://img.shields.io/badge/Data-CC%20BY%204.0-lightgrey.svg)](LICENSE) [![ORCID](https://img.shields.io/badge/ORCID-0009--0002--7650--833X-a6ce39.svg)](https://orcid.org/0009-0002-7650-833X) [![OpenAlex](https://img.shields.io/badge/OpenAlex-A5151908354-ff6f00.svg)](https://openalex.org/A5151908354) [![Site](https://img.shields.io/badge/site-kuangchujia.com-blue.svg)](https://kuangchujia.com)

> **一套中英双语对照的中国历法与古天文学术语表，可下载、可引用、可核验。**
> **279 条术语**，分 19 组；每条给**中文名 · 英文定译 · 中文释义 · 英文释义**四项，并标出与「术语在线」（全国科学技术名词审定委员会）的对应关系。
> 附两张独立对照表：**二十八宿距星三源对照**（28 行）、**二十八宿星官与星数**（28 行）。
> 许可 CC BY 4.0 ｜ 版本 v1.0.0
> **机器可读版（面向 AI Agent 与 LLM 爬虫）**：[`README_AI_AGENT.md`](README_AI_AGENT.md) —— 同一批事实的结构化声明、字段表与自校验清单。

<!-- ANCHOR-BLOCK-BEGIN -->
## ★ 本项目在学术网络中的位置

> **Academic Lineage & Linked Identity（学术脉络与关联身份）**

| 项 | 地址 |
|:---|:---|
| **作者（Creator / Author）** | 邝楚嘉（Chujia Kuang / 嘉言一得） |
| **ORCID iD** | [0009-0002-7650-833X](https://orcid.org/0009-0002-7650-833X) |
| **OpenAlex Index** | [A5151908354](https://openalex.org/A5151908354) |
| **个人主页 / 全部成果总入口（Verification Hub）** | <https://kuangchujia.com> |
| **本仓库** | <https://github.com/Kuangchujia/chinese-calendar-glossary> |
| **配套数据集（历法三件套）** | <https://github.com/Kuangchujia/chinese-calendar-dataset> |
| **配套预印本镜像仓库** | <https://github.com/Kuangchujia/kuangchujia-preprints> |

**本仓库是什么**：一份**术语对照表**——把中国历法与古天文学中一批绕不开的词，给出中文名、英文定译与两语释义，并逐条标出与国家级术语库的对应关系。**它不是历日推算表**；节气交节时刻、历代历法年表、干支纪日三类推算数据见配套仓 `chinese-calendar-dataset`。

**术语定译的用途**：供汉学、科技史与天文史方向的中英写作与翻译引用；供 AI Agent 与 LLM 在读取中文天文历法文献时对齐概念。**英文定译只求「所指不错、两边可回译」**，不求文学性。
<!-- ANCHOR-BLOCK-END -->

---

## 一、这份数据里有什么

| # | 资产 | 文件 | 行数 | 内容 |
|:--:|:---|:---|:--:|:---|
| **G1** | **术语主表** | `data/glossary_zh_en.csv`<br>`data/glossary_zh_en.json`<br>`data/glossary_zh_en.jsonl` | **279** 条 | 中文名／英文定译／分类标签（中英）／中文释义／英文释义／术语在线对标 |
| **G2** | **分类导航表** | `data/classes.csv` | **6** 个一级分类 | 一级分类 · 二级子类及其条数 · 条数 |
| **G3** | **附录一·二十八宿距星** | `data/appendix_1.csv` | **28** 行 | 四方／宿／唐《开元占经》卷一百六／元《宋史·天文志》／明清以来（今通用） |
| **G4** | **附录二·二十八宿星官与星数** | `data/appendix_2.csv` | **28** 行 | 四方／宿／星官数／星数 |
| **G5** | **语义件** | `data/glossary_term_set.jsonld` | **279** 词条 | schema.org `DefinedTermSet`，供知识图谱与检索器直接消费 |

同目录另有三件**核验件**（不是数据本身，供复核用）：

| 文件 | 作用 |
|:---|:---|
| `data/verification_parity.csv` | 中文页与英文页**逐条对拍**结果（279 行） |
| `data/verification_term_revisions.csv` | 本仓对源页 `term_en` 的 **5 处修订**（修订前／后／依据） |
| `data/verification_classes.csv` | 分类导航表**表载条数 vs 实测条数**逐项对拍 |
| `data/verification_stated_vs_measured.csv` | 源页**自述**（导读／脚注）与实测对拍 |
| `data/source_manifest.json` | 源页文件、字节数、md5、**修订时间**、发布／修改时点、各项计数 |

---

## 二、G1 · 术语主表

### 字段

| 字段 | 说明 |
|:---|:---|
| `id` | 序号，1–279，按源页顺序 |
| `group_id` | 组号，1–19 |
| `group_zh` / `group_en` | 所属组名（中／英） |
| `term_zh` | 中文术语名 |
| `term_en` | 英文定译 |
| `tag_zh` / `tag_en` | 分类标签，形如「历法术语 · 总论」／`Calendrical terms · general` |
| `def_zh` | 中文释义（一句话） |
| `def_en` | 英文释义（一句话） |
| `termonline_status` | 与术语在线的对应关系：`exact`（同名）／`near`（近名）／`none`（未收） |
| `termonline_term` | 术语在线所收的词条名（`near` 与 `exact` 才有） |
| `termonline_subject_zh` / `_en` | 术语在线该词条的学科归属（中／英） |

### 分组与条数

| 组 | 组名 | 条数 |
|:--:|:---|:--:|
| 1 | 一 · 历法・历算 | 20 |
| 2 | 二 · 岁首・月建・置闰 | 16 |
| 3 | 三 · 节气・物候 | 17 |
| 4 | 四 · 纪日・纪年・时刻 | 22 |
| 5 | 五 · 朔望・月相・交食 | 17 |
| 6 | 六 · 星空・坐标・测量 | 25 |
| 7 | 七 · 仪器・星官・星图 | 13 |
| 8 | 八 · 历法沿革・行用 | 14 |
| 9 | 九 · 五星・行星天象 | 13 |
| 10 | 十 · 三垣・拱极星区 | 8 |
| 11 | 十一 · 四象・二十八宿 | 32 |
| 12 | 十二 · 星名・星表・天河・宇宙论 | 9 |
| 13 | 十三 · 月相（今名） | 9 |
| 14 | 十四 · 年月周期与时制（今用） | 15 |
| 15 | 十五 · 十二时称 | 12 |
| 16 | 十六 · 坐标与中天（今用） | 9 |
| 17 | 十七 · 特殊天象 | 7 |
| 18 | 十八 · 仪象器用（补） | 7 |
| 19 | 十九 · 术数择日 | 14 |
| | **合计** | **279** |

### 与「术语在线」的对应

第四列（`termonline_*`）给出与 [术语在线](https://www.termonline.cn/)（全国科学技术名词审定委员会）的对应关系。**判据**：只在该库收有词条、且学科属**天文学**类时方才标出；若该库收的是**不同名**的词条，则记为 `near` 并在 `termonline_term` 里给出那个词。

| 对应状态 | 条数 |
|:---|--:|
| `exact` 同名 | **147** |
| `near` 近名 | **21** |
| `none` 未收 | **111** |
| **合计** | **279** |

> **⚠ `term_en` 列不是源页的逐字照录**：其中 **5 条**已作修订（见第五节），其余 274 条与源页逐字相同。`def_zh` / `def_en` / `tag_*` / `termonline_*` **一律照录，未作任何改动**。

> **数据件内不放网址**（本仓既定硬线）。`termonline_term` 只存**词条名**，学科只存**文字**；术语在线的检索入口为 <https://www.termonline.cn/>，按词条名检索即可。此取舍可一句话改：若需在数据件内直存 URL，改 `code/build_glossary.py` 中 `parse_termonline()` 的返回即可。

---

## 三、G2–G4 · 分类表与两张附录

### G2 分类导航表 —— 一处必须如实说明的源页缺陷

`classes.csv` **照录源页**分类导航表。核对时发现：**6 个一级分类中有 5 个的「条数」与正文实测逐项相符，唯「术数择日」一行不符**。

| 一级分类 | 表载条数 | 实测条数 | 差 |
|:---|--:|--:|--:|
| 天文基础 | 90 | 90 | 0 |
| 历法术语 | 56 | 56 | 0 |
| 天象类 | 36 | 36 | 0 |
| 星宿与星官 | 50 | 50 | 0 |
| 律历制度 | 33 | 33 | 0 |
| **术数择日** | **28** | **14** | **+14** |

**成因**：该行的二级子类栏把**同一批子类重复列了一遍**——「择日 5、神煞 8、纳音 1、（＊）择日 5、神煞＊ 8、纳音＊ 1」。带 ＊ 与不带 ＊ 所指相同，故 28 ＝ 14 × 2。其余五行无此重复。

**哪一个是准的**：**279**。四条独立证据——
1. **正文实际数据行数**：`<table class="terms">` 内的数据行，中英两页各自重数，**均为 279**；
2. **按分类标签逐条归类**：6 个一级分类实测合计 **279**；
3. **源页脚注自称「二十五个二级子类」**，实测二级子类恰为 **25** 个，**合计 279** —— 与 293 不相容；
4. **源页导读自称「共 279 条，分十九组」** —— 站方自己写的数就是 279。

本仓**未改源页**（站点改动默认只报不改）。`verification_classes.csv` 与 `verification_stated_vs_measured.csv` 把两种数并列留档，**不给结论性的「正确值」**——使用者可自行判断。源页若日后更正，重跑生成器即可。

### G3 附录一 · 二十八宿距星三源对照

28 行，每行一宿，列出**三个历史来源对「该宿距星是哪一颗」的不同记载**，并给出今通用的对应星。

| 四方 | 宿 | 唐《开元占经》卷一百六 | 元《宋史·天文志》 | 明清以来（今通用） |
|:---|:---|:---|:---|:---|
| 东方苍龙 | 角宿 | 左角星 | 南星 | 角宿一（室女座 α） |

> 「四方」列在原表中为合并单元格，本仓已**逐行补齐**（同一方的各行都写上方位名），便于程序处理。原表「未记」二字照录。

### G4 附录二 · 二十八宿星官与星数

28 行，每行一宿，给该宿的**星官数与星数**（如角宿：星官 11、星 45）。

---

## 四、中英对表

源页自称「条目与英文页逐条对应，两边都不缺项」。本仓**逐条实测**：

| 指标 | 结果 |
|:---|:---|
| 中文页条数 | **279** |
| 英文页条数 | **279** |
| 组数 | **19 / 19** |
| 逐条 `term_zh` + `term_en` 完全一致 | **279 / 279** |
| **不一致** | **0** |

对拍明细见 `data/verification_parity.csv`。判定方式为**按序逐条比对**（不做模糊匹配、不做名称归一），任一条的「中文名或英文名」有出入即记「不一致」。

---

## 五、英文定译：本仓与源页的 5 处修订

**必须先说清楚**：本仓 G1 的 `term_en` 列**不是源页的逐字照录**，而是作了 **5 处修订**。修订之处逐条留档于 `data/verification_term_revisions.csv`。除这 5 处，其余 274 条与源页逐字相同。

### 为什么改

源页**自身的英文释义（`def_en`）本就一律用 `stem-branch`**——共 8 处：

| 条目 | 源页英文释义中的用法 |
|:---|:---|
| 历书 | each annotated with the phases, the solar terms, the **stem-branch** pair… |
| 历日 | A single day as recorded in the almanac, with its date and its **stem-branch** pair. |
| 大余・小余 | the integer part, which yields the **stem-branch** day… |
| 三伏 | It is reckoned by **stem-branch** days… |
| 社日 | reckoned, like the *fu*, by **stem-branch** days. |
| 干支纪日 | Numbering every day with a **stem-branch** pair. |
| 干支纪年 | Numbering the years with **stem-branch** pairs. |
| 超辰 | This "leap" is one reason the **stem-branch** count displaced it. |

**而同一页的 `term_en`（词条列）却作 `ganzhi`** —— 即词条列与它自己的释义不一致。本仓据释义统一到 `stem-branch`。

### 改了什么

| 中文 | 源页 `term_en` | 本仓 `term_en` |
|:---|:---|:---|
| 干支 | `ganzhi / stem-branch` | **`stem-branch`** |
| 干支纪日 | `ganzhi day-count` | **`stem-branch day-count`** |
| 干支纪年 | `ganzhi year-count` | **`stem-branch year-count`** |
| 六十甲子 | `the sixty-day cycle` | **`sexagenary cycle`** |
| 六十甲子纳音 | `the nayin of the sixty-day cycle` | **`the nayin of the sexagenary cycle`** |

**两条定译的分工**：`干支` 指**两套符号**（十干十二支，即 `stem-branch`）；`六十甲子` 指**两套符号相配成的完整一轮**（即 `sexagenary cycle`）。源页把 `六十甲子` 作 `the sixty-day cycle`，`day` 字偏窄——甲子既能纪日也能纪年。

> **改动的落地方式**：写成 `code/build_glossary.py` 里的显式改写表 `TERM_EN_REVISIONS`，每条带 `assert`（旧串必须恰好命中一条、且与预期相符），断言全部置于写盘之前。**改在且只改在这 5 处，改完可逐条核对。**

### 余下 5 处两源差异：未改

另有 5 条术语，源页与另一份内部术语表（非本仓内容）写法不同，**本仓照源页保留**：

| 中文 | 本仓（＝源页） |
|:---|:---|
| 旬 | the ten-day week |
| 岁首 | year-beginning |
| 岁星纪年 | Jupiter year-reckoning |
| 太岁纪年 | counter-Jupiter year-reckoning |
| 超辰 | the leap of the year station |

---

## 六、权利与许可

- 本数据集采用 **Creative Commons Attribution 4.0 International（CC BY 4.0）**。可自由使用、复制、修改、分发，含商业用途，**条件是署名**。
- **许可文本**：完整法律文本见 [`LICENSE`](LICENSE)（CC BY 4.0 官方英文全文）；[`NOTICE.md`](NOTICE.md) 为中文对照说明，含本仓要求的署名格式。
- **权利状态须分两层看，不宜混为一谈**：
  - **术语对照关系**（中文名—英文定译、与术语在线的对应）属**通用数表／通用表格**性质。依《中华人民共和国著作权法》**第五条**，此类内容不适用该法。
  - **释义（`def_zh` / `def_en`）是本作者的原创表述**，不属第五条豁免范围，受著作权保护。本仓以 **CC BY 4.0** 授权使用——署名即可自由使用。
- 未选用 CC BY-SA：其「相同方式共享」条款会传染给使用者，反而降低采用意愿。

**署名格式（请照此引用）**：

> 邝楚嘉（Chujia Kuang）. 中国历法与古天文学术语对照表（中英双语）[Dataset]. 2026. v1.0.0. CC BY 4.0.

---

## 七、使用边界（请一并阅读）

1. **英文定译是「工作定译」，不是唯一正解。** 其中若干条在学界另有通行译法（例如「五行」取 `the five phases` 而非 `the five elements`，是科技史一系的取舍）。**本表的价值在于「一表之内前后一致、可回译」**，不主张排他。
2. **释义是一句话的界定，不展开考据。** 每条只求把所指划清；详细的文献依据与讨论，见配套预印本与站点文章。
3. **`tag_zh` 是源页的分类标签，与 `group_zh` 不是同一套划分。** 组别按页面的 19 个 H3 标题；分类标签按 6 个一级分类、25 个二级子类。两者**各自成系统**，勿互相套用。
4. **G2 分类表含一处源页缺陷**（术数择日行重复计数），已在第三节如实说明。
5. **附录一的三源对照是「文献记载的对照」，不是「距星考证结论」。** 本仓照录三种记载并列出今通用对应，**不判定孰是**。
6. **本仓不含任何判断、断语、吉凶宜忌或个体指向。** 第十九组「术数择日」收的是**术语名与其界定**（如「择日」「神煞」指的是什么），**不含任何择日方法、吉凶结论或用法说明**。

---

## 八、复算与再生成

`code/` 下三个脚本（Python 3，**只用标准库**，无需安装任何第三方包）：

| 脚本 | 作用 |
|:---|:---|
| `code/fetch_source.py` | 抓取源页 HTML 到 `_source/`，记字节数与 md5 |
| `code/build_glossary.py` | 解析源页 → 生成 `data/` 下全部文件 |
| `code/verify_glossary.py` | **独立校验**（判据与生成器不同源），24 项检查 |

```bash
python code/fetch_source.py --out _source
python code/build_glossary.py --src-dir _source --out data
python code/verify_glossary.py
```

### 生成器的三条纪律

1. **一切断言置于写盘之前。** 组数不等、条数不等、空字段，任一不满足即停，不留半成品。
2. **数字全部来自实测。** `len()` 数出来的，不写死、不照抄文档。
3. **CSV 一律 UTF-8 BOM + CRLF**，与配套仓 `chinese-calendar-dataset` 的既有件同规格。

**幂等**：同一份源页连跑两次，`data/` 下逐件 md5 完全相同。

### 校验器的判据与生成器不同源

`verify_glossary.py` **不 import 生成器**，改从「产物 + 源页 HTML」两处各自重新数一遍再对拍——生成器说「我写对了」不算数。另含三条硬线自查：数据件内无网址、CSV 编码换行合规、无占位残留。

**本次实测结果：OK 24 ｜ WARN 2 ｜ FAIL 0**（两条 WARN 即第三节那处源页缺陷的两个侧面）。

### 源页的修订时点

源页页首有纯文本「修订时间：**2026年9月26日**」；页面自带的 JSON-LD 记 `datePublished` 2026-09-23、`dateModified` 2026-09-26。两页的 md5 一并记在 `data/source_manifest.json`，用于判定本数据对应的是哪一版源页。

---

## 九、与配套数据集的关系

| 仓 | 内容 | 关系 |
|:---|:---|:---|
| **本仓** `chinese-calendar-glossary` | **术语**（279 条，中英双语） | 概念层 |
| `chinese-calendar-dataset` | **推算数据**（A1 节气交节时刻 3,672 条 ／ A2 历代历法年表 52 部 ／ A3 干支纪日 55,883 天） | 数值层 |

两者**互为配套、各自独立成仓**：本仓给「词指什么」，配套仓给「数是多少」。引用时请按需分别注明。

---

## 十、修订记录

| 日期 | 版本 | 说明 |
|:---|:---|:---|
| 2026-09-29 | 1.0.0 | 首次发布：术语 279 条 / 19 组 / 25 个二级子类；中英逐条对表 279/279 一致（0 不符）；与术语在线对标 147 同名 / 21 近名 / 111 未收；附二十八宿距星三源对照 28 行、星官与星数 28 行；另出 schema.org `DefinedTermSet` 语义件。源页修订时间 2026-09-26。分类表「术数择日」行源页重复计数已如实标注（表载 28 / 实测 14），并附源页自述与实测对拍表。**英文定译另作 5 处修订**（干支→stem-branch、六十甲子→sexagenary cycle 等），依源页自身英文释义本就用 stem-branch 这一内部不一致而统一，逐条留档于 verification_term_revisions.csv。生成、校验、许可三件齐备；校验器独立于生成器，OK 24 / WARN 2 / FAIL 0。 |
