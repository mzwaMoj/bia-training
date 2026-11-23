# ML Workflow, Data Preparation & Validation — Trainer Guide

**Live session:** 180 minutes, including a protected 10-minute break  
**Teaching case:** Building a Trustworthy Housing-Price Baseline  
**Live PowerPoint:** slides 1–46; slide 47 is an after-class reference  
**Working files:** `S18_ML_Workflow_Practical.ipynb`, `S18_Housing_Workflow.csv`, `S18_Data_Notes.md`  
**Trainer reference:** `S18_ML_Workflow_Solution.ipynb`

**Session question:** How do we turn a business question and imperfect historical records into a first prediction workflow whose evaluation we can trust?

The lesson is successful when learners can say **what information is eligible at prediction time**, **what can be learned only from training data**, **how one fitted preparation path handles validation and new inputs**, and **what a constant baseline's validation MAE does—and does not—show**. The slides explain; the notebook is where learners work. Do not narrate every slide or use the slides as a substitute for practice.

## Before learners arrive

- Open the PPTX, learner notebook and `S18_Data_Notes.md`. Put `S18_Housing_Workflow.csv` beside the learner notebook, or confirm the notebook's `DATA_PATH` points to the local copy. Keep the solution notebook **trainer-only**.
- Start a Python-capable Jupyter kernel. Check the starter imports, declared feature lists, raw CSV load and supplied `clean_features` helper in a disposable copy; do not expect unfinished learner task cells to run to completion. Confirm the kernel can restart and execute cells in order.
- The provided `S18_requirements.txt` documents the tested target environment: Python **3.12.10**, NumPy **2.1.3**, SciPy **1.14.1**, pandas **2.3.3**, scikit-learn **1.7.2**, ipykernel **7.4.0**. Use a compatible existing Jupyter frontend. If packages are missing, check the active kernel/environment before installing from `python -m pip install -r S18_requirements.txt`.
- Verify a local solution checkpoint and rehearse the **30-minute pipeline block** and its transition into the median baseline. Have a clean notebook restart and the solution checkpoint ready for recovery; do not display future answer cells to learners.
- Keep the language precise: prices are in **price units** and areas in **recorded area units**. The source's currency, geography, measurement unit, collection dates, original publisher and redistribution rights have not been established. The messiness is deliberately introduced into the teaching derivative, not an observed defect in the supplied source.

## At-a-glance live route

Times are **elapsed classroom time**, already including explanation, tool switching, demonstration, learner work and debrief. Speaker-note minute estimates are local cues; keep the blocks below as the delivery clock. **ANCHOR** = explain the mechanism; **QUICK** = prompt/transition; **DEMO** = model a small step in Jupyter; **DO** = protect learner work; **DEBRIEF** = interpret evidence.

| Elapsed | Slides | Trainer action and medium | Learner evidence / time protection |
|---|---|---|---|
| **00–12** | **1–7** | Deck ANCHOR + QUICK check: description vs fixed calculation vs prediction; rows, `X`/`y`, fit/generalization; supervised numerical regression vs classification, unlabeled grouping and one brief action/reward RL contrast. | Ask what is known and unknown for each example. Keep the RL contrast short. |
| **12–25** | **8–11** | Frame the decision and prediction moment; screen the feature-availability diagram. **Leave slide 11 visible**; open notebook **Section 1** for the written contract. | About 5 minutes writing: `price` is `y`; 12 raw inputs; `record_id` and `price_per_area_at_sale` excluded. |
| **25–50** | **12–18** | Deck: split roles and four leakage routes. **Leave slide 18 visible**; DEMO one identity check, then learner notebook **Sections 2–3**. | Protect about 8 minutes for aligned identity/dedup/split work. No fitted preprocessing yet. |
| **50–75** | **19–23** | Diagnose defects, fixed vs fitted rules and training-only IQR. **Leave slide 23 visible**; use notebook **Sections 4–5**. | Roughly **9 min explanation + 8 min live inspection + 8 min learner work**. Probe the supplied helper; don't rewrite it. |
| **75–85** | **24** | **Break — 10 minutes.** | Resume with split partitions retained. No new required instruction. |
| **85–105** | **25–30** | Explain one-hot indicators, missing vs unseen, standardization vs min–max and input-only ratio. Pose slide 30 predictions **before** inspecting fitted output. | Learners reason about `area_per_bedroom`, the forbidden price ratio and new categories. Keep the second scaling calculation brief. |
| **105–135** | **31–36** | **About 7 min** fit/API + flow on slides 31–32; **9 min** DEMO on slide 33/Jupyter; **14 min protected DO** on notebook **Section 6** with **slide 34 left visible**. Integrate slides 35–36 as quick checkpoint/debrief during the transition. | A complete fitted mixed-data pipeline, unchanged fitted settings on validation, interpretable matrix width. Do **not** spend extra minutes after this block reciting outputs. |
| **135–155** | **37–41** | **About 6 min** reference/MAE explanation, **6 min** DEMO, **8 min DO** in notebook **Section 7** with **slide 39 visible**. Integrate slides 40–41 into the result check. | Validation-only median MAE, plain-language interpretation and synthetic feature-only row. |
| **155–170** | **42–43** | **Show slide 42, NOT 43.** Protect about **10 min independent DO** in notebook **Section 8**, then reveal **slide 43** for about **5 min DEBRIEF**. | Independently fitted mean reference, same validation rows, fair lower-MAE comparison. **Never reveal mean results before the attempt.** |
| **170–180** | **44–46** | Slide 44: conceptual three-fold CV (about 5 min); slides 45–46: exit check and bridge (about 5 min). | Entire pipeline refits within each development fold; reserved test is outside. No CV code or regression estimator today. |

## Practical checkpoints at the switch points

**1. Predictive contract → notebook Section 1 (slide 11).** Ask: “Could this field exist before the eventual price is known?” A valid answer identifies the prediction moment, `price` as the target and **12 declared eligible raw features**. `price_per_area_at_sale` requires the target and leaks it; `record_id` is only a teaching audit ID, not property identity. If unsure, have learners sort three fields into **available input / target / audit or leakage**, then rewrite one sentence.

**2. Identity and independent evidence → Sections 2–3 (slide 18).** The teaching file has **553 × 15** entries/columns. Verify the eight repeated-`record_id` pairs are **identical full records** before retaining **545**; then `X` is **545 × 12** with aligned `y` and IDs. `train_test_split` with `shuffle=True, random_state=42`, reserving **20% test first** and **25% of the remaining rows for validation**, yields **327 train / 109 validation / 109 untouched test**. Check indexes and zero ID overlap. If copies conflict, **stop and investigate**, not blind `drop_duplicates` or arbitrary selection. If `X` and `y` are misaligned, repeat the split **together** with IDs in each call—not separately with independent selections.

**3. Judge training inputs → Sections 4–5 (slide 23).** Ask for *diagnosis before repair*: blank `area` is missing; `"5,400"` and `"2 baths"` need controlled parsing; `" YES "` is a known category variant; nonpositive `area` is invalid → missing; `parking=0` is valid; a large positive area is **investigate, not automatically delete**. The supplied `clean_features` parses and derives `area_per_bedroom`; learners read/probe it rather than author a new parser. A zero bedroom count must produce a **missing**, not infinite, ratio; `"about 4000"` must raise a clear error. The **training-only** area IQR upper flag is **10,612.5 recorded area units**, with **7 flagged rows**, largest valid **16,200**. Do not delete rows to improve a future score.

**4. Construct and inspect → Section 6 (slides 33–36).** Start by tracing **12 raw columns → fixed `clean` → `columns` → `baseline`**. The supplied `numeric_pipe` is median imputation then `StandardScaler`; learners build the categorical **most-frequent imputer → `OneHotEncoder(handle_unknown="ignore", sparse_output=False)`**, route the **six** numerical columns (including `area_per_bedroom`) and **seven** categorical columns through `ColumnTransformer(remainder="drop")`, then fit the complete pipeline on training rows. After a genuine build attempt, inspect **327 × 21** train and **109 × 21** validation matrices, finite values, identical feature names and unchanged fitted state after validation transform. Useful anchors: area median **4,500**, ratio median about **1,673.33**, `mainroad` mode **yes**, furnishing mode **semi-furnished**. A constant baseline's MAE cannot validate feature usefulness; inspect preparation separately.

**5. Establish and interpret → Section 7 (slides 39–41).** `DummyRegressor(strategy="median")` learns the **4,305,000.00 price-unit** training-target median and predicts it for every property. Validation MAE is **1,301,903.67 price units** on **109 validation rows**; it is an average absolute miss, **not an accuracy percentage**. A new synthetic row with exactly the 12 raw inputs, blank `area` and new `furnishingstatus="part-furnished"` goes through the *same* fitted pipeline. Its furnishing block is **[0, 0, 0]**; its median prediction is still **4,305,000**. This shows the new-row path functions, not that the model understands the category or values individual properties.

**6. Independent comparison → Section 8 (slide 42, then 43).** Before learners start, ask them to predict whether mean or median will have the lower **validation** MAE. Give structural hints only: create an independent **unfitted** candidate (for example with `clone`), set `baseline__strategy="mean"`, fit on the **same** training rows, evaluate on the **same** validation rows, and choose lower MAE (**median wins a tie**). Never direct them to test outcomes. **After the protected attempt**, reveal slide 43: training mean **4,713,074.74**, mean validation MAE **1,345,292.84**; median is the development reference **on this split**. Both are constants that ignore property differences; neither justifies claiming that the engineered ratio improves prediction.

## When the room gets stuck

**Use a graduated recovery:** (1) ask which invariant failed; (2) point to the relevant notebook section/flow on screen; (3) probe **one** value, column list or fitted object; (4) only after an attempt, selectively consult the matching solution checkpoint so the next required block can proceed. Never paste the full solution or prematurely show slide 43.

| Symptom | First useful clue / recovery |
|---|---|
| CSV not found, import/API error, stale variables | Check `DATA_PATH`, exact filename and working directory; confirm active kernel and installed versions. Restart kernel and run cells **from the top** if state is mixed; consult the solution's load checkpoint. |
| Duplicate count wrong or conflicting repeated ID | Compare **all fields**, not only IDs or prices. Do not discard a conflicting pair as if it were a verified teaching copy. |
| Split counts, targets or IDs disagree | Pass `X`, `y`, IDs together through both seeded `train_test_split` calls; check index alignment and no overlap before advancing. |
| String numeric token / zero-bedroom ratio fails | Read the already-supplied `clean_features` and test one row. Known formats are parsed; unfamiliar formats must error. Invalid area/denominator gives `NaN`, then the fitted imputer handles missing numerical features. |
| Pipeline fails, target leaks in, matrix is wrong width | Check **explicit** `RAW_FEATURES`, `NUMERIC_WITH_RATIO` (6), `CATEGORICAL` (7), step names `clean`/`columns`/`baseline`, branch order and `remainder="drop"`. Never use automatic numeric selection across `price` or `price_per_area_at_sale`. Fit training only. |
| Missing/unseen category confusion | A blank is imputed using the training mode; a **new, well-formed** furnishing term is encoded as all zeros. This is a fallback, not a new learned category. |
| Mean comparison is unfair or fails | Confirm a newly cloned/unfitted candidate and **same** training/validation partitions. Use explicit `mean_absolute_error`, not an unexplained `.score()` or a percentage. Hold the answer until the slide-43 debrief. |

## Pacing discretion and non-negotiable boundaries

If behind, compress **additional industry anecdotes → prolonged RL elaboration → second scaling arithmetic example → retyping the supplied helper → repeated table/matrix browsing**. Use a single representative fitted-state check and integrate brief debrief lines into notebook transitions. Do **not** cut the split/leakage rationale, outlier judgement, safe-versus-leaky feature contrast, **14-minute learner pipeline construction**, **10-minute independent mean attempt**, interpretation of MAE, conceptual CV or **10-minute break**. If many learners are blocked, offer staged hints, then a verified checkpoint to protect the next learning movement. Faster learners can explain why all-zero one-hot is not semantic understanding and why a constant cannot assess `area_per_bedroom`—not start regression or a new search experiment.

**Claims to protect throughout:** Training learns fitted statistics; validation compares development choices; the main test set is **never scored** here. A pipeline cannot choose legitimate features or repair a fundamentally wrong split. Mechanical preparation checks are not evidence of predictive feature value. MAE has price units and is not business approval, causation, a reliable future-performance guarantee or a deployment appraisal. Cross-validation is an **illustration of refitting within development folds**, not an extra coding lab.

## Close: three-part exit check

Ask for **one training-learned rule** (e.g., training median for missing `area`), **one fixed rule** (e.g., nonpositive `area` → missing, or known token parsing), and **one unsupported claim** (e.g., the engineered ratio improves prediction or validation MAE proves deployment readiness). Then state the bridge: the upcoming **Regression Models & Evaluation** lesson will fit a model that actually learns from property features and compare it against this reference. Keep slide 47 available as a **reference after class**, not an additional timed slide.

*Technical help, when needed:* [scikit-learn 1.7 common pitfalls](https://scikit-learn.org/1.7/common_pitfalls.html) · [scikit-learn 1.7 OneHotEncoder](https://scikit-learn.org/1.7/modules/generated/sklearn.preprocessing.OneHotEncoder.html) · [Jupyter running code and kernels](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Running%20Code.html).
