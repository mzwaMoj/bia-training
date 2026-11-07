# Session 17 — Math Foundations for Machine Learning
## In-person trainer delivery guide

**Course:** Boston Institute of Analytics — Data Science and Artificial Intelligence (Generative AI and Agentic AI)  
**Module:** 6 — Statistics & Math for ML  
**Live duration:** 180 minutes, including a 12-minute break  
**Audience:** Mixed-level fresh graduates and career changers  
**Teaching materials:** `S17 Math Foundations for Machine Learning.pptx` (99 slides); `S17_Gradient_Descent_Practical.ipynb` (learner); `S17_Gradient_Descent_Practical_Solution.ipynb` (trainer only); `S17_Teaching_Content.md` (deeper explanation)

> **The session in one sentence:** An invented delivery-time rule turns an order's feature numbers into a prediction; we score its mistakes and use the gradient to change **one shared coefficient**, then inspect the result in NumPy and Matplotlib.

**Delivery priorities:** Teach the meaning before the notation; elicit an answer before displaying a check slide; protect the three guided calculations; keep the 76–88 break and 147–170 independent attempt intact. **Slide 83 is the solution gate:** learners save their 4–6-sentence interpretation *before* any seven-step reference trace, three-rate results, private solution or known optimum is shown. Slides 84–94 are reference material, **not** ten slides to lecture through in five minutes.

The slide deck is a visual teaching resource. Use it to anchor explanations, shift to the *learner notebook* for guided calculations, and then stop presenting while learners work. Do not allocate equal speaking time to every slide. Use the detailed Teaching Content if a learner needs a fuller conceptual explanation, and the private solution notebook for technical checks, not live answer projection.

## 1. Before learners enter: classroom pre-flight

| Check | Trainer action / readiness condition |
|---|---|
| Files | Distribute or make accessible **only** `S17_Gradient_Descent_Practical.ipynb` to learners. Keep the complete solution in a separate, non-projected window or device. Have the 99-slide `.pptx` and Teaching Content available locally. |
| Runtime | Choose **local Jupyter** or **Google Colab** and confirm an executable Python kernel with NumPy and Matplotlib. In Colab, learners may need a Google sign-in and **File → Upload notebook** to open the supplied `.ipynb`. Do not promise login-free Colab access. |
| Clean run | On the intended trainer environment, restart the kernel and run the **trainer solution** from top to bottom. Confirm the setup array, all three guided values, the seven-update history, the trajectory and three-panel rate plot. A fresh-kernel test matters more than old saved outputs. |
| Learner state | Open the learner notebook on a separate copy. Check that its setup and guided cells run in order; its `TODO` cells are **intentionally incomplete** and can raise `NotImplementedError`. Do not replace these with solutions before distribution. |
| Screen & sound | Test projector legibility, PowerPoint ↔ Jupyter/Colab switching, full-screen slide navigation and room visibility. Prepare a visible timer; verify internet if using Colab. A mathematical explanation should not depend on a slide animation. |
| Fallback | Keep the four-order table and blank paper available. If a device fails, learners can still compute a dot product, errors/MSE, gradient, first update and rate predictions by hand, then discuss plots at the permitted debrief. |
| Data and packages | The notebook embeds its **four synthetic cases**. No CSV, custom `.py` script, external API, scikit-learn fit or separate dataset is needed. Existing local packages or a working hosted environment **are** needed. |

**First minute of room setup:** Ask learners to locate the learner notebook, not to run all cells blindly. If the environment is unreliable, identify affected learners and the paper fallback before minute 142. A restarted kernel requires rerunning the earlier setup cells, because variables from a previous session no longer exist.

### Start-of-class mental model

Use an order estimated at **2 km and 3 items** (opening slides 2–3) to surface ordinary reasoning, then introduce the shared rule in words: **10 base minutes + 4 minutes per kilometre + 2 minutes per item**. The question is not "Can you fit a predictor?" but "Which numbers describe *this order*, which numbers define *the rule for every order*, and how can the rule be improved?" The four measured-looking rows are **invented**, not business evidence.

## 2. Live run-of-show — use the actual 99-slide deck

Elapsed times are **inclusive of** discussion, demonstrating the notebook, moving between windows and taking questions. The final column indicates what to shorten *within that block*, not where to borrow protected time.

| Elapsed | Slides | Mode and trainer action | Observable learner action / compression choice |
|---|---|---|---|
| **00–10** | **1–9** | **OPEN / ANCHOR / QUICK.** Take estimates for the 2-km/3-item order; use slides 3–5 to distinguish order inputs, shared weights, invented target rows and the predict → compare → correct chain. Ask slide 6; only then advance to answer 7. | Learner can say which value belongs to an order and which belongs to the common rule. If late, reduce pair discussion and move briskly through 8–9. |
| **10–32** | **10–18** | **ANCHOR / DO.** Contrast scalar with ordered feature vector `[3,2]`, locate Case 3 on the labelled two-feature plane (13), explain shape `(2,)`, targets outside features and feature-vs-weight units. Ask coordinate check 14 before showing 15. | Point to (3 km, 2 items), read the two axes, reject `[3,2,23]` as inputs. Compress repeated vector questions, not the input/target distinction. |
| **32–55** | **19–31** | **ANCHOR / QUICK DEMO.** Stack four cases into `X`, identify `(4,2)`, compare scalar/additive and broadcast `*` to the weighted `@` product. Ask slide 22 before answer 23. Show the invalid `(4,2) @ (3,)` and compact `X @ W`; recognize `X.T`. | Predict shape **and meaning**; explain why `*` keeps two contributions but `@` gives one per case. Trim repeated shapes, matrix–matrix talk and transpose recognition first. |
| **55–76** | **32–38** | **ANCHOR / GUIDED DO.** Explain Case 3 dot product and `+ b`, then four predictions. **Slides 37–38: Guided Check 1, about 6 min**, paper → learner notebook → brief readout. | Case 3 weighted subtotal 16, prediction 26, four-case output `(4,)`. Case 2 is fast-finisher extension only. Compress earlier verbal repetitions, not the actual check. |
| **76–88** | **39** | **BREAK.** Twelve minutes, no compulsory coding or extra lecture. | Learners step away; restart promptly at minute 88. |
| **88–108** | **40–50** | **ANCHOR / GUIDED DO.** Define function, input and parameter; compute signed errors, squares and MSE. Introduce `L(a)` as a loss for each choice of **a**, not a distance plot. **Slides 46–47: Guided Check 2, 6–7 min.** | Write errors, squares and `7.5 min²`, then explain what this does *not* show. Reduce optional comparisons of loss choices if late. |
| **108–126** | **51–60** | **ANCHOR / QUICK DO.** Read curve slope, use small-change example before `dL/da`, calculate the one-parameter gradient and recognize a gradient vector. Use question 59, answer 60. | Explain **positive gradient ⇒ locally lower a** with a suitably small positive step; derivative is not the per-case error. Keep calculus intuitive; trim generic curve repetition. |
| **126–142** | **61–71** | **ANCHOR / GUIDED DO.** Predict → loss → gradient → subtract scaled gradient → repeat. **Slides 65–66: Guided Check 3, ~4 min**. Define iteration 0 and ask qualitative small/moderate/large rate predictions at 70. | Pair calculation: step 0.75, updated a 3.25, new MSE 0.46875. Do not reveal full histories or the optimum. Trim hypothetical rate anecdotes, not the update. |
| **142–147** | **72–76** | **ORIENT / DEMO.** Reconnect the notebook to guided checks; identify supplied `prediction(a)`, `loss(a)` and plot helpers versus learner-owned gradient, loop and interpretation. Confirm notebook access and saving, then **leave the deck**. | Every learner can run setup cells, find TODOs and knows that incomplete TODO cells may stop execution intentionally. Avoid a long technology walkthrough. |
| **147–170** | **77–82** | **PROTECTED DO.** Show a timer or the relevant task slide; circulate without projecting trainer answers. Five work windows below total **23 min**. | Learner completes core expressions, records a trajectory, compares rates and **saves 4–6 interpretation sentences**. Do not replace this interval with instruction. |
| **170–175** | **83–94** | **GATE → DEBRIEF.** First confirm attempts are saved on slide 83. Prioritize slide **85** (starting and first update), **86** (trajectory), **88** (rate table) and **89** (three panels). Slide 84 frames comparison if useful. | Learners compare their *own saved evidence* to references and correct interpretations. **87, 90–94 are optional after-attempt reference**, not must-show slides. |
| **175–180** | **95–98** | **SYNTHESIS / QUICK.** Revisit the six-link chain on 95, ask 96 before displaying 97, then bridge to Session 18 using 98. Slide 99 is a source reference, not a mandatory spoken slide. | Ask one learner to explain why low loss on four synthetic rows is not real-world prediction quality. Close on time. |

**Practical transition rule:** When a block says **GUIDED DO**, a slide sets up the question but the learner performs the paper/NumPy work. When the block says **PROTECTED DO**, the trainer stops leading and assists selectively. Speaker notes add helpful cues; **use the revised slide numbering above** if older numeric references within notes disagree.

## 3. The three short guided checks — exactly what to facilitate

Do not display the corresponding **readout** slide until learners have committed to paper results and a shape/sign prediction. These checks rehearse mathematical ideas already explained; their first-step numbers may be discussed openly **before** the independent exercise.

### Guided Check 1 — Case 3 dot product and prediction (55–76; slides 37 → 38; ~6 min)

**Setup cue:** "Use Case 3: 3 km, 2 items. What do the two features contribute *before* the base time? Then predict the final minutes and the whole-array shape."

1. **Paper, ~2 min:** Learners multiply matching feature and weight entries, sum, then add base 10. Ask them to say why the units become minutes.
2. **Predict and run, ~2 min:** Before execution, each learner writes expected shape for `X @ w + b`. Switch to the learner notebook's **Guided check 1** cell, not Stage 1 TODO.
3. **Readout, ~2 min:** Display slide 38 and compare: `3×4 + 2×2 = 16` weighted minutes; plus 10 gives **26 min**. All four predictions `[16,20,26,30]`, shape **`(4,)`**. An early finisher can check Case 2 = **20 min**.

**Listen for:** "16 is already the prediction" (forgot bias); "eight outputs" or `(4,2)` (used `*`); `(2,3)` feature order; confusing the Case 3 output with the four-case array. **Hint, not answer:** "Where does the base time enter? What operation sums the two contributions into one number per row?" **Move on when:** learners can explain the **meaning** of `(4,)`, not just repeat the tuple.

### Guided Check 2 — signed error and MSE (88–108; slides 46 → 47; ~6–7 min)

**Setup cue:** "We have four predictions and four observed minutes. A signed miss belongs to one order; how can one score compare whole rules?"

1. **Paper, ~3 min:** Use predictions `[16,20,26,30]` and targets `[15,18,23,26]`. Write **prediction minus observed** for each, square, sum, divide by **four**.
2. **Run, ~2 min:** Execute the learner notebook's **Guided check 2** cell and compare errors, squares, average. Prompt: "In what unit is the mean?"
3. **Interpret, ~1–2 min:** Ask for one sentence on what MSE shows and one thing it cannot show; then reveal slide 47.

**Checkpoint:** errors `[+1,+2,+3,+4]` min; squared `[1,4,9,16]` min²; sum 30 min²; **MSE 7.5 min²**. Case 4 contributes most. **Watch for:** averaging signed errors (gives 2.5, not MSE); omitting a square; dividing by 2 or 3; calling 7.5 "minutes late"; using `observed_minutes` as a feature. **Prompt:** "Do opposite signed errors cancel under squaring? What quantity is being averaged?" **Move on when:** students can say this is a **training loss on four invented cases**, not an accuracy percentage or a guarantee about new orders.

### Guided Check 3 — one negative-gradient update (126–142; slides 65 → 66; ~4 min)

**Setup cue:** "At a = 4 min/km, the slope of loss is +15. With α = 0.05, which way should the *shared distance coefficient* move, and by how much?"

1. **Pairs, ~2 min:** Work out `α × gradient`, decide the sign in `a_next = a − αg`, record the new **parameter**, not a changed case distance.
2. **Check, ~1 min:** Run the learner notebook's **Guided check 3** cell to inspect the new MSE.
3. **Readout, ~1 min:** Reveal slide 66: **step = 0.75**, **a = 3.25 min/km**, predictions `[15.25,18.5,23.75,27]` min; **new MSE = 0.46875 min²**.

**Watch for:** adding `αg`, saying `a = 0.75`, changing `X[:,0]`, reversing the error sign or assuming one smaller loss proves convergence. **Prompt:** "Is +15 the downhill direction or the direction in which the loss rises? Which symbol is the parameter?" **Move on when:** learners can say why `a` decreased and what stayed fixed (`b=10`, `c=2`, all X/y values).

## 4. The protected notebook investigation — 23 minutes

**At 142–147, demonstrate navigation, not solutions.** The notebook already supplies the four-row inputs, feature-space plot, matrix demonstrations, three guided checks, `prediction(a)`, `loss(a)`, `plot_trajectory(...)` and `plot_rate_comparison(...)`. The *student* must write the initial predictions/MSE, the gradient expression, the subtractive update, the gradient-descent loop/history and the rates/reset; the prewritten functions **draw** a student-generated history rather than inventing an optimization path.

Use one shared visible timer and the following exact timeboxes. If a group is behind, give a diagnostic nudge and protect a correct update, at least one generated trajectory and an honest saved interpretation. Do **not** move Stage 5 out of the protected window.

| Minute window | Learner-owned work | What the trainer inspects (without filling the TODO) | First safe hint after an attempt |
|---|---|---|---|
| **147–151** / 4 min | **Stage 1.** Inspect `X`, `y`, `w`; fill `initial_prediction` and `initial_mse`. | Predictions contain four results; MSE is the mean of **squared prediction-minus-target errors**; this is **iteration 0**. | "Which operator gives one weighted sum per row? Where is `b` added?" |
| **151–157** / 6 min | **Stage 2.** Complete `gradient(a)` and the one-step update using **α = 0.05**. | Gradient uses distances `X[:,0]` paired with **signed** error; the update subtracts the scaled gradient. A correct first step matches the taught guided check. | "What does a change in `a` multiply for each order? Is the gradient pointing uphill?" |
| **157–163** / 6 min | **Stage 3.** Complete `run_descent` gradient/update statements and append **both** new parameter and new loss on every pass; use supplied trajectory plot. | `a_history` and `loss_history` start with iteration **0 before the loop**. Seven updates produce **eight paired entries**. Plot horizontal axis is **a (min/km)**, not iteration. | "What is the state before the first update? When exactly do you append after calculating the new state?" |
| **163–166** / 3 min | **Stage 4.** Supply `[0.001, 0.05, 0.20]`; reset **each** rate to original `a0=4`; use comparison helper. | Every run shares iteration-0 `a=4`, MSE 7.5 and seven updates. Read printed values and axes: three panels, independent y-scales, high-rate plot logarithmic. | "Does each call start with `a0` or the previous run's last value? Read the y-axis label." |
| **166–170** / 4 min | **Stage 5.** Write and **save 4–6 evidence-based sentences** in the learner notebook. | Names `a` in min/km; explains the positive initial gradient/update direction; quotes old vs first-step MSE; contrasts three rates; states one synthetic-data limitation. | "Which observed result supports your claim? What would this not tell an actual delivery team?" |

**Hint ladder across all stages:** (1) ask learner to name inputs, units, shape and expected result; (2) point to the relevant variable, notebook markdown or expression role; (3) give one procedural nudge **after a genuine attempt**; (4) invite a paper-first computation or peer explanation. Do not paste a completed cell, open the answer notebook on screen, overwrite student code or perform the loop for them. Fast finishers may think about alternative plots or the `0.09` crossing case **only after the core and saved interpretation**, without changing the group's pacing or revealing reference results.

**At 170:** Ask everyone to save their notebook and show/confirm that the interpretation text is no longer the template prompt. Slide **83** stays up until this is done. Learners with device failure should preserve their paper derivation/interpretation, note what they could not execute and then join the debrief; do not describe unexecuted work as a completed code result.

## 5. After saving: five-minute evidence-driven debrief (170–175)

The goal is **one concrete correction to the learner's interpretation**, not a tour of all reference slides. Show only the highest-value slides needed by the room.

| Approx. time | Show | Ask / establish |
|---|---|---|
| **170:00–170:30** | **83** (gate), optionally **84** | "Have you saved your own explanation? Which number or plot will you compare first?" No answer projection until confirmed. |
| **170:30–171:30** | **85** | Check old vs new parameter, gradient direction and MSE: does a disputed result start at a wrong prediction, error or sign? |
| **171:30–172:30** | **86** | Read the **loss-versus-parameter** plot. Iteration numbers label points on the path; the horizontal coordinate is **a**, not iteration. |
| **172:30–173:40** | **88** | Compare same-start, seven-update numerical states for all **three** core rates; ask why the largest rate made the loss grow. |
| **173:40–175:00** | **89** | Read three **loss-versus-iteration** panels with different vertical scales; one is logarithmic. Ask learners to refine one of their written rate descriptions and retain the synthetic-data caveat. |

**If late:** Preserve the save gate; combine slides **85** and **88–89** into a faster result check; skip slide 86 if students already understand the axis distinction. Do not sacrifice the 175–180 synthesis. Slides **87** (full history) and **90–94** (rounding, optional `0.09` crossing, constructed optimum, limitations and misconception repair) are available for after-class review or a question **only after** the attempt. Showing every one is **not** the live requirement.

### Private post-attempt numerical reference — do not project before minute 170

All three rate runs start at `a=4` and MSE `7.5 min²`. Iteration **0** precedes any update; iteration **7** follows seven updates.

| Learning rate `α` | After first update: `a`, MSE | After seven updates: `a`, MSE | Trainer interpretation |
|---|---|---|---|
| **0.001** | `3.985`, `7.2766875` | ~`3.899609`, ~`6.069718` | Very slow progress over seven steps; not a stall caused by a zero gradient. |
| **0.05** | `3.25`, `0.46875` | ~`3.000061`, ~`2.794 × 10⁻⁸` | Rapid approach on this particular loss; `0.00000` at fixed decimals is **not exact zero**. |
| **0.20** | `1.00`, `30.0` | `−125.0`, `122880` | Crosses repeatedly and moves farther away; **diverges**. A negative coefficient here is a numerical failure, not operational advice. |

**Optional after-attempt distinction:** `α=0.09` first lands at `a=2.65`, MSE `0.91875`; subsequent updates cross back and **converge**. Overshoot **is not necessarily divergence**. This manufactured example also has `L(a) = 7.5(a−3)²`, so the known training minimum is `a=3` with loss zero; these are **post-attempt checks**, not the facts to reveal while students are writing their optimization paths. Neither is a universal guarantee for other models or objectives.

## 6. Trainer's rapid mathematical reference

| Question likely to arise | Correct short answer |
|---|---|
| What counts as a feature or target? | `distance_km`, `items` are input features, in that order. `observed_minutes` is **y**, for comparison only. Synthetic cases: `(1,1)→15`, `(2,1)→18`, `(3,2)→23`, `(4,2)→26`. |
| What is the shape and purpose of each object? | `X` `(4,2)` = four orders × two features; `y` `(4,)` = four observed targets; `w=[4,2]` `(2,)` = shared coefficients; `b=10` is a scalar. `X.T` is `(2,4)`. |
| What differs between the two multiplication operators? | `X * w`: broadcast entrywise, **`(4,2)`**, keeps contributions apart. `X @ w`: one weighted sum per row, **`(4,)`**. `X @ W` for `W=[[4,5],[2,2]]` gives `(4,2)` with two illustrative rule columns, **not** a fitted alternative. |
| How is one prediction made? | Case 3: `3×4 + 2×2 = 16` weighted minutes; `+10` gives **26 min**, versus observed **23 min**. Full start `X @ w + b = [16,20,26,30]` min. |
| How is error/loss defined? | Error is always **prediction − observed**: `[1,2,3,4]` min. Squares `[1,4,9,16]` min²; MSE `30/4 = 7.5 min²`. It is not an accuracy percentage. |
| What changes during the optimization? | Only distance coefficient **`a`** in `prediction(a)=10 + a×distance + 2×items`; fixed `b=10`, `c=2`, `X`, `y`. Parameter `a` belongs to the **shared rule**; a distance value belongs to one case. |
| What is the gradient and update? | `g(a)=2 × mean(distance × (prediction(a)−y))`; at `a=4`, `g=+15`. `a_next=a−αg`; with `α=0.05`, `a_next=3.25`, MSE `0.46875 min²`. Positive gradient means **increasing a** is locally uphill; *subtract* it to descend. |
| Which horizontal axis am I looking at? | Feature plot: **distance_km** (x), `items` (y). Loss curve/trajectory: **a (min/km)** (x), training MSE (y). Rate comparison: **iteration index** (x), MSE (y). Always read axis scale and units. |

**Interpretation guardrail:** Training loss is computed on just four constructed observations. Low/zero loss here does **not** establish future prediction quality, statistical confidence, causation or a deployable system. A derivative of zero is a **locally flat slope**, not automatically a general global minimum. A negative gradient is locally downhill but an excessive step can increase loss.

## 7. In-room troubleshooting — diagnose the first wrong thing

When a result differs, compare in this order: **feature/weight order → prediction → signed error → squared loss → gradient factor/sign → update subtraction → iteration-0 history → identical run starts → update count → plot axes/scales**. Find the earliest divergence instead of debugging the final chart first.

| Symptom / mistake | Likely cause | Fast, learner-owned repair cue |
|---|---|---|
| Feature vector appears as `[3,2,23]`. | Target entered as an input feature. | "Which two facts can we know **before** the delivery? When does the observed 23 enter?" Recheck `X` vs `y`. |
| `(4,2) @ (3,)` fails. | Three weight entries for two feature columns. | Compare feature and weight **meanings/counts**; do not pad or reshape to silence the error. Slide 27–28. |
| Code runs but gives four **pairs** rather than four predictions. | Used `X*w` instead of `X@w`. | Ask for shape of each and which operation sums a row; slides 25–26. |
| Case 3 yields **16** instead of **26**. | Omitted base `b`. | "Is 16 the weighted subtotal or the final predicted time?" Slides 33–34. |
| MSE is **2.5**, negative or in minutes. | Averaged signed errors, reversed convention, missed squaring or misread units. | Write one **prediction − y** error and its square; then mean the four squared values. Slides 43–47. |
| `a` increases although initial gradient is positive. | Used `+ αg` or confused uphill gradient with downhill step. | Ask for sign of `g` and why the update uses **minus**. Slides 55–66. |
| First history entry is **3.25** or only seven entries exist. | Iteration 0 was recorded **after** updating, or missing an append. | "What existed before the loop? How many states follow seven updates?" Eight values expected. |
| Rate runs show different iteration-0 values. | Runs chained from previous final `a`. | Recheck explicit `start_a=a0`; each starts at **4**. Slide 81. |
| Loss curve is mistaken for iteration plot. | Did not inspect x-axis: `a` vs step number. | Compare slides 86 and 89; ask for horizontal **unit** and what each point represents. |
| Fast/diverging line hides others; rates look alike. | Shared y-scale, or logarithmic axis misread. | Use supplied separate rate panels; high-rate panel uses a **log y-axis**. Compare numeric table, not only line shape. |
| `NotImplementedError` in a TODO cell. | Learner has not replaced an intended placeholder; or ran later cell before completing previous one. | Read the TODO message, find the placeholder, complete it; restart and rerun setup cells if variables vanished. The error is **expected until completed**. |
| `NameError` after notebook restart. | Setup or helper cell not rerun. | Rerun from the first import/data cell through the current task in order; do not blindly execute incomplete future TODOs. |
| Plot missing, blank or mislabeled. | Kernel/cell order issue, failed `run_descent`, missing history entries or confusing axes. | Check `a_history`/`loss_history` length and numeric values **before** rerunning plotting helper. Confirm the plot cell executed and output was displayed. |
| "The model is accurate/ready to deploy." | Confused small synthetic training MSE with quality on unseen examples. | "Which four rows were used to change a? What new data were tested?" None. This session is mathematical intuition. |

**Device/network fallback:** Do not spend the 23-minute practical repairing one machine while the room waits. Ask the learner to work on paper with the table and taught expressions, document one valid update plus an evidence-based prediction of rate behavior, and save/retain that work. Show actual reference graphs only at the post-attempt gate. If Colab disconnects, the new runtime may have lost variables; an existing notebook file and saved written reasoning are still valuable.

## 8. Timing decisions and final close

**If the class is five minutes behind before the break:** cut repeated shape predictions and spend less time on the second `X @ W` rule or transpose; **do not** squeeze Guided Check 1 or the 12-minute break.

**If the class is five minutes behind at the gradient block:** keep one graph-based slope explanation, the `g=+15` reasoning and the `a−αg` sign; reduce repeated generic bowls and optional rate speculation. Guided Check 3 still happens.

**If learner access takes longer at 142:** use the paper fallback for affected learners; the whole group still starts protected work at 147. Do not shift the save gate to consume the final synthesis.

**If the practical is uneven:** use visible stage checkpoints; help with interpretation without revealing missing code. A correct gradient/update, one authentic trajectory (or a documented paper fallback) and saved reasoning are more valuable than uncompleted optional graphs.

**If debrief time is short:** show the comparison evidence, not every reference slide. The five minutes after the practical are for validation and interpretation; the final five are for consolidation and a bridge, not first exposure to essential mathematics.

**Exit prompt (175–180, slides 95–98):** "Use one sentence each: What describes an order? What makes a predicted number? What summarizes the errors? What does the gradient tell us, and what changes at each step? What does a near-zero toy training loss *not* tell us?" Accept ordinary language before algebra. Close with the bridge to Session 18, which introduces the wider ML workflow and appropriate evaluation. Regression methods, nearest-neighbour/clustering methods and neural-network backpropagation are later lessons, **not Session 17 extensions**.

### Trainer reference links

- [NumPy `matmul` / `@`: matrix-product semantics and shape errors](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html) and [NumPy broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting)
- [Matplotlib logarithmic scales and their interpretation](https://matplotlib.org/stable/gallery/scales/log_demo.html)
- [Google Colab FAQ: import/upload notebooks and execution/runtime behavior](https://research.google.com/colaboratory/faq.html)

*Software interfaces and account requirements can vary. Confirm the actual classroom environment before delivery; these references do not replace a clean local run.*
