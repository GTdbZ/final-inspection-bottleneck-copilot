from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {
    "lot_id",
    "station",
    "shift",
    "input_qty",
    "defect_qty",
    "defect_type",
    "delay_hours",
}
STATION_ORDER = ["AOI", "Final Inspection"]


def find_input_csv(repo_root: Path) -> Path:
    """Locate the synthetic defect log by schema rather than by a hard-coded path."""
    mock_data_dir = repo_root / "mock_data"

    if not mock_data_dir.exists():
        raise FileNotFoundError("mock_data directory was not found.")

    for csv_path in sorted(mock_data_dir.glob("*.csv")):
        sample = pd.read_csv(csv_path, nrows=5)
        if REQUIRED_COLUMNS.issubset(sample.columns):
            return csv_path

    raise FileNotFoundError(
        "No synthetic CSV file with the required schema was found in mock_data."
    )


def validate_data(df: pd.DataFrame) -> None:
    missing_columns = REQUIRED_COLUMNS - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    if (df["input_qty"] <= 0).any():
        raise ValueError("input_qty must be greater than 0 for every row.")
    if (df["defect_qty"] < 0).any():
        raise ValueError("defect_qty cannot be negative.")
    if (df["defect_qty"] > df["input_qty"]).any():
        raise ValueError("defect_qty cannot exceed input_qty.")
    if (df["delay_hours"] < 0).any():
        raise ValueError("delay_hours cannot be negative.")


def build_group_summary(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    summary = (
        df.groupby(group_col, as_index=False)
        .agg(
            input_qty=("input_qty", "sum"),
            defect_qty=("defect_qty", "sum"),
            delay_hours=("delay_hours", "sum"),
        )
        .assign(defect_rate=lambda data: data["defect_qty"] / data["input_qty"])
    )
    summary["defect_rate_percent"] = summary["defect_rate"] * 100
    return summary


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    reports_dir = repo_root / "reports"
    reports_dir.mkdir(exist_ok=True)

    input_csv = find_input_csv(repo_root)
    df = pd.read_csv(input_csv)
    validate_data(df)

    station_summary = build_group_summary(df, "station")
    station_summary["station"] = pd.Categorical(
        station_summary["station"], categories=STATION_ORDER, ordered=True
    )
    station_summary = station_summary.sort_values("station")

    shift_summary = build_group_summary(df, "shift").sort_values(
        "defect_rate", ascending=False
    )

    defect_summary = (
        df.groupby("defect_type", as_index=False)
        .agg(defect_qty=("defect_qty", "sum"))
        .sort_values("defect_qty", ascending=False)
    )

    bottleneck_station = station_summary.sort_values(
        "delay_hours", ascending=False
    ).iloc[0]

    output_path = reports_dir / "analysis_summary.txt"
    with output_path.open("w", encoding="utf-8") as report:
        report.write("Final Inspection Bottleneck Copilot - Analysis Summary\n")
        report.write("=" * 58 + "\n\n")
        report.write("Data safety statement:\n")
        report.write("- Synthetic/mock data only\n")
        report.write("- No company/customer/product data\n")
        report.write("- No real yield, capacity, or internal production data\n\n")
        report.write(f"Input file: {input_csv.relative_to(repo_root)}\n\n")

        report.write("Station summary:\n")
        report.write(station_summary.to_string(index=False))
        report.write("\n\n")

        report.write("Shift summary (highest defect rate first):\n")
        report.write(shift_summary.to_string(index=False))
        report.write("\n\n")

        report.write("Defect type ranking:\n")
        report.write(defect_summary.to_string(index=False))
        report.write("\n\n")

        report.write("Bottleneck proxy:\n")
        report.write(
            f"- {bottleneck_station['station']} has the highest total "
            f"synthetic delay_hours value at {bottleneck_station['delay_hours']:.2f} hours.\n"
        )
        report.write("- This is a demonstration proxy, not a causal conclusion.\n")

    print(f"Analysis summary written to {output_path.relative_to(repo_root)}")


if __name__ == "__main__":
    main()
