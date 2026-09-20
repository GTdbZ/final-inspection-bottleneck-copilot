from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT_DIR / "reports"
MOCK_DATA_DIR = ROOT_DIR / "mock_data"
REPORTS_DIR.mkdir(exist_ok=True)

STATION_ORDER = ["AOI", "Final Inspection"]
REQUIRED_COLUMNS = {
    "station",
    "input_qty",
    "defect_qty",
    "defect_type",
    "delay_hours",
}


def load_defect_log() -> pd.DataFrame:
    path = MOCK_DATA_DIR / "synthetic_defect_log.csv"
    if not path.exists():
        raise FileNotFoundError(f"Cannot find required CSV file: {path.name}")

    df = pd.read_csv(path)
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    return df


def build_station_summary(defect_log: pd.DataFrame) -> pd.DataFrame:
    station_summary = (
        defect_log.groupby("station", as_index=False)
        .agg(
            input_qty=("input_qty", "sum"),
            defect_qty=("defect_qty", "sum"),
            delay_hours=("delay_hours", "sum"),
        )
    )
    station_summary["defect_rate_percent"] = (
        station_summary["defect_qty"] / station_summary["input_qty"] * 100
    )

    existing = list(station_summary["station"].dropna().unique())
    ordered_categories = [s for s in STATION_ORDER if s in existing]
    ordered_categories += [s for s in existing if s not in ordered_categories]
    station_summary["station"] = pd.Categorical(
        station_summary["station"], categories=ordered_categories, ordered=True
    )
    return station_summary.sort_values("station")


def save_delay_hours_by_station(station_summary: pd.DataFrame) -> None:
    plt.figure(figsize=(8, 5))
    plt.bar(station_summary["station"].astype(str), station_summary["delay_hours"])
    plt.title("Delay Hours by Station")
    plt.xlabel("Station")
    plt.ylabel("Total Synthetic Delay Hours")
    plt.tight_layout()
    plt.savefig(REPORTS_DIR / "delay_hours_by_station.png", dpi=150)
    plt.close()


def save_station_defect_rate_chart(station_summary: pd.DataFrame) -> None:
    plt.figure(figsize=(8, 5))
    plt.bar(
        station_summary["station"].astype(str),
        station_summary["defect_rate_percent"],
    )
    plt.title("Station Defect Rate")
    plt.xlabel("Station")
    plt.ylabel("Defect Rate (%)")
    plt.tight_layout()
    plt.savefig(REPORTS_DIR / "station_defect_rate_chart.png", dpi=150)
    plt.close()


def save_defect_type_ranking(defect_log: pd.DataFrame) -> None:
    defect_ranking = (
        defect_log.groupby("defect_type", as_index=False)["defect_qty"]
        .sum()
        .sort_values("defect_qty", ascending=False)
    )

    plt.figure(figsize=(8, 5))
    plt.bar(defect_ranking["defect_type"], defect_ranking["defect_qty"])
    plt.title("Defect Type Ranking")
    plt.xlabel("Defect Type")
    plt.ylabel("Synthetic Defect Quantity")
    plt.tight_layout()
    plt.savefig(REPORTS_DIR / "defect_type_ranking.png", dpi=150)
    plt.close()


def main() -> None:
    defect_log = load_defect_log()
    station_summary = build_station_summary(defect_log)

    save_delay_hours_by_station(station_summary)
    save_station_defect_rate_chart(station_summary)
    save_defect_type_ranking(defect_log)

    print("Chart generation completed.")
    print(f"Output folder: {REPORTS_DIR}")


if __name__ == "__main__":
    main()
