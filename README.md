# Final Inspection Bottleneck Copilot v0.2

## Project Overview

This project is a beginner-friendly PCB manufacturing data analysis portfolio project.

The goal is to use Python, pandas, and AI-assisted development to analyze synthetic PCB final inspection data and identify possible bottleneck signals.

This project uses 100% synthetic data. No company data or confidential manufacturing data is used.

## Background

In PCB manufacturing, final inspection and AOI data can be used to monitor:

- Lot-level defect rate
- Station-level defect trend
- Shift-level risk
- Delay hours
- Potential bottleneck station

This v0.2 project focuses on a simple but explainable workflow:

Synthetic lot data → pandas DataFrame → defect rate calculation → station / shift summary → chart → bottleneck candidate.

## Dataset

The synthetic dataset includes the following fields:

- lot_id
- station
- shift
- input_qty
- defect_qty
- defect_type
- delay_hours
- defect_rate
- defect_rate_percent
- defect_rate_label

## Formula

The basic defect rate formula is:

```python
defect_rate = defect_qty / input_qty
defect_rate_percent = defect_rate * 100
```
## Chart Outputs

This project generates chart outputs under the `reports/` folder:

- `delay_hours_by_station.png`: compares total delay hours by station as a bottleneck proxy.
- `defect_type_ranking.png`: ranks defect types by total defect quantity.
- `station_defect_rate_chart.png`: compares station-level defect rates.

All charts are generated from synthetic mock final inspection data only. No company, customer, product, yield, capacity, or internal production data is used.
