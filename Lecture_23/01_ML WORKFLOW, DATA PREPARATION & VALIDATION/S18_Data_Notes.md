# Building a Trustworthy Housing-Price Baseline: data notes

## The prediction question

Estimate a property's eventual recorded `price` from attributes that could be known **before that price is known**. One row is one recorded observation for this educational exercise. Treating the original records as separate, comparable, cross-sectional examples is an assumption for practice, not a fact established by the source. The values are for learning a sound data and evaluation workflow; they do not establish a deployable appraisal system.

Use `S18_Housing_Workflow.csv` for the exercise. It has 553 rows and 15 columns: 545 source observations, eight exact teaching copies, the 13 original columns, and two added teaching columns. The supplied `Housing.csv` had no blank cells or exact duplicate rows. **The missing values, inconsistent inputs, nonpositive areas and duplicate copies in this file were intentionally introduced for teaching**; they are not evidence of defects in a real business system. Every original `price` remains with its original observation.

## Column dictionary

"Recorded" describes what the source table calls a value, without claiming a verified measurement method. Blank cells occur only in selected adapted feature fields. Original category terms are retained except for a few introduced input variants.

| Column | Role and interpretation | Values and quality notes |
|---|---|---|
| `price` | Target: recorded outcome to estimate. | Positive numbers in **price units**; currency is unknown. No introduced blanks or edits. Never an input feature. |
| `area` | Eligible numerical feature: recorded property area. | **Recorded area units** are unknown. Some adapted cells are blank, have a grouped numeric token, or are nonpositive and therefore invalid. An unusually large positive area is not automatically an error. |
| `bedrooms` | Eligible numerical feature: recorded bedroom count. | Original values are whole numbers from 1 to 6; no introduced defects. A new input with zero or invalid bedrooms must be handled safely before forming a ratio. |
| `bathrooms` | Eligible numerical feature: recorded bathroom count. | Original values are whole numbers from 1 to 4. Some adapted cells are blank or carry a number with a clear text suffix. |
| `stories` | Eligible numerical feature: recorded number of stories. | Original values are whole numbers from 1 to 4; no introduced defects. |
| `parking` | Eligible numerical feature: recorded parking-space count. | Original values are whole numbers from 0 to 3. **Zero is valid**, not a missing-value code. |
| `mainroad` | Eligible categorical feature: source flag for a main-road association; its precise criterion is undocumented. | Source terms `yes` / `no`. Some adapted cells are blank or have case/outer-space variants. |
| `guestroom` | Eligible categorical feature: source flag for a guest room. | Source terms `yes` / `no`; no introduced defects. |
| `basement` | Eligible categorical feature: source flag for a basement. | Source terms `yes` / `no`; no introduced defects. |
| `hotwaterheating` | Eligible categorical feature: source flag for hot-water heating. | Source terms `yes` / `no`; no introduced defects. |
| `airconditioning` | Eligible categorical feature: source flag for air conditioning. | Source terms `yes` / `no`; no introduced defects. |
| `prefarea` | Eligible categorical feature: source flag for a preferred area; the source gives no definition of preference or geography. | Source terms `yes` / `no`; no introduced defects. |
| `furnishingstatus` | Eligible categorical feature: recorded furnishing category. | Source terms `furnished`, `semi-furnished`, `unfurnished`. Some adapted cells are blank or have case, spacing or spelling variants. |
| `record_id` | Added audit identifier for one original source row and any teaching copy of it. | `H0001`–`H0545`; eight IDs appear twice. Use for duplicate and partition checks only. It is **not** verified property identity or a predictor. |
| `price_per_area_at_sale` | Added **forbidden leakage illustration**: original `price` divided by original valid `area`, rounded to six decimal places. | Price units per recorded area unit. Calculated before any area defect was introduced; it can remain populated when the visible `area` is blank or invalid. It requires the outcome and would be unavailable at the prediction moment. Never put it in the feature matrix. |

The twelve eligible **raw** prediction inputs are `area`, `bedrooms`, `bathrooms`, `stories`, `parking`, `mainroad`, `guestroom`, `basement`, `hotwaterheating`, `airconditioning`, `prefarea` and `furnishingstatus`. A fresh prediction row needs only these twelve columns. It does not need `price`, `record_id`, `price_per_area_at_sale` or a precomputed ratio.

`area_per_bedroom` is a legitimate candidate **derived later**, because it uses inputs that could be available before the outcome. It is deliberately absent from the CSV. Calculate it from cleaned `area` and `bedrooms` in the same repeated feature-preparation path used for training, validation and future rows. If either input is missing/invalid or bedrooms is zero, the ratio should be missing rather than infinite or fabricated; a training-fitted numerical imputer can then handle it. Do not precompute it on the entire table and pass a special column into prediction.

## Reading and preparing the imperfect inputs

First inspect the columns, row count, target completeness, blank cells, raw value types/categories and repeated `record_id` values. Check that repeated IDs have identical rows before retaining one copy per ID. A shared teaching ID establishes deliberate copy identity; it cannot establish whether different original rows represent different real-world properties.

Distinguish these situations before choosing an action:

- A blank feature is **missing**, while a value such as a number with a thousands separator or a clear count suffix is **present but needs controlled parsing**. Accept only a documented, unambiguous format; investigate unfamiliar tokens instead of silently coercing everything or deleting the row.
- A nonpositive `area` is impossible for the intended recorded-area meaning, so treat it as invalid and then missing. A large **positive** recorded area may be unusual but plausible; investigate rather than delete it automatically. Keep `parking = 0` as a real value.
- A known case/space/spelling variant can be normalized by a fixed rule. A genuinely new category in a future input is different: it should be handled deliberately by the prediction path, not quietly relabeled as a known one.
- A missing feature need not invalidate an observed target. Do not fill a missing target and call it an observed label. Here the original target values are present.

After identity handling, protect an evaluation split **before learning** any imputation value, scaling factor, outlier threshold or model category vocabulary. The planned exercise reserves 20% as test, then uses 25% of the remaining records as validation, with shuffled `train_test_split(random_state=42)` at both steps. On 545 retained IDs, that is 327 training, 109 validation and 109 reserved test observations. Keep IDs and targets aligned and disjoint. Later data-quality decisions and fitted preparation must come from training data; the reserved test remains unused for development in this exercise. The source is sorted by descending price, which makes an unshuffled position split especially misleading. A shuffled split still cannot prove protection against unknown time, geography or shared-property effects.

Be able to explain why a column is available at prediction time, why an input is missing versus malformed versus invalid, why a rule is fixed versus learned from data, and why an apparently good validation result cannot by itself verify preprocessing. A constant baseline predicts the same value for every row, so its error does not test whether individual feature values were prepared correctly.

## Source, adaptation and use

The exact supplied `Housing.csv` is the source for this adaptation (SHA-256 `a8ef508351b4d6e87b23a831cf316a3d53c794ed9d969c7b697a865a60a3d65f`). Its original publisher, acquisition chain, collection dates, country, currency, physical area unit and right to redistribute this particular copy were **not established** by the supplied file. A [public Kaggle housing listing](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset) and [a public copy with matching field names and row count](https://github.com/reisanar/datasets/blob/master/kaggle-housing.csv) are provenance leads, not proof that either is the origin or license for these attached bytes. Checked 18 November 2026. Broader learner distribution and reuse rights remain unresolved pending source/permission review; this package is for internal review in the meantime.
