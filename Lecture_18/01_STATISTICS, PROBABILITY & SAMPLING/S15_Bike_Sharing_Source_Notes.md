# Bike Sharing daily data: source and field notes

`day.csv` contains daily rental counts for the Capital Bikeshare system in Washington, D.C., from **2011-01-01 through 2012-12-31**. One row is one observed calendar day. The 731 days in this file can serve as a finite historical frame for summaries and classroom sampling. They do not represent all future days or other bike-share systems.

## Source, attribution and reuse

Fanaee-T, H. (2013). *Bike Sharing* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5W894

- Dataset page: https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset
- Original distribution downloaded **2026-10-21**: https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip ; the file supplied here is its `day.csv` entry, copied byte for byte. The archive also contains `Readme.txt` and `hour.csv`; neither is needed to load this daily package. The UCI page's 17,389 instance count describes the broader listing, not the 731-row daily file.
- UCI lists the dataset under **Creative Commons Attribution 4.0 International (CC BY 4.0)**: https://creativecommons.org/licenses/by/4.0/ . Reuse requires appropriate credit, a license link and an indication of changes. **No changes were made to `day.csv`.**
- The archive's `Readme.txt` also asks that publications cite Fanaee-T, H., & Gama, J. (2013), “Event labeling combining ensemble detectors and background knowledge,” *Progress in Artificial Intelligence*, https://doi.org/10.1007/s13748-013-0040-3 . It describes the underlying rental log as Capital Bikeshare data and the weather information as drawn from FreeMeteo.
- SHA-256 of the supplied `day.csv`: `a6bcf826782d3c0fbfdcbeead17cd0884185a0dafe8ff10cd48a874ee7ba18be` (57,569 bytes). The downloaded ZIP's SHA-256 was `b70182d0d0508e9abbb79306ce5c0cec34869000f8220175ac83d11dbe845401`. These hashes identify the distribution checked on the retrieval date.

## Fields and codes

The CSV preserves all 16 source columns. Integer codes for categories should be treated as labels, not measured quantities.

| Field | Meaning and type |
| --- | --- |
| `instant` | Sequential record index, 1–731; identifier, not a ride count. |
| `dteday` | Calendar date (`YYYY-MM-DD`); one-day observation context. |
| `season` | Coded seasonal category. The **current UCI dataset page** gives `1` winter, `2` spring, `3` summer, `4` fall. See the source-document conflict below. |
| `yr` | Coded year: `0` = 2011, `1` = 2012. |
| `mnth` | Calendar month code `1`–`12`. |
| `holiday` | Binary holiday indicator: `1` = holiday, `0` = not marked as a holiday. |
| `weekday` | Day-of-week category `0`–`6`. Comparing its values with `dteday` confirms `0` = Sunday through `6` = Saturday. |
| `workingday` | Binary category: `1` if the day is neither a weekend nor a holiday; otherwise `0`. |
| `weathersit` | Coded weather-condition category. Source meanings are listed below. |
| `temp` | Normalized temperature-related measurement, stored as a decimal, **not raw °C**. The source documents conflict on its exact conversion; see below. |
| `atemp` | Normalized perceived/feeling temperature, **not raw °C**. Conversion documentation also differs; see below. |
| `hum` | Normalized humidity: source documents say divided by 100. Stored values are proportions, **not unscaled percentages**. Multiplying by 100 gives the source's percentage scale. |
| `windspeed` | Normalized wind speed: source documents say divided by 67, not a raw speed with a stated unit in this CSV. |
| `casual` | Daily count of rentals by casual users; nonnegative integer. |
| `registered` | Daily count of rentals by registered users; nonnegative integer. |
| `cnt` | Total daily rental count; nonnegative integer. In every row, `cnt = casual + registered`. |

UCI's `weathersit` category descriptions are:

| Code | Source-listed conditions |
| --- | --- |
| `1` | Clear; Few clouds; Partly cloudy (listed twice in UCI's text). |
| `2` | Mist + Cloudy; Mist + Broken clouds; Mist + Few clouds; Mist. |
| `3` | Light Snow; Light Rain + Thunderstorm + Scattered clouds; Light Rain + Scattered clouds. |
| `4` | Heavy Rain + “Ice Pallets” + Thunderstorm + Mist; Snow + Fog. “Ice Pallets” is the source's wording. |

Code `4` has **no observations** in this daily file. These codes are categories, not a numerical weather scale.

**Source-document differences.** The ZIP's original `Readme.txt` instead calls seasons `1` “springer,” `2` summer, `3` fall, `4` winter. The current UCI page gives the mapping in the table above. The observed switches to code `2` on March 21, `3` on June 21 and `4` on September 23 in both years, supporting the current page's Northern Hemisphere mapping, but the conflicting Readme labels remain part of the source record. Keep the numeric source codes in calculations and state the chosen label convention when displaying seasons.

For `temp`, the ZIP Readme says values were divided by 41, while the current UCI page describes min–max normalization using −8°C and +39°C and qualifies that description as “only in hourly scale.” It similarly differs on the `atemp` conversion. Because this is the **daily** file and the documents disagree, do not convert its `temp` or `atemp` values back into claimed exact physical temperatures. Use them as normalized measurements. The `hum` scaling statement is consistent across the two source documents.

## Checks on the supplied file

- **731 rows × 16 columns**, with all 731 calendar dates from 2011-01-01 through 2012-12-31 present once, in date order. No invalid dates, duplicate dates, duplicate rows or calendar gaps were found.
- No missing or blank cells, nonfinite numeric values, noninteger values in the coded/count fields, or negative values in `casual`, `registered` or `cnt` were found. `cnt` ranges from 22 to 8,714 rentals.
- `cnt = casual + registered` holds on all 731 rows. `instant` runs from 1 through 731. The `yr`, `mnth`, `weekday` and `workingday` codes agree with the dates and holiday flags on every row.
- Observed domains: `season` = {1, 2, 3, 4}; `workingday` = {0, 1}; `weathersit` = {1, 2, 3}. All stored `temp`, `atemp`, `hum` and `windspeed` values fall within 0–1. The supplied bytes match the `day.csv` entry in the downloaded UCI ZIP.
- A local Pandas read and strict `YYYY-MM-DD` date parse succeeded. Pandas loaded 11 integer columns, four decimal columns and one parsed date column. No cleaning, recoding, row removal or other transformation was applied.

## Local use

Place `day.csv` beside the notebook and open the notebook with that folder as its working directory:

```python
import pandas as pd

days = pd.read_csv("day.csv", parse_dates=["dteday"])
```

This reads the bundled local file without internet access. For a different notebook working directory, adjust the relative path to point to this same unchanged CSV.
