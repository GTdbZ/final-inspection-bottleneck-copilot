# Project Brief: Final Inspection Bottleneck Copilot

## Overview
In high-volume manufacturing environments (e.g., PCB assembly, semiconductor packaging), the final inspection phase is critical for quality control. However, final inspection can easily become a bottleneck due to uneven arrival rates, varying inspection times, operator scheduling, or high rework rates.

The **Final Inspection Bottleneck Copilot** is a manufacturing analytics assistant designed to process inspection records, highlight bottlenecks, identify defect trends, analyze queue/waiting times, and suggest corrective actions for line supervisors.

## Key Objectives
1. **Identify Bottlenecks:** Analyze average wait times (`wait_time_min`) across different inspection stations (`FI-AOI`, `FI-VI`, `FI-Packing`, `FI-Recheck`) to pinpoint where delays accumulate.
2. **Detect Defect Trends:** Track defect occurrences (`defect_type`) to help quality engineers identify recurring process failures (e.g., contamination, open/shorts).
3. **Optimize Rework Cycles:** Evaluate how rework rates (`rework_flag`) affect overall queueing times and throughput.
4. **Actionable Insights:** Generate automatic recommendations (e.g., reallocating operators, adjusting machine calibration) based on thresholds.

## Scope & Implementation
- **Mock Data Platform:** Built entirely on synthetic data to simulate real production runs without exposing proprietary manufacturing information.
- **Analytics Engine:** Intended to run locally using standard Python libraries (`pandas`, `matplotlib`, `seaborn`) or lightweight notebook interfaces.
