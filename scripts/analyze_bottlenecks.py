#!/usr/bin/env python3
"""
Final Inspection Bottleneck Copilot - Initial Analysis Script
Analyzes synthetic final inspection records to locate bottleneck stations and defect patterns.
"""

import os
import sys

# 1. Error handling: Check for pandas
try:
    import pandas as pd
except ImportError:
    print("-" * 60)
    print("Error: The 'pandas' package is not installed.")
    print("Please install pandas to run this analysis by running:")
    print("  pip install pandas")
    print("-" * 60)
    sys.exit(1)

def main():
    # 2. Error handling: Check if the CSV file exists
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.normpath(os.path.join(script_dir, '..', 'mock_data', 'final_inspection_sample.csv'))

    if not os.path.exists(csv_path):
        print(f"Error: The target CSV data file was not found at: {csv_path}")
        print("Please ensure the synthetic CSV mock data is placed in the mock_data/ directory.")
        sys.exit(1)

    # Load dataset
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        sys.exit(1)

    # 3. Error handling: Check for required columns
    required_columns = {'lot_id', 'date', 'station', 'wait_time_min', 'defect_type', 'operator_group', 'rework_flag'}
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        print(f"Error: The dataset at {csv_path} is missing required columns:")
        for col in sorted(missing_columns):
            print(f"  - {col}")
        sys.exit(1)

    print("=" * 60)
    print(" FINAL INSPECTION BOTTLENECK COPILOT - DATA ANALYSIS REPORT")
    print("=" * 60)
    print(f"Dataset path: {csv_path}")
    print(f"Total records analyzed: {len(df)}\n")

    # 1. Average wait_time_min by station, sorted descending
    print("1. Average Wait Time by Station (Minutes)")
    print("-" * 42)
    avg_wait = df.groupby('station')['wait_time_min'].mean().sort_values(ascending=False)
    for station, time in avg_wait.items():
        print(f"  {station:<15} : {time:>6.1f} min")
    print()

    # 2. Top defect_type counts, excluding blank values
    print("2. Top Defect Types (Excluding Passes)")
    print("-" * 42)
    # Exclude nulls/NaNs and strings representing 'None' or empty
    defects = df['defect_type'].dropna()
    defects = defects[defects.astype(str).str.strip().str.lower().replace({'none': '', 'nan': ''}) != '']
    defect_counts = defects.value_counts()
    if not defect_counts.empty:
        for defect, count in defect_counts.items():
            print(f"  {defect:<15} : {count:>5} occurrences")
    else:
        print("  No defects recorded.")
    print()

    # 3. Rework rate by station
    print("3. Rework Rate by Station")
    print("-" * 42)
    rework_rate = df.groupby('station')['rework_flag'].mean().sort_values(ascending=False)
    for station, rate in rework_rate.items():
        print(f"  {station:<15} : {rate:>6.1%} rework rate")
    print()

    # 4. Station with highest average wait time
    highest_wait_station = avg_wait.index[0]
    highest_wait_time = avg_wait.iloc[0]
    print("4. Maximum Bottleneck Station")
    print("-" * 42)
    print(f"  Station '{highest_wait_station}' has the highest average queue delay of {highest_wait_time:.1f} minutes.\n")

    # 5. Recommendation based on synthetic mock data
    print("5. Copilot Recommendations")
    print("-" * 42)
    print(f"  * BOTTLENECK ALERT: [{highest_wait_station}] is the primary queue bottleneck with {highest_wait_time:.1f} min avg wait time.")
    
    # Custom rule-based tips based on the synthetic data values
    if highest_wait_station == 'FI-Recheck':
        print("    Recommendation: FI-Recheck processes rework loops. High queue delays here point to either")
        print("    operator capacity constraints in re-inspection or prolonged diagnostic/rework processing.")
        print("    Action: Allocate additional Group-B/C operators to FI-Recheck to resolve the backlog.")
    elif highest_wait_station == 'FI-AOI':
        print("    Recommendation: FI-AOI is automated optical inspection. Excessive wait times indicate automated")
        print("    machine queues are backlogged, possibly due to false-alarm rate spikes or lot batching.")
        print("    Action: Run calibration checks on AOI sensors to reduce false calls.")
    else:
        print("    Recommendation: Review resource allocation and queue patterns at the bottleneck station.")
        print("    Action: Adjust shifts/operator balance.")

    # Defect specific recommendation
    if not defect_counts.empty:
        top_defect = defect_counts.index[0]
        print(f"  * QUALITY INSIGHT: '{top_defect}' is the most frequent defect ({defect_counts.iloc[0]} occurrences).")
        if top_defect in ['scratch', 'cosmetic_ng']:
            print("    Action: Inspect handling trays and mechanical conveyor belts for abrasion surfaces.")
        elif top_defect in ['contamination']:
            print("    Action: Check cleanroom filters, air showers, and worker gowning compliance.")
        elif top_defect in ['open_short']:
            print("    Action: Verify solder paste deposition parameters and stencil alignment.")
        elif top_defect in ['label_error']:
            print("    Action: Inspect printing/labeling machine alignment and barcode scanners.")
        elif top_defect in ['dimension_ng']:
            print("    Action: Recalibrate pick-and-place components or inspection camera offsets.")
            
    print("=" * 60)

if __name__ == '__main__':
    main()
