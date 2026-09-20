# Data Schema

This document describes the synthetic data schema used by the Final Inspection Bottleneck Copilot portfolio project.

## Dataset Purpose

The dataset demonstrates a small manufacturing inspection analytics workflow with Python and pandas. It is intentionally synthetic and does not represent any company, customer, product, or real production process.

## Columns

| Column | Description |
|---|---|
| lot_id | Synthetic lot identifier |
| station | Example inspection station |
| shift | Example production/inspection shift |
| input_qty | Synthetic inspected/input quantity for the lot |
| defect_qty | Synthetic defect quantity for the lot |
| defect_type | Generic synthetic defect category |
| delay_hours | Synthetic delay duration used as a bottleneck proxy |
| defect_rate | `defect_qty / input_qty` |
| defect_rate_percent | Defect rate expressed as a percentage |
| defect_rate_label | Human-readable percentage label |

## Example Station Values

| Value | Description |
|---|---|
| AOI | Example automated optical inspection station |
| Final Inspection | Example final inspection station |

## Defect Type Examples

The synthetic dataset includes generic labels such as:

- scratch
- dent
- open
- short

These labels are demonstration values only and do not represent company-specific defect codes or real quality records.

## Validation Expectations

- `input_qty` must be greater than 0.
- `defect_qty` must be non-negative and cannot exceed `input_qty`.
- `delay_hours` must be non-negative.
- Required columns must be present before analysis.

## Safety Statement

This project uses synthetic/mock data only. It does not contain company data, customer names, product names, part numbers, real yield/capacity data, internal production records, API keys, passwords, tokens, or credentials.
