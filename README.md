# Final Inspection Bottleneck Copilot

A Python-based manufacturing analytics demo for identifying bottlenecks in final inspection.

## What it does

This project analyzes mock final inspection data and generates:

- Average wait time by station
- Top defect types excluding pass records
- Rework rate by station
- Maximum bottleneck station
- Copilot-style operational recommendations

## Sample Result

The current mock dataset shows that FI-Recheck is the primary bottleneck, with an average queue delay of 80.0 minutes.

The most frequent defect type is scratch, suggesting a need to inspect handling trays and mechanical conveyor belts for abrasion surfaces.

## Why this project matters

In manufacturing operations, final inspection bottlenecks can delay shipment, increase WIP, and hide repeated quality issues.

This project demonstrates how Python can be used to turn inspection records into practical operational insights.

## Data Safety

This project uses mock data only.

No company confidential data is used.
