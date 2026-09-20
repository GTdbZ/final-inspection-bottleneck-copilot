# Agent Guide

This repository is a portfolio-oriented analytics project for synthetic manufacturing inspection and bottleneck analysis.

## Scope

The current version focuses on:

- synthetic inspection data
- example station and shift comparisons
- defect-type ranking
- delay analysis using `delay_hours`
- simple reproducible charts and text summaries

## Agent Rules

Any AI assistant or automation tool working on this repository must:

1. Use synthetic or mock data only.
2. Never add company, customer, product, part-number, real yield/capacity, or internal production data.
3. Never add API keys, passwords, tokens, credentials, or private configuration files.
4. Avoid local personal paths in committed files.
5. Keep changes small, reviewable, and reproducible.
6. Preserve the generic manufacturing positioning unless the owner explicitly changes the project scope.

## Required Data Columns

- lot_id
- station
- shift
- input_qty
- defect_qty
- defect_type
- delay_hours

## Example Station Values

- AOI
- Final Inspection

## Safe Development Notes

All charts, reports, and analysis outputs must be reproducible from synthetic/mock data stored in this repository. The repository is intended for public portfolio demonstration and should remain safe to publish.
