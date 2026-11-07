# Session 15 — Short Trainer Guide

**Statistics, Probability & Sampling** · Module 6 · 180 minutes · 79-slide teaching deck

## At a glance

**Purpose:** Move beyond the dashboard mean: describe observed daily rentals, explain their spread and selection, and distinguish what the evidence can and cannot claim.

**Three recurring checks:** What is the unit? · Who or what is represented? · What does the summary omit?

**Learner entry:** Mixed mathematical confidence; scheduled exposure to Python/Pandas/charts is not proof of fluency. Explain the fraction and denominator before probability notation.

**Protected:** 8–10 minute worked variance trace; conditional-denominator reasoning; raw days versus sample means; 14 + 19 minutes of notebook work; 12-minute break.

**Boundary:** Do not teach formal inference (S16), gradients/optimisation (S17), predictive models (S18+) or time-series methods here.

## Before learners arrive

- [ ] **Files on the teaching machine:** S15 Statistics, Probability & Sampling.pptx; S15_Statistics_Practical.ipynb; unchanged day.csv; trainer-only S15_Statistics_Practical_Solution.ipynb; S15_Bike_Sharing_Source_Notes.md.
- [ ] **Set the learner workspace:** Place day.csv beside the learner notebook in the active working folder. Notebook uses `Path("day.csv")`; confirm the built-in SHA-256 check passes.
- [ ] **Do a fresh-kernel dry run:** Run the trainer solution in order through the plots, event table, 2012-09-15 z-score and seeded sample-mean simulation; confirm Python, Pandas, NumPy and Matplotlib work.
- [ ] **Keep the two versions separate:** Distribute the scaffolded learner notebook with seven C1.3 None entries, four C2.2 count entries and one C2.3 z-score entry. Keep the completed solution private until checks.
- [ ] **Decide the classroom path:** Local Jupyter can run offline; if using Colab, upload day.csv into the current runtime. Runtime resets may require re-upload. Do not depend on APIs, ML packages or live downloads.
- [ ] **Prepare a non-executing fallback:** Have previously verified views of the dataset, histogram/boxplot, event table and resampling visual available; label them as prepared outputs if used.
- [ ] **Keep time visible:** Put 75, 89, 101, 155, 174 and 180 on your time cue. Leave both checkpoint windows and the break intact; debriefs are selective within those windows.

**Dataset checksum:** `a6bcf826782d3c0fbfdcbeead17cd0884185a0dafe8ff10cd48a874ee7ba18be` (SHA-256 of `day.csv`).

## Live delivery map

### 00–101 minutes · Statistical foundations

Use slide ranges as landmarks, not a minutes-per-slide schedule. Hold a visual when it clarifies an idea; move quickly past labels that learners already understand.

| Clock / deck slides | Delivery mode and trainer action | If behind |
| --- | --- | --- |
| 00-14 · 1-8 | **ANCHOR / QUICK.** Start with the same KPI but different operating conditions. Elicit a staffing prediction. Distinguish description, inference and chance; read 5/20 = 25% by naming both counts. Close with the three recurring questions. | Shorten the ML preview (6), not the denominator refresher (7). |
| 14-27 · 9-15 | **ANCHOR / QUICK.** Use an actual day.csv row to locate observation versus variable; have pairs classify the integer-coded season, workingday, weathersit versus cnt and normalized temp/hum. Define frame N = 731 and sample n = 50 before mu and x-bar. | Make nominal/ordinal vocabulary brief; keep real row and frame/sample distinction. |
| 27-45 · 16-22 | **ANCHOR / DEMO.** Predict whether a random 50 and the first 50 days match the frame. Make simple random selection concrete; explain season-stratified draws and one correct systematic and cluster example. Distinguish sampling variation from biased selection. | Compress 19-21 after method meaning lands; do not suggest a single random draw must match. |
| 45-75 · 23-38 | **ANCHOR.** Mean/median/mode, the 200 outlier, quartiles, range and IQR; compare same-mean/different-spread series. Protect 8-10 minutes for slides 30-34: mean -> deviations -> squares -> sum -> N versus n-1 -> square root and units. Finish with shape and reporting choice. | Briefly mention variant quantile rules (27), extra outlier and shape comparisons; never compress the variance reasoning to formulas. |
| 75-89 · 39-42 | **DO / SELECTIVE DEBRIEF.** Leave the deck for S15_Statistics_Practical.ipynb. Learners attempt C1.1-C1.4; use slides 41-42 to verify selected outputs only after their attempt. Keep the full 14-minute checkpoint allocation. | Reduce reveal to one selection caveat and one centre/spread interpretation; avoid new tasks. |
| 89-101 · 43 | **BREAK.** Stop instruction for 12 minutes. Keep notebooks accessible and resolve only minor setup snags without converting the break into a compulsory demonstration. | Break remains 12 minutes. |

**Non-negotiable:** The full first-half sequence must lead to a genuine learner attempt. The prepared result slides are not new teaching blocks beyond the scheduled checkpoint.

### 101–180 minutes · Probability and uncertainty

| Clock / deck slides | Delivery mode and trainer action | If behind |
| --- | --- | --- |
| 101-121 · 44-54 | **ANCHOR / QUICK.** Contrast a model probability with the historical count fraction. Define H: cnt >= 5000 and W: workingday == 1, but keep dataset counts hidden. Use the invented cafe 2x2 table for P(S\|R); teach complement, inclusive OR, intersection, P(A\|B), independence versus mutual exclusion. | One carefully worked denominator and one exclusive-versus-independent check beat repeated exercises. |
| 121-139 · 55-62 | **ANCHOR / DEMO.** Contrast a discrete PMF, continuous PDF area, and empirical counts. Show the normal model only conditionally; 68-95-99.7 is not universal. Read z as signed SD distance before the real-day checkpoint. | Use prepared plots; skip additional curve variations, never confuse mass with density. |
| 139-155 · 63-69 | **ANCHOR / DEMO.** One raw-day observation versus one sample mean versus a distribution of repeated sample means. Use n = 5 and n = 50 prepared resampling views; explain narrowing spread under stated independent-draw model, not future forecasts. | Slide 68 is optional. Protect raw-days-versus-means and independence caveats. |
| 155-174 · 70-75 | **DO / SELECTIVE DEBRIEF.** Return to the learner notebook for C2.1-C2.5. Learners calculate event denominators and z, read simulation panels and write a 4-6 sentence analyst note. Slides 72-75 are selective checks only after attempts. | Prioritize denominator, one z reading and the analyst note; no mandatory extra debrief minutes. |
| 174-180 · 76-79 | **QUICK / DEBRIEF.** Close the chain: unit -> selection -> centre/spread/shape -> conditional rate -> limits. Use misconception prompts as needed; leave S16 inference question open. Slide 79 is attribution/reference, not an extra teaching block. | One real-data claim and one S16 question are enough if time is tight. |

### If the room runs late

**Protect:** First-time interpretation and arithmetic; 8-10 minute variance trace; conditional denominator; raw data versus sample means; C1 (14 min), C2 (19 min), break (12 min), final evidence check.

**Compress in this order:** (1) Secondary sampling-method elaboration (slides 19–21); (2) repeated outlier/quantile treatment (slides 24, 27, 29); (3) extra model/curve examples and the optional skewed simulation (slide 68); (4) a second pass over already-resolved comparisons.

Live judgement: brief answer slides and speaker notes need not be narrated in full. Preserve coverage of each named topic without turning quick checks into lectures.

## Learner checkpoint facilitation

### Checkpoint 1 · What do the days reveal?

*75-89 min · Slides 39-42 · ~14 minutes total, including framing and selective checks*

| Trainer action | What to notice or verify |
| --- | --- |
| Before learner attempt | Connect back to row = day, categories versus measurements, full frame versus selected days, and why centre needs a shape/spread view. Open S15_Statistics_Practical.ipynb with day.csv available. |
| Learners own | C1.1 inspection and cnt identity; C1.2 random 50 (seed 1501) versus first 50 dates; C1.3 seven expressions for mean, median, Q1, Q3, P90, variance and SD; C1.4 method/selection judgement. |
| Circulate and diagnose | A season code is categorical, temp is normalized, and no row is a single ride. For C1.3: quantiles use linear interpolation and population spread uses ddof=0; chart needs a correct mean/median reference. Ask: what does this average hide? |
| Reveal after attempts | Slides 41-42: frame 4,504.35 mean versus 4,548 median; random 50 mean 4,492.52, first 50 mean 1,420.66. Highlight one spread fact and why the first 50 dates overrepresent early-period days. Do not lecture through every cell. |

### Checkpoint 2 · Can we responsibly explain demand?

*155-174 min · Slides 70-75 · ~19 minutes total, including selective debrief*

| Trainer action | What to notice or verify |
| --- | --- |
| Before learner attempt | Reconnect events, conditional denominators, z-score and the repeated-sampling display. The notebook continues from prepared die/PMF-PDF and seed-1516 simulation cells; no second dataset or new model. |
| Learners own | C2.1 shape/reporting; C2.2 four event counts for H and W; C2.3 one z expression for 2012-09-15; C2.4 raw days versus means of 5/50; C2.5 4-6 sentence analyst note. |
| Circulate and diagnose | P(H\|W) denominator is 500 working days, not 731. The +2.17 z is SD distance, not a normal percentile. The 2,000 resamples of historical observations are not new independent future days. |
| Reveal after attempts | Use slides 72-75 sparingly: the 2x2 counts, signed position, narrower sample means and example analyst-note structure. Keep the worked note hidden until learners write their own; return to one valid evidence-qualified conclusion. |

**Checkpoint rule:** The 14- and 19-minute windows already contain the selected answer checks. They are not learner time plus a new untimed debrief.

## Ask one question; land one meaning

| Concept | Ask / expected reasoning | If the response is off |
| --- | --- | --- |
| KPI / rows | "What is being averaged?" One daily count per recorded day, not rides or riders. | Point to one dated row (slide 9). |
| Coded values | "Is season 2.5 meaningful?" No; integer-coded labels are groups. | Ask whether addition changes the meaning of a label. |
| Frame / claim | "Does this file describe next year?" No: it is the complete 2011-2012 daily historical frame. | Make the target group explicit before judging the calculation. |
| Sampling | "If random 50 is different, did randomness fail?" No; sample variation is expected. | Contrast fair method with a guaranteed result. |
| Centre / shape | "When 200 appears, which centre moved?" Mean to 45.71, median stays 20 here. | Median is resistant, not impossible to change. |
| Variance | "Why square, then root?" Prevent deviation cancellation; SD returns original units. | Walk -10 -> 100 and sum 250 before formulas; name N vs n-1. |
| Conditional event | "Out of which days is P(H\|W)?" 195 out of 500 working days. | Circle the W row total, not the grand total. |
| Independent/exclusive | "If even, can the die be odd?" No: disjoint events with positive chance are dependent. | Test whether learning one changes the other. |
| Distribution / z | "PMF bar versus PDF curve?" Mass per value versus probability as interval area. z gives signed distance. | A z-score does not certify normality or a percentile. |
| CLT | "What becomes more normal?" Repeated sample means under conditions, not raw days. | Point to middle/right panels; note with-replacement historical resampling. |

## When the classroom gets stuck

| Problem | Fast recovery |
| --- | --- |
| CSV missing / wrong hash | Check notebook working directory and exact filename; restore the approved day.csv and retry. Do not disable the SHA check or silently fetch a different revision. |
| None / "complete expressions" | Confirm it is the learner version. The None fields in C1.3, C2.2 and C2.3 are the exercise, not broken upstream code. |
| Blank chart / undefined name | Re-run the prepared cells sequentially from a clean kernel; inspect path and completed earlier learner tasks before editing plotting code. |
| Different SD or quantile | Ask which data subset and divisor were used. For full frame use ddof=0; Pandas default is ddof=1, NumPy default ddof=0. Use linear-interpolated quantiles. |
| Time or runtime failure | Switch to a clearly labelled previously verified display and continue the reasoning. Do not present a screenshot as a fresh execution. Retest later outside learner time. |

## Numbers worth having at hand

| Trainer-only reference | Expected result / interpretation |
| --- | --- |
| Data integrity | 731 days x 16 columns; 2011-01-01 to 2012-12-31 inclusive; no missing dates; cnt = casual + registered in every row. Historical frame, not a representative future sample. |
| Daily cnt, full frame | Mean 4,504.35; median 4,548; Q1 3,152; Q3 5,956; P90 7,290; IQR 2,804; population SD 1,935.89 (ddof=0); min 22, max 8,714. Shape is broad, not strongly right-skewed. |
| 50-day comparisons | Seed 1501 simple random 50: mean 4,492.52, median 4,527.5. Chronological first 50: mean 1,420.66, median 1,486.5. Do not promise every random sample is this close. |
| 2x2 table H/W | H: cnt >= 5000; W: workingday == 1. W & H 195; W & not H 305; not W & H 91; not W & not H 140. H total 286, W total 500. |
| Empirical rates | P(H) = 286/731 = 0.3912; P(H\|W) = 195/500 = 0.3900; P(H\|not W) = 91/231 = 0.3939. Near-equality neither proves independence nor implies causality. |
| Reference z | 2012-09-15 has cnt = 8,714. z = (8,714 - 4,504.35) / 1,935.89 ~ +2.17 historical-frame SDs. Do not translate to a normal-model percentile. |
| Resampling visual | Seed 1516, 2,000 resamples with replacement from the frame: raw-day SD 1,935.9; SD of means n=5 about 846.8, n=50 about 266.3. They are sample means, not new demand observations. |
| Five-value variance | [5,10,15,20,25], mean 15; deviations [-10,-5,0,5,10]; squared deviations [100,25,0,25,100]; sum 250. Population: variance 50, SD 7.07; sample: variance 62.5, SD 7.91. |
| Mean sensitivity | [10,15,20,25,30,20] mean=20 and median=20; after adding 200: mean=45.71 and median=20. Same-mean sets [48,49,50,51,52] and [30,40,50,60,70] have different spread. |

## Final six-minute evidence check · Slides 76–78

Invite a 4-6 sentence analyst note: name the 2011-2012 system and unit; give a central daily count; quantify spread and characterize shape; report P(H|W) with 195/500; identify sampling/coverage and future-claim limits. Ask: "What would we need before generalizing a sample pattern beyond these observed days?" Leave formal confidence statements and tests for Session 16.

**References:** Fanaee-T (2013), [UCI Bike Sharing](https://doi.org/10.24432/C5W894), CC BY 4.0; [pandas `Series.std`](https://pandas.pydata.org/docs/reference/api/pandas.Series.std.html); [NumPy `std`](https://numpy.org/doc/stable/reference/generated/numpy.std); [Google Colab FAQ](https://research.google.com/colaboratory/faq.html). Use the dataset source notes for season-label and normalized-temperature caveats.
