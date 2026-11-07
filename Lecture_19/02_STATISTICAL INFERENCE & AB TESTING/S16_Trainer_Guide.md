# Session 16 — Trainer Delivery Guide

**STATISTICAL INFERENCE & A/B TESTING FOR BUSINESS DECISIONS**  
Boston Institute of Analytics · Data Science and Artificial Intelligence (Generative AI and Agentic AI) · Module 6: Statistics & Math for ML  
**180 minutes total**, including a **12-minute break (77–89)** and a **28-minute integrated practical (146–174)** with at least **20 minutes of learner-owned work (150–170)**.

## 1. At a glance: the decision to teach

The recurring question is **“Page B's displayed signup rate is higher. Is that enough to launch it?”** Start with an *illustrative* dashboard (A **10.0%**, B **12.0%**), with no sample sizes or assignment evidence; **do not** give a launch verdict. Revisit six questions as the lesson progresses:

1. **Measure:** Which population, independent unit, numerator and denominator?
2. **Vary:** Could a gap arise from chance, dependence or unfair selection?
3. **Estimate:** How uncertain is the **B − A** effect?
4. **Test:** What does a predeclared, null-conditional p-value say?
5. **Validate:** Is the test appropriate, and was A/B assignment and measurement sound?
6. **Decide:** Is the effect worthwhile, credible and safe to act on?

**Non-negotiable delivery rules:** Keep real practical answers hidden until **minute ~170, after learners have attempted and saved their 5–7 sentence conclusions**. Do not project slide **71 or beyond** before that gate. Preserve the **77–89 break**, **150–170 learner attempt**, and **174–180 business debrief**. The deck explains the material; *do not read every slide aloud*. The trainer can use the detailed Teaching Content and speaker notes for explanations before class.

**Continuity:** Session 15's bike-sharing observations were days, not randomized groups. Session 16 introduces causal-design reasoning and inference on unique visitors. Session 17 takes up mathematical foundations; avoid ML modeling, optimization and advanced experimentation procedures here.

## 2. Before learners arrive

- [ ] Open the **78-slide** PowerPoint in slideshow mode; confirm projector legibility, presenter notes, and a **private** trainer screen. Do not share slide-sorter thumbnails, presenter previews, solution outputs, or a full-results deck in advance. Slide **78** is after-class references.
- [ ] Distribute **`S16_AB_Testing_Practical.ipynb`** and the unchanged **`S16_AB_Signup_Experiment.csv`** only. Keep **`S16_AB_Testing_Practical_Solution.ipynb`** and the data notes trainer-private. The CSV is fully synthetic and needs no website or account.
- [ ] Confirm the learner notebook and CSV can be accessed in the **same working directory**. In Colab, upload the CSV with the **Files** panel into the runtime working directory; files may need to be uploaded again if that runtime resets. Locally, check the Jupyter working directory. Do not rename the CSV or modify its bytes.
- [ ] Run the learner import and prepared **file-audit** cells privately, without filling the learner tasks or distributing their output. Check Python kernel availability and imports for NumPy, pandas, SciPy, statsmodels, Matplotlib and IPython.
- [ ] Execute **all code cells in the trainer solution, in order, from a fresh kernel** against the canonical CSV, and inspect the CI plot and decision reference. If your environment cannot execute it, keep the previously validated figures below as a **labelled fallback**, not as a claim of a fresh execution.
- [ ] Confirm the SHA-256 audit will pass for the original CSV: `c8ce3aaff3a6eb3909b4452feb66bede9ff65a2da7017bc7dcf90e1628ea52fb`. A mismatch is a file problem—obtain the canonical file; **never disable the checksum check**.
- [ ] Prepare a quick way to move from PowerPoint to Jupyter/Colab at **minute 150** and back at **minute 170**, without exposing trainer-only tabs. Check notebook save permissions and the learners' ability to write in Markdown cells.
- [ ] Keep a private copy of the verified numerical reference at the end of this guide. If connectivity or packages fail, preserve learners' reasoning attempt first; show reference output **only after the reveal gate**.

**Recorded compatible baseline (from the notebooks):** Python 3.12.10, NumPy 2.1.3, pandas 2.2.3, SciPy 1.14.1, statsmodels 0.14.5, Matplotlib 3.10.7. Other supported versions can work; verify the actual machine rather than installing or claiming compatibility blindly. Resolve missing packages **before** the session; package installation is not part of the 28-minute practical. The notebook uses no external API, experiment service, or live user data.

## 3. Grouped live-delivery map

Use **ANCHOR** for ideas that need a careful explanation; **QUICK** for a short illustration or check; **DO** for learner work; and **DEBRIEF** for reflection. Times are **elapsed minutes from session start**, not per-slide targets.

| Time (duration) | Slides | Mode | What the trainer does / learning to protect | First sensible compression if behind |
|---|---|---|---|---|
| **00–12 (12)** | **1–7** | ANCHOR + QUICK | Start at slide 2 with the *illustrative* 10%/12% dashboard. Ask “Ship B?” and withhold the answer. Contrast 10/100 with 1,000/10,000; establish visitor versus page view, denominator, **+2.0 pp versus +20% relative**. Bridge briefly to S15. | Shorten the show-of-hands discussion; do not reveal an A/B verdict. |
| **12–35 (23)** | **8–14** | ANCHOR | Name population, estimand, estimator and sample statistic; use repeated-sample visual (**9–10**). **Protect SD versus SE (11)**, independence, and **random sampling versus random assignment (13)**. Ask why more duplicate rows cannot fix the estimate. | Move quickly through formulas on **12** and repeat checks on **14**. |
| **35–57 (22)** | **15–23** | ANCHOR + QUICK | Explain **confidence intervals** as estimate ± uncertainty, **95% repeated-procedure coverage (17–18)**, the signed B − A interval and the **0 versus +2.0 pp** decision lines (**20–21**). **22:** overlapping separate arm CIs do not decide a difference. | Compress width variants **19** and extra checks **23**; keep coverage and signed interval interpretation. |
| **57–77 (20)** | **24–31** | ANCHOR + QUICK | Set two-sided H₀/H₁ and α *before* data; explain tail area and **p conditional on H₀** (**26–27**), reject/fail-to-reject, Type I/II and statistical versus business commitments. | Take one rather than three wording checks from **28/31**; preserve p-value meaning. |
| **77–89 (12)** | **32** | BREAK | **No teaching.** Quietly check file access and notebook readiness. | **Do not compress.** |
| **89–114 (25)** | **33–47** | ANCHOR + DEMO | Choose by **unit + outcome type**. Work one-sample mean versus benchmark (**35–37**); independent **Welch** two-mean example (**38–40**); **observed and expected chi-square counts** (**41–44**). Z (**45**) and one-way ANOVA (**46**) are **brief recognition only**. | Cut repeated t critical-value arithmetic or second explanations; retain each worked-test distinction and short Z/ANOVA recognition. |
| **114–137 (23)** | **48–60** | ANCHOR + QUICK | Contrast **correlation/association versus causation** and confounding (**48**); use visitor-level sticky random assignment (**49–50**). Fix design, date/outcome window, primary KPI, test and **+2.0 pp** threshold **before** results (**51–53**). Discuss allocation/logging failures, sample-ratio mismatch, peeking, guardrails, significance versus value (**54–60**). | Shorten extra warning examples and variants on **55–59**; keep eligibility, denominator, validity and precommitment. |
| **137–146 (9)** | **61–62** | QUICK ANCHOR | Relate effect size, independent n, SE, α, Type II error and **power = 1 − β**. Slide **61** depicts **both tails**; the business minimum is **not** the formally planned minimum detectable effect. No derivation or power calculator. | Explain the main visual once and do not elaborate sample-size formulas. |
| **146–174 (28)** | **63–74** | **DO**, then short DEBRIEF | **146–150:** orient (**63–66**) and switch to learner notebook. **150–170:** protect **20 minutes of learner attempt** (**67–70**, optional hints only). **170–174:** after saved notes, transition **71** and selectively reveal **72–74**. | Reduce trainer talk and optional troubleshooting slide; **never steal the 20-minute attempt or reveal early**. |
| **174–180 (6)** | **75–77** | **DEBRIEF** | Ask whether a difference was detected, whether +2.0 pp was established, and whether operational validity/economics justify action. Compare different defensible learner recommendations, then connect to next session. | Ask one learner for a single well-qualified recommendation; keep all three decision distinctions. |
| **After class** | **78** | REFERENCE | Sources and reading; not an extra lecture block. | — |

**Teaching emphasis:** Longer deck sections do not imply equal delivery time per slide. The **15 slides in the 89–114 block** include quick orientation and comparison slides as well as three compact worked examples; Z and ANOVA must not turn into extra exercises. Use the notes' ANCHOR/QUICK rhythm, not a rigid “minutes per slide” rule.

## 4. High-leverage spoken checks and recoveries

Ask **one useful question** at the indicated movement, listen for the reasoning, and correct the *meaning*, not just the calculation.

| Slides | Ask | Listen for / recovery if needed |
|---|---|---|
| **2–7** | “What else would we need before shipping B?” | Sample size, distinct eligible people, fair assignment, matched signup definition, business costs. **10%→12%** is **+2 pp**, **+20% relative to A**, not the actual experiment. |
| **9–14** | “If 64 tickets have SD 8 minutes, why is the mean's SE only 1?” | `8/√64 = 1`; **SD describes individuals, SE the statistic across samples**. More clicks from the same user do not provide new independent units. |
| **17–23** | “What repeats when we say ‘95% confidence’?” | The **method producing intervals**, not the fixed true effect. Read an effect-difference CI in **pp**; separate arm intervals are not an interval for **B − A**. |
| **24–31** | “Does p = 0.03 mean H₀ has a 3% chance of being true?” | No: under the null model, a test statistic at least as extreme has about 3% probability. **p ≥ α means fail to reject**, not “proved equal.” α and business threshold are different. |
| **35–47** | “Which test for handling minutes? Which for signup yes/no?” | Numeric one-mean benchmark → one-sample t; independent two-mean comparison → **Welch t**; binary conversion by arm → **Pearson chi-square counts** and a difference-of-proportions interval. Z/ANOVA are recognitions, not primary practical methods. |
| **48–60** | “Could an association survive without a causal page effect?” | Yes: self-selection, campaign mix, wrong exposure/logging. Random assignment supports comparability **in expectation**; exact equal synthetic quotas do **not** prove a functioning randomizer. |
| **61–62** | “If a real improvement exists, why might a test miss it?” | Limited independent n, small effect, noisy measurements, fixed α; Type II error. Slide 61 illustrates about **24% versus 71% power** for two assumed sample sizes. **Both positive and negative rejection regions** count; this is not a calculation from the practical data. |
| **75–77** | “Is detected the same as worthwhile and safe to deploy?” | **Three distinct claims:** null-based detection, commercial effect/uncertainty, and trustworthy implementation plus guardrails. |

**Fast example anchors for test selection (not signup practical data):** One-sample support cases versus **16 minutes**: `t(7) ≈ 2.646`, `p ≈ 0.0331`; independent Welch workflow comparison: **B − A = −3.25 minutes**, `t ≈ −2.662`, `df ≈ 12.63`, `p ≈ 0.01998`; invented chi-square table **A [14, 86], B [20, 80]**: `χ² ≈ 1.276`, `p ≈ 0.2587`. These examples use **different outcomes and populations**; do not confuse them with the synthetic website CSV. A Z-test with genuinely known population SD and one-way ANOVA for **three or more means** stay conceptual. Never use “n ≥ 30, therefore Z” or suggest a significant omnibus ANOVA names the differing pair.

## 5. Practical run-of-show: keep learners in charge

**Purpose for the room:** Use the earlier inference and experiment-design reasoning to inspect one fictional, visitor-level signup test, implement a small number of missing Pandas/statistics expressions, and **write an evidence-qualified 5–7 sentence product recommendation**. Familiar parts are notebook execution, `groupby` and arithmetic; the newly integrated pieces are the chi-square's **null-expected** counts, the **Newcombe B − A** interval, and defending a business decision.

| Clock | Deck / tool state | Trainer action and learner work |
|---|---|---|
| **146–147** | **63** | Announce a 28-minute investigation. Say the file is **synthetic**, not a real experiment or proof of randomization. Show no outcome totals. |
| **147–150** | **64–66**, then Jupyter/Colab | Confirm `S16_AB_Testing_Practical.ipynb` and the CSV are in the working directory; identify **`visitor_id`, `variant`, `converted`, `assignment_date`**. Explain that one row = one eligible visitor, not a visit or date. Point to tasks and final note; **do not demo the solutions**. |
| **150–153** | **67**; learner Markdown Task 1 | Learners pre-record A=current/B=simplified, visitor unit, KPI numerator and **all assigned visitors** denominator, 14-day assignments + individual seven-day signup window, **two-sided H₀: p_B = p_A / H₁: p_B ≠ p_A**, α=0.05, uncorrected chi-square, Newcombe **B first**, and **+2.0 pp** business minimum. Ask: “Which of these must not change after we see outcomes?” |
| **153–164** | **68**; learner notebook Tasks 2–5 | Learners run **prepared imports and audit** first; complete the `None`/TODO expressions for nonconversion, rates, observed **2×2** counts, signed pp and relative lift. Set `correction_choice` and compute chi-square; fill B-then-A converted counts in Newcombe call, convert bounds to pp, interpret zero and +2.0 lines. **Circulate with hints, not answers.** |
| **~164–170** | Briefly show **69**; return to **68**. Use **70** only if many are stuck (ideally after minute 158). | Require individual **5–7 sentence notes**: unit/KPI, arm rates/effects, predeclared test, CI/threshold, a validity or guardrail limitation, and defensible action. Have learners **save** their note. Still no slide 71+, solution notebook or summary screenshot. |
| **170–171** | **71** *only after saved attempts* | Explicit gate: “You've committed to your interpretation; now compare with the verified analysis.” If learners are behind, favor a saved incomplete-but-honest reasoning attempt over prematurely handing them the answers. |
| **171–174** | **72–74** | Reveal **descriptive counts/rates → chi-square/expected counts → CI and threshold**, in that order; invite one correction to the learner's own explanation. Keep this short so the final six-minute decision block survives. |
| **174–180** | **75–77** | Lead the decision debate and close (see Section 8). |

**Audit limits to reinforce:** The notebook checks column order, row count, SHA-256, unique IDs, missingness, arm values, binary outcomes and all 14 dates; a valid CSV **cannot** verify actual randomizer behavior, sticky exposure, instrumentation, outages, cost, retention or other unrecorded guardrails. Do not turn `assignment_date` into 14 independent observations.

**Decision note quality check:** Look for the *signed effect in pp*, an appropriately conditional claim about the p-value, CI compared with **both** zero and +2.0 pp, and **one concrete limitation plus next step**. A sensible answer may withhold a full launch and propose an instrumentation check, guardrail evaluation, controlled rollout or properly planned follow-up evidence; do not force one exact wording if reasoning is sound.

## 6. Troubleshooting without solving the exercise

| Symptom or misconception | Quick diagnostic / recovery prompt |
|---|---|
| `FileNotFoundError` / missing CSV | Ask: “Where is the kernel's current working directory, and is the exact CSV name there?” Local Jupyter: place file beside notebook; Colab: use Files upload into runtime working directory. Rerun the **audit**, not a substitute dataset. |
| SHA-256 differs / schema assert fails | The supplied file was altered, exported with an index, or replaced. Restore the **canonical CSV**; do not remove checksum/schema assertions to make it run. |
| `ModuleNotFoundError` / version incompatibility | Identify the **specific missing package** and active kernel; use the notebook's documented baseline or a compatible verified setup; install/restart **before class where possible**. Check with the original import cell. Do not claim an untested runtime is validated. |
| `NotImplementedError` from Task 2, 3, 4 or 5 | This is an **intentional incomplete learner cell**. Ask which `None`/TODO expression or `correction_choice` remains unset, and which earlier slide supplies the reasoning. Do not paste the trainer cell. |
| `NameError`, missing `summary`, `observed` or rate values | A required earlier cell was skipped, edited or not rerun. Work **top to bottom** after edits; check that Task 2 creates `summary` before Task 3 uses it. |
| Wrong denominator / unexpected counts | Ask: “Where did the nonconverters go?” Count **all assigned eligible visitors**, not page views, sessions, conversions only or the 14 dates. Verify A then B rows, converted then not-converted columns. |
| Effect sign or units reversed | Ask: “Which subtraction is the business question?” **B − A**. Rate differences are probability units until multiplied by **100 for pp**; relative lift divides by **A's rate** and then multiplies by 100. |
| Chi-square or p differs | Check `observed` row/column order and whether the learner chose `correction=False`. SciPy defaults to a Yates correction for 2×2 tables unless told otherwise; **do not change the prespecified test to fit the result**. |
| Newcombe interval sign/size differs | Confirm **B is `count1`/`nobs1`**, A is `count2`/`nobs2`; `compare='diff'`, `method='newcomb'`, `alpha=0.05`; convert *both* interval endpoints into **pp**. Do not substitute a Wald interval. |
| Expected cells called “predictions” | Ask: “Expected under which hypothesis?” They are **null-model comparison counts**, not forecasts of future signups. |
| “p is P(H₀ true)”, “not significant means equal”, or “significant means launch” | Ask for three sentences: **what the null test detects; what the estimated effect/CI imply about +2.0; what the four columns cannot verify**. Keep these questions separate. |
| “Exactly 5,000 each means randomization worked” | Explain fixed synthetic quotas. Actual assignment and logging/exposure quality require separate operational evidence; balanced counts alone do not demonstrate randomization. |

**Room-level fallback:** If technology fails widely, do **not** spend the entire practical on package repair. Preserve Task 1, interpretation questions and each learner's draft decision; use the previously validated results **only after the minute-170 reveal**, clearly identifying them as a reference rather than fresh execution. If few learners are stuck, circulate and ask diagnostic questions while others continue. The optional reflection is not required live.

## 7. If the class runs late

1. **First reduce repetitions:** shorten slides **19, 23, 28/31, 55–59**; take one check rather than several, and avoid reiterating an already-understood arithmetic example.
2. **Then shorten optional elaboration:** skip detailed critical-value lookups in the t examples, additional chart commentary, and extended Z/ANOVA/power explanation. Still name **why** each test fits, work the one-sample t, Welch t and chi-square mechanisms, and keep the two-tailed power interpretation.
3. **Tighten transitions, not learner ownership:** pre-open the notebook and CSV before class; spend **146–150** orienting, not fixing packages; use slide 70 only for a shared blocker. Keep **150–170** as a genuine attempt, **170–174** as a selective reveal, and **174–180** for judgment.
4. **Never trade away:** SD vs SE; repeated CI coverage; correct p-value/fail-to-reject language; randomization, unit, denominator and preregistered business rule; the **12-minute break**; the **20-minute attempt**; or an explicitly qualified closing recommendation.

## 8. Final six-minute debrief (slides 75–77)

**174–176, slide 75 — Three claims:** Invite a learner to answer (a) was equality rejected at α = 0.05, (b) did the data establish **at least +2.0 pp**, and (c) has a valid operational experiment and a safe launch been demonstrated? Require **separate answers**.

**176–178, slide 76 — Decision quality:** Have learners point to their own evidence, uncertainty, limitation and proposed action. Accept different cautious next steps if costs, guardrails, future visitors and instrumentation are treated as unknown rather than made-up facts. The synthetic result does not prove a real product improvement.

**178–180, slide 77 — Transfer:** Ask “Would you ship B, and what one further fact matters most?” End with the reusable path **unit → estimate/SE → interval → null test → validity → business rule → action**. Preview that S17 develops the mathematical tools behind later ML, **not** an extension of today's A/B inference or additional model training.

---

## Trainer-only answer reference — **do not distribute or project before minute 170**

The following values are for private checking and the **slides 72–76 debrief**, not for preparing the opening slides or helping learners finish an incomplete expression. The study is **wholly synthetic**.

| Item | Verified answer / operational meaning |
|---|---|
| Observation and horizon | **10,000 unique assigned eligible visitors**; fictional assignment dates **2026-09-01–2026-09-14**. Per visitor, `converted=1` means signup on assignment day or next six days. Last possible outcome-window day **2026-09-20**. |
| Exact columns | `visitor_id`, `variant`, `converted`, `assignment_date`; analysis unit is a **visitor**, not a date or page view. |
| Arm A: current control | **5,000 assigned; 600 converted; 4,400 not converted; 12.0%**. |
| Arm B: simplified treatment | **5,000 assigned; 675 converted; 4,325 not converted; 13.5%**. |
| Effect | **B − A = +1.5 percentage points**; **+12.5% relative** to A's 12.0% conversion rate. |
| Hypotheses / rules | **H₀: p_B = p_A; H₁: p_B ≠ p_A**, two-sided; α = **0.05**. **Minimum worthwhile: +2.0 pp**, separately chosen beforehand, **not** a formal MDE. |
| Observed 2×2 counts | Rows **A then B**; columns **converted then not converted**: `[[600, 4400], [675, 4325]]`. |
| Pearson chi-square | `scipy.stats.chi2_contingency(observed, correction=False)` → **χ² = 5.0564638463**, **df = 1**, **p = 0.0245342485**. Under valid assumptions, reject equality at 0.05. |
| Expected under H₀ | **637.5 converted**, **4,362.5 not converted** in **each** arm. These are not forecasts. |
| Signed confidence interval | `confint_proportions_2indep` with **B first**, **A second**, `compare='diff'`, `method='newcomb'`, `alpha=0.05` → **95% CI = +0.192359 to +2.808042 pp** for **B − A**. The API returns probability units: multiply endpoints by 100 for pp. |
| Interpretation | Interval excludes **0** but crosses **+2.0 pp**; observed **+1.5 pp** falls short of the commercial target. Evidence for a nonzero difference is **not** evidence that the target was achieved or that unmeasured guardrails are acceptable. |
| Causal / operational limits | The CSV does **not** prove genuine randomization, persistent page exposure, logging accuracy, performance, crashes, user impact, costs, retention or generalization to future visitors. Exact arm balance is constructed, not proof of a real assignment system. |

**Reference conclusion to paraphrase, not dictate:** A higher synthetic B conversion rate was detected by the prespecified two-sided Pearson test under its assumptions. The point effect is **below** the minimum worthwhile improvement; the Newcombe interval contains both smaller and larger effects than that target. Without operational randomization/exposure/logging audits and economic or user guardrails, an unconditional rollout is not supported. Explain the uncertainty and propose a bounded next step—validate tracking, inspect guardrails and costs, consider a controlled rollout or collect appropriately planned further evidence.

### Technical references

- [SciPy — `chi2_contingency`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.contingency.chi2_contingency.html): continuity-correction argument and null-expected counts.
- [statsmodels — `confint_proportions_2indep`](https://www.statsmodels.org/stable/generated/statsmodels.stats.proportion.confint_proportions_2indep.html): `compare='diff'` means first proportion minus second; explicit `method='newcomb'`.
- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html): hosted notebook environment and runtime considerations.

Use the canonical learner notebook and its prepared checks for local instructions. Nothing in the file proves that a live website experiment was conducted.
