# Agent Guide

This project is a portfolio-oriented analysis copilot for synthetic PCB final inspection bottleneck analysis.

## Scope

The current project version focuses on:

- Synthetic PCB inspection data
- AOI and Final Inspection station comparison
- Defect type ranking
- Delay analysis using delay_hours
- Simple reproducible charts for portfolio demonstration

## Agent Rules

Any AI assistant or automation tool working on this repository must follow these rules:

1. Use synthetic or mock data only.
2. Do not use company data.
3. Do not use customer names.
4. Do not use product names or part numbers.
5. Do not use real yield data.
6. Do not use real capacity data.
7. Do not use internal production data.
8. Do not use API keys, passwords, tokens, credentials, or private configuration files.
9. Do not reference local personal paths.
10. Keep changes small, reviewable, and aligned with the current synthetic data schema.

## Current Data Columns

The current synthetic dataset is expected to include:

- lot_id
- station
- defect_type
- inspected_qty
- defect_qty
- delay_hours

## Current Station Values

The current station values are:

- AOI
- Final Inspection

## Safe Development Notes

This repository is intended for public portfolio demonstration.

All charts, reports, and analysis outputs must be reproducible from synthetic or mock data stored in this repository. No confidential manufacturing information should be added.
