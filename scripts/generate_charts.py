from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT_DIR / "reports"
MOCK_DATA_DIR = ROOT_DIR / "mock_data"

REPORTS_DIR.mkdir(exist_ok=True)

STATION_ORDER = ["AOI", "Final Inspection"]


def find_csv(filename: str) -> Path:
    """Find a CSV file from mock_data/ first, then repo root."""
    candidates = [
        MOCK_DATA_DIR / filename,
        ROOT_DIR / filename,
    ]

    for path in candidates:
        if path.exists():
            return path

    raise FileNotFoundError(f"Cannot find required CSV file: {filename}")


def apply_station_order(df: pd.DataFrame, station_col: str = "station") -> pd.DataFrame:
    """Apply a consistent station order for station-based charts."""
    df = df.copy()

    existing = list(df[station_col].dropna().unique())
    ordered_categories = [s for s in STATION_ORDER if s in existing]
    ordered_categories += [s for s in existing if s not in ordered_categories]

    df[station_col] = pd.Categorical(
        df[station_col],
        categories=ordered_categories,
        ordered=True,
    )

    return df.sort_values(station_col)


def load_station_summary() -> pd.DataFrame:
    """Load station_summary.csv, or generate station summary from synthetic defect log."""
    try:
        station_summary_path = find_csv("station_summary.csv")
        return pd.read_csv(station_summary_path)
    except FileNotFoundError:
        defect_log_path = find_csv("synthetic_defect_log.csv")
        defect_log = pd.read_csv(defect_log_path)

        station_summary = (
            defect_log.groupby("station", as_index=False)
            .agg(
                input_qty=("input_qty", "sum"),
                defect_qty=("defect_qty", "sum"),
                delay_hours=("delay_hours", "sum"),
            )
        )

        station_summary["defect_rate"] = (
            station_summary["defect_qty"] / station_summary["input_qty"]
        )
        station_summary["defect_rate_percent"] = station_summary["defect_rate"] * 100

        return station_summary


def load_defect_log() -> pd.DataFrame:
    """Load synthetic defect log."""
    defect_log_path = find_csv("synthetic_defect_log.csv")
    return pd.read_csv(defect_log_path)


def save_delay_hours_by_station(station_summary: pd.DataFrame) -> None:
    station_plot_df = apply_station_order(station_summary)

    plt.figure(figsize=(8, 5))
    plt.bar(station_plot_df["station"], station_plot_df["delay_hours"])
    plt.title("Delay Hours by Station")
    plt.xlabel("Station")
    plt.ylabel("Delay Hours")
    plt.tight_layout()
    plt.savefig(REPORTS_DIR / "delay_hours_by_station.png")
    plt.close()


def save_station_defect_rate_chart(station_summary: pd.DataFrame) -> None:
    station_plot_df = apply_station_order(station_summary)

    plt.figure(figsize=(8, 5))
    plt.bar(station_plot_df["station"], station_plot_df["defect_rate_percent"])
    plt.title("Station Defect Rate")
    plt.xlabel("Station")
    plt.ylabel("Defect Rate (%)")
    plt.tight_layout()
    plt.savefig(REPORTS_DIR / "station_defect_rate_chart.png")
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
    plt.ylabel("Defect Quantity")
    plt.tight_layout()
    plt.savefig(REPORTS_DIR / "defect_type_ranking.png")
    plt.close()


def main() -> None:
    station_summary = load_station_summary()
    defect_log = load_defect_log()

    save_delay_hours_by_station(station_summary)
    save_station_defect_rate_chart(station_summary)
    save_defect_type_ranking(defect_log)

    print("Chart generation completed.")
    print(f"Output folder: {REPORTS_DIR}")


if __name__ == "__main__":
    main()
