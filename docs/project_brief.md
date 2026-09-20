# Project Brief

## Project Name

Final Inspection Bottleneck Copilot

## Goal

Build a small, explainable manufacturing analytics workflow that converts synthetic inspection records into station/shift summaries, defect-rate metrics, bottleneck signals, and reproducible visual outputs.

## Current Scope

- Read synthetic inspection data
- Validate required columns and basic quantity constraints
- Calculate weighted defect rates
- Compare example inspection stations
- Compare Day/Night shifts
- Rank synthetic defect categories
- Use `delay_hours` as a simple bottleneck proxy
- Generate text and chart outputs for portfolio review

## Outputs

The project generates:

- station-level defect-rate comparison
- shift-level defect-rate comparison in the analysis summary
- defect-type ranking
- delay-hours comparison by station
- reproducible chart files under `reports/`

## Data Safety

This project is designed for public portfolio use and uses synthetic/mock data only. No company, customer, product, real yield/capacity, internal production, or credential data should be added.

## Portfolio Positioning

This is a compact manufacturing analytics project focused on explainability, reproducibility, data safety, and clear engineering trade-offs. It is intentionally kept generic so the workflow can be discussed across manufacturing contexts rather than being tied to one specific factory or process.
