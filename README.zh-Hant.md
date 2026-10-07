# Chinese Calendrical & Uranographical Glossary（中國曆法與古天文學術語對照表·中英雙語）

**[简体中文](README.zh.md) ｜ 繁體中文 ｜ [English](README.md) ｜ [日本語](README.ja.md) ｜ [한국어](README.ko.md)**

<!-- badges -->

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23028692.svg)](https://doi.org/10.5281/zenodo.23028692) [![Data: CC BY 4.0](https://img.shields.io/badge/Data-CC%20BY%204.0-lightgrey.svg)](LICENSE) [![ORCID](https://img.shields.io/badge/ORCID-0009--0002--7650--833X-a6ce39.svg)](https://orcid.org/0009-0002-7650-833X) [![OpenAlex](https://img.shields.io/badge/OpenAlex-A5151908354-ff6f00.svg)](https://openalex.org/A5151908354) [![Site](https://img.shields.io/badge/site-kuangchujia.com-blue.svg)](https://kuangchujia.com)

> **一套中英雙語對照的中國曆法與古天文學術語表，可下載、可引用、可核驗。**
> **279 條術語**，分 19 組；每條給**中文名 · 英文定譯 · 中文釋義 · 英文釋義**四項，並標出與「術語在線」（全國科學技術名詞審定委員會）的對應關係。
> 附兩張獨立對照表：**二十八宿距星三源對照**（28 行）、**二十八宿星官與星數**（28 行）。
> DOI：10.5281/zenodo.23028692 ｜ 許可 CC BY 4.0 ｜ 版本 v1.2.0
> **機器可讀版（面向 AI Agent 與 LLM 爬蟲）**：[`README_AI_AGENT.md`](README_AI_AGENT.md) —— 同一批事實的結構化聲明、字段表與自校驗清單。

*A Chinese–English glossary of calendrical and uranographical terms — downloadable, citable and checkable. 279 terms in 19 groups, each with a Chinese name, a fixed English rendering and a definition in both languages, together with its correspondence to Termonline, the terminology platform of China's National Committee for Terms in Sciences and Technologies. Two stand-alone tables are appended: the determinative stars of the twenty-eight lunar mansions across three sources (28 rows), and the star officers and star counts of the twenty-eight mansions (28 rows). DOI: 10.5281/zenodo.23028692 · CC BY 4.0 · v1.2.0. A machine-readable edition is available in `README_AI_AGENT.md`.*

<!-- ANCHOR-BLOCK-BEGIN -->
## ★ 本項目在學術網絡中的位置

> **Academic Lineage & Linked Identity（學術脈絡與關聯身份）**

| 項 | 地址 |
|:---|:---|
| **作者（Creator / Author）** | 鄺楚嘉（Chujia Kuang / 嘉言一得） |
| **ORCID iD** | [0009-0002-7650-833X](https://orcid.org/0009-0002-7650-833X) |
| **OpenAlex Index** | [A5151908354](https://openalex.org/A5151908354) |
| **個人主頁 / 全部成果總入口（Verification Hub）** | <https://kuangchujia.com> |
| **本倉庫** | <https://github.com/Kuangchujia/chinese-calendar-glossary> |
| **本數據集 DOI（Zenodo）** | [10.5281/zenodo.23028692](https://doi.org/10.5281/zenodo.23028692) |
| **OSF 項目（開放研究鏡像）** | <https://osf.io/3wvkh/> |
| **配套數據集（曆法三件套）** | <https://github.com/Kuangchujia/chinese-calendar-dataset> |
| **配套預印本鏡像倉庫** | <https://github.com/Kuangchujia/kuangchujia-preprints> |

**本倉庫是什麼**：一份**術語對照表**——把中國曆法與古天文學中一批繞不開的詞，給出中文名、英文定譯與兩語釋義，並逐條標出與國家級術語庫的對應關係。**它不是曆日推算表**；節氣交節時刻、歷代曆法年表、干支紀日三類推算數據見配套倉 `chinese-calendar-dataset`。

**術語定譯的用途**：供漢學、科技史與天文史方向的中英寫作與翻譯引用；供 AI Agent 與 LLM 在讀取中文天文曆法文獻時對齊概念。**英文定譯只求「所指不錯、兩邊可回譯」**，不求文學性。
<!-- ANCHOR-BLOCK-END -->

---

## 一、這份數據裡有什麼

| # | 資產 | 文件 | 行數 | 內容 |
|:--:|:---|:---|:--:|:---|
| **G1** | **術語主表** | `data/glossary_zh_en.csv`<br>`data/glossary_zh_en.json`<br>`data/glossary_zh_en.jsonl` | **279** 條 | 中文名／英文定譯／分類標籤（中英）／中文釋義／英文釋義／術語在線對標 |
| **G2** | **分類導航表** | `data/classes.csv` | **6** 個一級分類 | 一級分類 · 二級子類及其條數 · 條數 |
| **G3** | **附錄一·二十八宿距星** | `data/appendix_1.csv` | **28** 行 | 四方／宿／唐《開元占經》卷一百六／元《宋史·天文志》／明清以來（今通用） |
| **G4** | **附錄二·二十八宿星官與星數** | `data/appendix_2.csv` | **28** 行 | 四方／宿／星官數／星數 |
| **G5** | **語義件** | `data/glossary_term_set.jsonld` | **279** 詞條 | schema.org `DefinedTermSet`，供知識圖譜與檢索器直接消費 |

同目錄另有三件**核驗件**（不是數據本身，供覆核用）：

| 文件 | 作用 |
|:---|:---|
| `data/verification_parity.csv` | 中文頁與英文頁**逐條對拍**結果（279 行） |
| `data/verification_term_revisions.csv` | 本倉對源頁英文兩列的 **29 處修訂**（含**列**／修訂前／後／依據） |
| `data/verification_classes.csv` | 分類導航表**表載條數 vs 實測條數**逐項對拍 |
| `data/verification_stated_vs_measured.csv` | 源頁**自述**（導讀／腳註）與實測對拍 |
| `data/source_manifest.json` | 源頁文件、字節數、md5、**修訂時間**、發佈／修改時點、各項計數 |

### 五語版（2026-10-07 增）

五種語言（簡／繁／英／日／韓）的對照件與原文件並存，**原文件一字未動**：

`data/glossary_multi5.csv` · `.json` · `.jsonl` —— **279** 行 × **26** 列，全表展開為五語
`data/classes_multi5.csv`（**6** 行）· `data/appendix_1_multi5.csv`（**28** 行）· `data/appendix_2_multi5.csv`（**28** 行）· `data/glossary_term_set_multi5.jsonld`（**279** 詞條）

範圍上有兩點要說明。`appendix_1_multi5.csv` 的兩列引文（唐《開元占經》卷一百六、元《宋史·天文志》）是**古籍原文照錄，不作翻譯**——譯了就不是原文。上面五件核驗件則是**覆核記錄**，逐字引用源頁（字節數、md5、修訂前後），故保持源語言。

---

## 二、G1 · 術語主表

### 字段

| 字段 | 說明 |
|:---|:---|
| `id` | 序號，1–279，按源頁順序 |
| `group_id` | 組號，1–19 |
| `group_zh` / `group_en` | 所屬組名（中／英） |
| `term_zh` | 中文術語名 |
| `term_en` | 英文定譯 |
| `tag_zh` / `tag_en` | 分類標籤，形如「曆法術語 · 總論」／`Calendrical terms · general` |
| `def_zh` | 中文釋義（一句話） |
| `def_en` | 英文釋義（一句話） |
| `termonline_status` | 與術語在線的對應關係：`exact`（同名）／`near`（近名）／`none`（未收） |
| `termonline_term` | 術語在線所收的詞條名（`near` 與 `exact` 才有） |
| `termonline_subject_zh` / `_en` | 術語在線該詞條的學科歸屬（中／英） |

### 分組與條數

| 組 | 組名 | 條數 |
|:--:|:---|:--:|
| 1 | 一 · 曆法・曆算 | 20 |
| 2 | 二 · 歲首・月建・置閏 | 16 |
| 3 | 三 · 節氣・物候 | 17 |
| 4 | 四 · 紀日・紀年・時刻 | 22 |
| 5 | 五 · 朔望・月相・交食 | 17 |
| 6 | 六 · 星空・座標・測量 | 25 |
| 7 | 七 · 儀器・星官・星圖 | 13 |
| 8 | 八 · 曆法沿革・行用 | 14 |
| 9 | 九 · 五星・行星天象 | 13 |
| 10 | 十 · 三垣・拱極星區 | 8 |
| 11 | 十一 · 四象・二十八宿 | 32 |
| 12 | 十二 · 星名・星表・天河・宇宙論 | 9 |
| 13 | 十三 · 月相（今名） | 9 |
| 14 | 十四 · 年月週期與時制（今用） | 15 |
| 15 | 十五 · 十二時稱 | 12 |
| 16 | 十六 · 座標與中天（今用） | 9 |
| 17 | 十七 · 特殊天象 | 7 |
| 18 | 十八 · 儀象器用（補） | 7 |
| 19 | 十九 · 術數擇日 | 14 |
| | **合計** | **279** |

### 與「術語在線」的對應

第四列（`termonline_*`）給出與 [術語在線](https://www.termonline.cn/)（全國科學技術名詞審定委員會）的對應關係。**判據**：只在該庫收有詞條、且學科屬**天文學**類時方才標出；若該庫收的是**不同名**的詞條，則記為 `near` 並在 `termonline_term` 裡給出那個詞。

| 對應狀態 | 條數 |
|:---|--:|
| `exact` 同名 | **147** |
| `near` 近名 | **21** |
| `none` 未收 | **111** |
| **合計** | **279** |

> **⚠ 英文兩列不是源頁的逐字照錄**：其中 **24 條**已作修訂（見第五節），其餘 **255 條**與源頁逐字相同。`def_zh` / `tag_*` / `termonline_*` **一律照錄，未作任何改動**；`term_en` 與源頁自身的英文釋義（`def_en`）兩列則按第五節所述作了修訂。

> **數據件內不放網址**（本倉既定硬線）。`termonline_term` 只存**詞條名**，學科只存**文字**；術語在線的檢索入口為 <https://www.termonline.cn/>，按詞條名檢索即可。此取捨可一句話改：若需在數據件內直存 URL，改 `code/build_glossary.py` 中 `parse_termonline()` 的返回即可。

---

## 三、G2–G4 · 分類表與兩張附錄

### G2 分類導航表 —— 一處必須如實說明的源頁缺陷

`classes.csv` **照錄源頁**分類導航表。核對時發現：**6 個一級分類中有 5 個的「條數」與正文實測逐項相符，唯「術數擇日」一行不符**。

| 一級分類 | 表載條數 | 實測條數 | 差 |
|:---|--:|--:|--:|
| 天文基礎 | 90 | 90 | 0 |
| 曆法術語 | 56 | 56 | 0 |
| 天象類 | 36 | 36 | 0 |
| 星宿與星官 | 50 | 50 | 0 |
| 律曆制度 | 33 | 33 | 0 |
| **術數擇日** | **28** | **14** | **+14** |

**成因**：該行的二級子類欄把**同一批子類重複列了一遍**——「擇日 5、神煞 8、納音 1、（＊）擇日 5、神煞＊ 8、納音＊ 1」。帶 ＊ 與不帶 ＊ 所指相同，故 28 ＝ 14 × 2。其餘五行無此重複。

**哪一個是準的**：**279**。四條獨立證據——
1. **正文實際數據行數**：`<table class="terms">` 內的數據行，中英兩頁各自重數，**均為 279**；
2. **按分類標籤逐條歸類**：6 個一級分類實測合計 **279**；
3. **源頁腳註自稱「二十五個二級子類」**，實測二級子類恰為 **25** 個，**合計 279** —— 與 293 不相容；
4. **源頁導讀自稱「共 279 條，分十九組」** —— 站方自己寫的數就是 279。

本倉**未改源頁**（站點改動默認只報不改）。`verification_classes.csv` 與 `verification_stated_vs_measured.csv` 把兩種數並列留檔，**不給結論性的「正確值」**——使用者可自行判斷。源頁若日後更正，重跑生成器即可。

### G3 附錄一 · 二十八宿距星三源對照

28 行，每行一宿，列出**三個歷史來源對「該宿距星是哪一顆」的不同記載**，並給出今通用的對應星。

| 四方 | 宿 | 唐《開元占經》卷一百六 | 元《宋史·天文志》 | 明清以來（今通用） |
|:---|:---|:---|:---|:---|
| 東方蒼龍 | 角宿 | 左角星 | 南星 | 角宿一（室女座 α） |

> 「四方」列在原表中為合併單元格，本倉已**逐行補齊**（同一方的各行都寫上方位名），便於程序處理。原表「未記」二字照錄。

### G4 附錄二 · 二十八宿星官與星數

28 行，每行一宿，給該宿的**星官數與星數**（如角宿：星官 11、星 45）。

---

## 四、中英對表

源頁自稱「條目與英文頁逐條對應，兩邊都不缺項」。本倉**逐條實測**：

| 指標 | 結果 |
|:---|:---|
| 中文頁條數 | **279** |
| 英文頁條數 | **279** |
| 組數 | **19 / 19** |
| 逐條 `term_zh` + `term_en` 完全一致 | **279 / 279** |
| **不一致** | **0** |

對拍明細見 `data/verification_parity.csv`。判定方式為**按序逐條比對**（不做模糊匹配、不做名稱歸一），任一條的「中文名或英文名」有出入即記「不一致」。

---

## 五、英文定譯：依李約瑟／席文規範，對源頁的 29 處修訂

**必須先說清楚**：本倉 G1 的英文兩列**不是源頁的逐字照錄**，而是作了 **29 處修訂**——`term_en` **6 處**、`def_en` **23 處**，共落在 **24 條**條目上。修訂之處逐條留檔於 `data/verification_term_revisions.csv`（含「列」一欄）。除這 24 條，其餘 **255 條**與源頁逐字相同。

### 依據（2026-10-07 立）

核心術語依**李約瑟（Joseph Needham）／席文（Nathan Sivin）西方科技史規範**。兩條為硬性：

| 中文 | 規範英譯 | 不予採用 |
|:---|:---|:---|
| 干支 | **`Sexagenary Cycle`** | 羅馬字 `ganzhi`、字面直譯 `stem-branch`、`Heavenly Stems and Earthly Branches` |
| 歲差 | **`Precession of the Equinoxes`** | 單寫 `precession` |

羅馬字**不得充當術語譯名**。節氣名一律**意譯**（`Beginning of Spring`，而非其羅馬字寫法；`Awakening of Insects`，而非其羅馬字寫法）。市面命理俗譯——`BaZi`、`Four Pillars`、`Eight Characters`——一概排除；確需指涉擇日實踐時，寫 **traditional calendrical teaching materials**。

### 改了什麼

| 中文 | 列 | 源頁 | 本倉 |
|:---|:---|:---|:---|
| 干支 | `term_en` | `ganzhi / stem-branch` | **`Sexagenary Cycle`** |
| 干支紀日 | `term_en` | `ganzhi day-count` | **`Sexagenary Day-Count`** |
| 干支紀年 | `term_en` | `ganzhi year-count` | **`Sexagenary Year-Count`** |
| 六十甲子 | `term_en` | `the sixty-day cycle` | **`the Sixty Binomials of the Sexagenary Cycle`** |
| 六十甲子納音 | `term_en` | `the nayin of the sixty-day cycle` | **`the Nayin of the Sexagenary Cycle`** |
| 歲差 | `term_en` | `precession` | **`Precession of the Equinoxes`** |
| 曆書 ／ 曆日 ／ 大餘・小餘 ／ 三伏 ／ 社日 ／ 干支紀日 ／ 干支紀年 ／ 超辰 | `def_en` | 字面直譯 `stem-branch`（共 8 處） | `sexagenary binomial` ／ `sexagenary days` ／ `sexagenary count` |
| 閏月 ／ 章 | `def_en` | `the solar year and the lunar months` | `the tropical year and the synodic months` |
| 朔 ／ 晦 ／ 胐 ／ 六曜 | `def_en` | `a lunar month` | `a calendrical month` |
| 節 ／ 中氣／氣 ／ 啟蟄 | `def_en` | 節氣名的羅馬字寫法 | `Beginning of Spring`、`Awakening of Insects`、`Rain Water`、`Spring Equinox` |
| 歲周 | `def_en` | `due to precession.` | `due to the precession of the equinoxes.` |
| 上元 ／ 天赦 ／ 六十甲子納音 | `def_en` | 羅馬字日名 | 威妥瑪（`chia-tzu`、`i-ch'ou`、`chia-wu`、`wu-shen`、`wu-yin`） |

### 舊口徑已明文取代

首版（2026-09-29）把「干支」定為 `stem-branch`、「六十甲子」定為 `sexagenary cycle`，以範圍分工。**該分工自 2026-10-07 起被上表明文取代**——「干支」本身即 `Sexagenary Cycle`。舊句在本節與 `data/verification_term_revisions.csv` 中作為**留痕**保留；**兩者不一致時，以本節為準。**

> **改法**：在 `code/build_glossary.py` 內寫成兩張顯式修訂表——`TERM_EN_REVISIONS`（詞條列）與 `DEF_EN_REVISIONS`（釋義列），每條帶 `assert`（舊串須命中預期次數），並設回讀閘重掃兩列是否殘留舊形。**全部斷言置於寫盤之前**，改動只在這兩處、且事後可逐條複核。

### 標識符不是譯名

數據模式保留原有標識符：`ganzhi_day`、`ganzhi_index_1_60`、`solar_term_month_branch` 及其取值、`data/ganzhi_day_1900_2052.csv`、`code/gen_dataset_ganzhi.py`。它們是**契約而非譯名**——改名即打斷所有下游連接與既有引用。故本規範不動它們，文檔亦照原樣引用。

---

## 六、權利與許可

數據集 DOI：`10.5281/zenodo.23028692` ｜ 永久鏈接：<https://doi.org/10.5281/zenodo.23028692>

- 本數據集採用 **Creative Commons Attribution 4.0 International（CC BY 4.0）**。可自由使用、複製、修改、分發，含商業用途，**條件是署名**。
- **許可文本**：完整法律文本見 [`LICENSE`](LICENSE)（CC BY 4.0 官方英文全文）；[`NOTICE.md`](NOTICE.md) 為中文對照說明，含本倉要求的署名格式。
- **權利狀態須分兩層看，不宜混為一談**：
  - **術語對照關係**（中文名—英文定譯、與術語在線的對應）屬**通用數表／通用表格**性質。依《中華人民共和國著作權法》**第五條**，此類內容不適用該法。
  - **釋義（`def_zh` / `def_en`）是本作者的原創表述**，不屬第五條豁免範圍，受著作權保護。本倉以 **CC BY 4.0** 授權使用——署名即可自由使用。
- 未選用 CC BY-SA：其「相同方式共享」條款會傳染給使用者，反而降低採用意願。

**署名格式（請照此引用）**：

> 鄺楚嘉（Chujia Kuang）. 中國曆法與古天文學術語對照表（中英雙語）[Dataset]. Zenodo. 2026. v1.2.0. CC BY 4.0. DOI: 10.5281/zenodo.23028692

---

## 七、使用邊界（請一併閱讀）

1. **英文定譯是「工作定譯」，不是唯一正解。** 其中若干條在學界另有通行譯法（例如「五行」取 `the five phases` 而非 `the five elements`，是科技史一系的取捨）。**本表的價值在於「一表之內前後一致、可回譯」**，不主張排他。
2. **釋義是一句話的界定，不展開考據。** 每條只求把所指劃清；詳細的文獻依據與討論，見配套預印本與站點文章。
3. **`tag_zh` 是源頁的分類標籤，與 `group_zh` 不是同一套劃分。** 組別按頁面的 19 個 H3 標題；分類標籤按 6 個一級分類、25 個二級子類。兩者**各自成系統**，勿互相套用。
4. **G2 分類表含一處源頁缺陷**（術數擇日行重複計數），已在第三節如實說明。
5. **附錄一的三源對照是「文獻記載的對照」，不是「距星考證結論」。** 本倉照錄三種記載並列出今通用對應，**不判定孰是**。
6. **本倉不含任何判斷、斷語、吉凶宜忌或個體指向。** 第十九組「術數擇日」收的是**術語名與其界定**（如「擇日」「神煞」指的是什麼），**不含任何擇日方法、吉凶結論或用法說明**。

---

## 八、復算與再生成

`code/` 下三個腳本（Python 3，**只用標準庫**，無需安裝任何第三方包）：

| 腳本 | 作用 |
|:---|:---|
| `code/fetch_source.py` | 抓取源頁 HTML 到 `_source/`，記字節數與 md5 |
| `code/build_glossary.py` | 解析源頁 → 生成 `data/` 下全部文件 |
| `code/verify_glossary.py` | **獨立校驗**（判據與生成器不同源），24 項檢查 |

```bash
python code/fetch_source.py --out _source
python code/build_glossary.py --src-dir _source --out data
python code/verify_glossary.py
```

### 生成器的三條紀律

1. **一切斷言置於寫盤之前。** 組數不等、條數不等、空字段，任一不滿足即停，不留半成品。
2. **數字全部來自實測。** `len()` 數出來的，不寫死、不照抄文檔。
3. **CSV 一律 UTF-8 BOM + CRLF**，與配套倉 `chinese-calendar-dataset` 的既有件同規格。

**冪等**：同一份源頁連跑兩次，`data/` 下逐件 md5 完全相同。

### 校驗器的判據與生成器不同源

`verify_glossary.py` **不 import 生成器**，改從「產物 + 源頁 HTML」兩處各自重新數一遍再對拍——生成器說「我寫對了」不算數。另含三條硬線自查：數據件內無網址、CSV 編碼換行合規、無佔位殘留。

**本次實測結果：OK 24 ｜ WARN 2 ｜ FAIL 0**（兩條 WARN 即第三節那處源頁缺陷的兩個側面）。

### 源頁的修訂時點

源頁頁首有純文本「修訂時間：**2026年9月26日**」；頁面自帶的 JSON-LD 記 `datePublished` 2026-09-23、`dateModified` 2026-09-26。兩頁的 md5 一併記在 `data/source_manifest.json`，用於判定本數據對應的是哪一版源頁。

---

## 九、與配套數據集的關係

| 倉 | 內容 | 關係 |
|:---|:---|:---|
| **本倉** `chinese-calendar-glossary` | **術語**（279 條，中英雙語） | 概念層 |
| `chinese-calendar-dataset` | **推算數據**（A1 節氣交節時刻 3,672 條 ／ A2 歷代曆法年表 52 部 ／ A3 干支紀日 55,883 天） | 數值層 |

兩者**互為配套、各自獨立成倉**：本倉給「詞指什麼」，配套倉給「數是多少」。引用時請按需分別註明。

---

## 十、修訂記錄

| 日期 | 版本 | 說明 |
|:---|:---|:---|
| 2026-09-29 | 1.0.0 | 首次發佈：術語 279 條 / 19 組 / 25 個二級子類；中英逐條對表 279/279 一致（0 不符）；與術語在線對標 147 同名 / 21 近名 / 111 未收；附二十八宿距星三源對照 28 行、星官與星數 28 行；另出 schema.org `DefinedTermSet` 語義件。Zenodo DOI 10.5281/zenodo.23028692。源頁修訂時間 2026-09-26。分類表「術數擇日」行源頁重複計數已如實標註（表載 28 / 實測 14），並附源頁自述與實測對拍表。**英文定譯另作 5 處修訂**（干支→stem-branch、六十甲子→sexagenary cycle 等），依源頁自身英文釋義本就用 stem-branch 這一內部不一致而統一，逐條留檔於 verification_term_revisions.csv。生成、校驗、許可三件齊備；校驗器獨立於生成器，OK 24 / WARN 2 / FAIL 0。 |
| 2026-09-29 | 1.0.1 | **對外 DOI 口徑修正**。v1.0.0 的 README／CITATION.cff 對外公佈的是**版本級記錄號**（非概念號；依家規不復寫於本 README），與《海外發布規則·2026-09-20》§一「每合集一個概念 DOI，對外只公佈這一個」相抵——版本號會停在舊版（鏈式追尾）。本版統一改為**概念 DOI** `10.5281/zenodo.23028692`（合集級，永久指向最新版），版本號只進 git commit 信息。`README_AI_AGENT.md` 補概念 DOI 一行，對齊配套倉體例。校驗器增第七組判據「對外 DOI 口徑」2 項，故計數由 24 項升至 26 項；`.zenodo.json` 描述內原記 OK 17 / WARN 1（早期一輪舊值），一併訂正為本版實測值。**數據件一字未動**：279 條 / 19 組 / 兩附錄 28×2 與 v1.0.0 完全相同。校驗 OK 26 / WARN 2 / FAIL 0。 |
| 2026-10-07 | 1.1.0 | 五語版：README 出 **簡體中文／繁體中文／English／日本語／한국어** 五語，各件題頭置語言切換行。`README.md` 為英文主版、`README.zh.md` 為中文治理版；新增 `README.zh-Hant.md`／`README.ja.md`／`README.ko.md`。**數據件、DOI、許可均未變。** |
| 2026-10-07 | 1.2.0 | **英譯改依李約瑟／席文規範重定。** `term_en` 6 處、`def_en` 23 處（共 29 處），逐條留檔於 `data/verification_term_revisions.csv`（含「列」一欄）：干支 → **Sexagenary Cycle**（v1.0.0 的 `stem-branch` 口徑**已明文取代**）、歲差 → **Precession of the Equinoxes**、六十甲子 → the Sixty Binomials of the Sexagenary Cycle；節氣名由羅馬字改寫改為意譯；市面命理俗譯（`BaZi`、`Four Pillars`、`Eight Characters`）移除；`the solar year and the lunar months` → `the tropical year and the synodic months`；`a lunar month` → `a calendrical month`；正文中的羅馬字日名改用威妥瑪。**全部改動置於 `code/build_glossary.py` 的斷言式修訂表之後，並設回讀閘；JSON 鍵名與文件名一律未動**（標識符是契約，不是譯名）。韓語列按同一規範，在每件首次出現處加**韓文（漢字）並記**（如 `간지(干支)`）。DOI 與許可未變。 |
