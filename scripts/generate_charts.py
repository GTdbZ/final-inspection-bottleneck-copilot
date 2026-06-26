from pathlib import Path
import shutil

import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT / "reports"
DATA_DIR = ROOT / "mock_data"
REPORTS_DIR.mkdir(exist_ok=True)

log_path = DATA_DIR / "synthetic_defect_log.csv"
station_summary_path = DATA_DIR / "station_summary.csv"

log_df = pd.read_csv(log_path)
station_df = pd.read_csv(station_summary_path)


def save_delay_hours_by_station():
    chart_df = station_df.sort_values("delay_hours", ascending=False)

    plt.figure(figsize=(8, 5))
    plt.bar(chart_df["station"], chart_df["delay_hours"])
    plt.title("Delay Hours by Station")
    plt.xlabel("Station")
    plt.ylabel("Delay Hours")
    plt.tight_layout()

    output_path = REPORTS_DIR / "delay_hours_by_station.png"
    plt.savefig(output_path, dpi=150)
    plt.close()

    print(f"Saved: {output_path}")


def save_defect_type_ranking():
    chart_df = (
        log_df.groupby("defect_type", as_index=False)["defect_qty"]
        .sum()
        .sort_values("defect_qty", ascending=False)
    )

    plt.figure(figsize=(8, 5))
    plt.bar(chart_df["defect_type"], chart_df["defect_qty"])
    plt.title("Defect Type Ranking")
    plt.xlabel("Defect Type")
    plt.ylabel("Defect Quantity")
    plt.tight_layout()

    output_path = REPORTS_DIR / "defect_type_ranking.png"
    plt.savefig(output_path, dpi=150)
    plt.close()

    print(f"Saved: {output_path}")


def copy_existing_station_chart_if_available():
    source_path = ROOT / "station_defect_rate_chart.png"
    target_path = REPORTS_DIR / "station_defect_rate_chart.png"

    if source_path.exists():
        shutil.copy2(source_path, target_path)
        print(f"Copied existing chart: {target_path}")


if __name__ == "__main__":
    save_delay_hours_by_station()
    save_defect_type_ranking()
    copy_existing_station_chart_if_available()

    print("\nChart generation complete.")
    print("Data safety note: all charts are generated from synthetic mock data only.")
