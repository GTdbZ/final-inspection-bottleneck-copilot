# Data Schema

This document describes the current synthetic data schema used by the Final Inspection Bottleneck Copilot portfolio project.

## Dataset Purpose

The dataset is designed to demonstrate how Python and pandas can be used to analyze synthetic PCB inspection bottlenecks.

The data is not real manufacturing data. It is only mock data for portfolio demonstration.

## Columns

| Column | Description |
|---|---|
| lot_id | Synthetic lot identifier for mock analysis |
| station | Inspection station name |
| defect_type | Synthetic defect category |
| inspected_qty | Number of inspected units in the mock dataset |
| defect_qty | Number of defective units in the mock dataset |
| delay_hours | Synthetic delay duration used as a bottleneck proxy |

## Station Values

| Value | Description |
|---|---|
| AOI | Automated optical inspection station in the mock workflow |
| Final Inspection | Final inspection station in the mock workflow |

## Defect Type Examples

The dataset may include synthetic defect categories such as:

- scratch
- dent
- open
- short

These defect categories are generic mock labels and do not represent any company-specific process, customer issue, product issue, or internal manufacturing record.

## Safety Statement

This project uses synthetic or mock data only.

It does not contain:

- company data
- customer names
- product names
- part numbers
- real yield data
- real capacity data
- internal production data
- API keys
- passwords
- tokens
- credentials
