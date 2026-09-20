# Final Inspection Bottleneck Copilot v0.2

A small, reproducible manufacturing analytics portfolio project built with Python, pandas, matplotlib, and 100% synthetic inspection data.

The project turns lot-level inspection records into station/shift summaries, defect-rate metrics, bottleneck signals, and simple charts that can be reviewed without access to any company data.

## What This Project Demonstrates

- Loading and validating structured manufacturing data with pandas
- Calculating weighted defect rates correctly from quantity totals
- Comparing station- and shift-level performance
- Using `delay_hours` as a simple bottleneck proxy
- Ranking defect categories
- Generating reproducible CSV/text summaries and charts
- Keeping public portfolio data synthetic and free of confidential information

## Workflow

```text
Synthetic inspection data
        ↓
Schema / value validation
        ↓
Station + shift aggregation
        ↓
Defect-rate calculation
        ↓
Bottleneck proxy + defect ranking
        ↓
Text summary + charts
```

## Included Synthetic Example

The sample dataset uses two example inspection stations (`AOI` and `Final Inspection`) and Day/Night shifts.

From the included synthetic dataset:

- AOI defect rate: **5.29%**
- Final Inspection defect rate: **7.00%**
- Day-shift defect rate: **5.11%**
- Night-shift defect rate: **7.56%**
- Final Inspection also has the highest total synthetic `delay_hours` value in this example

These values are demonstration outputs only. They are not real factory benchmarks or production results.

## Repository Structure

```text
final-inspection-bottleneck-copilot/
├─ analysis.ipynb
├─ requirements.txt
├─ mock_data/
│  ├─ synthetic_defect_log.csv
│  ├─ station_summary.csv
│  └─ shift_summary.csv
├─ scripts/
│  ├─ analyze_bottlenecks.py
│  └─ generate_charts.py
├─ reports/
│  ├─ analysis_summary.txt
│  ├─ delay_hours_by_station.png
│  ├─ defect_type_ranking.png
│  └─ station_defect_rate_chart.png
└─ docs/
```

## Quick Start

```bash
python -m venv .venv
```

Activate the environment, then install dependencies:

```bash
pip install -r requirements.txt
```

Run the text analysis:

```bash
python scripts/analyze_bottlenecks.py
```

Generate charts:

```bash
python scripts/generate_charts.py
```

## Core Formula

```python
defect_rate = defect_qty / input_qty
```

For station/shift summaries, the rate is recalculated from aggregated quantities rather than averaging row-level percentages:

```python
summary_defect_rate = sum(defect_qty) / sum(input_qty)
```

## Data Safety

This repository uses **synthetic/mock data only**. It does not contain:

- company or customer data
- product names or part numbers
- real yield, capacity, or production records
- internal process parameters
- API keys, tokens, passwords, or credentials

## Limitations

This is a portfolio-scale analytics prototype, not a production monitoring system or predictive AI model.

- The dataset is intentionally small and synthetic.
- `delay_hours` is used only as a simple bottleneck proxy.
- No causal inference or production-grade alerting is implemented.
- The results should not be interpreted as real manufacturing performance.

## Development Note

AI tools were used as coding/review aids during development. The analysis itself is deterministic and inspectable in the repository scripts and notebook.
