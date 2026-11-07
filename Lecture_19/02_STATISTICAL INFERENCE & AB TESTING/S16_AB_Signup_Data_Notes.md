# S16 synthetic A/B signup experiment: data notes

## Scope and fields

This CSV is a wholly synthetic teaching simulation of a fictional product team's signup-page experiment. One row represents **one eligible unique visitor assigned once** to the current page (**A**, control) or simplified page (**B**, treatment). The primary outcome is the fraction of assigned visitors who sign up. Nonconverters remain in the denominator. The file contains no real visitor, website, or operational records.

The 14 consecutive assignment dates are **2026-09-01 through 2026-09-14**, inclusive. `converted = 1` means a signup within the assignment date or the following six calendar days, a seven-calendar-day measurement window per visitor. The final synthetic outcome window ends **2026-09-20**. No signup timestamp or conversion date is stored. Dates supply context; the analysis unit is the visitor, not a day.

| Field | Type and meaning |
| --- | --- |
| `visitor_id` | Unique, non-identifying synthetic token (`V` plus 16 uppercase hexadecimal characters); one row per assigned visitor. |
| `variant` | Exactly `A` or `B`, as defined above. |
| `converted` | Integer `1` for a signup in the defined window; integer `0` otherwise. |
| `assignment_date` | ISO `YYYY-MM-DD` calendar date of the fictional first assignment and page exposure. |

CSV encoding is UTF-8 without a byte-order mark, with a header and no exported index. A local `pandas.read_csv("S16_AB_Signup_Experiment.csv")` reads it without a login, download, or network call.

## Reproduction and provenance

Run `python S16_AB_Signup_Generate.py` from this folder (Python 3.8+; standard library only) to recreate the CSV beside the script. The public deterministic seed is `S16-AB-signup-2026-v1`. SHA-256 with separate labels creates opaque IDs, spreads dates across the 14-day window, selects the fixed number of converters within each arm, and interleaves output rows. The script fixes 5,000 assignments per arm and exactly 600 A and 675 B conversions. These quotas are teaching-design inputs, not estimates from real traffic. The synthetic equal allocation does not establish that any real randomization or logging process worked correctly.

The records were generated from scratch; no personal information or third-party dataset was used. No external data license applies to the CSV. It may be reused for the course's teaching materials with its synthetic status retained.

**CSV SHA-256:** `c8ce3aaff3a6eb3909b4452feb66bede9ff65a2da7017bc7dcf90e1628ea52fb`

## Checks on the saved CSV

An independent full-file CSV read found **10,000 rows**, **10,000 unique nonblank IDs**, the exact four-column schema, no missing or invalid values, and all 14 valid dates in both arms. Every visitor appears once. Per-arm daily assignment counts range from **325 to 393**; ID, arm, and outcome records are interleaved rather than grouped into blocks. A separate pandas 3.0.1 `read_csv` check reproduced the 10,000 × 4 shape and all four outcome counts, parsed `converted` as integer, and found no nulls or index column. A pandas read/write/read round-trip preserved every row, column, and data type.

| Arm | Assigned visitors | Converted | Did not convert | Conversion rate |
| --- | ---: | ---: | ---: | ---: |
| A | 5,000 | 600 | 4,400 | 12.0% |
| B | 5,000 | 675 | 4,325 | 13.5% |
| Total | 10,000 | 1,275 | 8,725 | 12.75% |

Computed from these saved rows, **B − A = +1.5 percentage points**. Relative lift is **+12.5%**, using A's 12.0% rate as its denominator. The observed table in `[[A converted, A not converted], [B converted, B not converted]]` order is `[[600, 4400], [675, 4325]]`.

For later notebook reconciliation, SciPy 1.14.1 `chi2_contingency(observed, correction=False)` returned Pearson χ² = **5.0564638463**, df = **1**, p = **0.0245342485**. Its null-expected converted count is **637.5 in each arm** (and 4,362.5 nonconverters in each arm). The 95% **Newcombe** interval for independent proportions, with **B first and A second**, was independently calculated from Wilson limits as **+0.192359 to +2.808042 percentage points** for B − A. This uses the Newcombe construction published in the statsmodels source; it is not a Wald interval. A direct `statsmodels` function call was unavailable in the validation environment because that package was not installed. The interval should be called again with `method="newcomb", compare="diff"` when the later notebook's environment is established.

The fixed quotas and method checks make the file internally consistent for teaching. They do not verify real assignment, exposure, instrumented signups, or a real-world causal effect. The results section above is an integrity reference; when using the CSV in class, let learners state the metric and decision rules before showing the aggregate outcomes.

## Technical references consulted

- [SciPy `chi2_contingency` documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.contingency.chi2_contingency.html), accessed 2026-10-23. Documents Pearson's default statistic and the `correction=False` choice for a 2 × 2 table.
- [statsmodels `confint_proportions_2indep` documentation](https://www.statsmodels.org/stable/generated/statsmodels.stats.proportion.confint_proportions_2indep.html) and [published method source](https://www.statsmodels.org/stable/_modules/statsmodels/stats/proportion.html), accessed 2026-10-23. Document the `p1 − p2` sign for `compare="diff"` and the Wilson-based Newcombe construction.
