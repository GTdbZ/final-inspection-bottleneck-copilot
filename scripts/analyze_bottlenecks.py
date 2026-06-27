from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {
    "lot_id",
    "station",
    "defect_type",
    "inspected_qty",
    "defect_qty",
    "delay_hours",
}

STATION_ORDER = ["AOI", "Final Inspection"]


def find_input_csv(repo_root: Path) -> Path:
    mock_data_dir = repo_root / "mock_data"

    if not mock_data_dir.exists():
        raise FileNotFoundError("mock_data directory was not found.")

    for csv_path in sorted(mock_data_dir.glob("*.csv")):
        sample = pd.read_csv(csv_path, nrows=5)
        if REQUIRED_COLUMNS.issubset(sample.columns):
            return csv_path

    raise FileNotFoundError(
        "No synthetic CSV file with the required v0.2 schema was found in mock_data."
    )


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    reports_dir = repo_root / "reports"
    reports_dir.mkdir(exist_ok=True)

    input_csv = find_input_csv(repo_root)
    df = pd.read_csv(input_csv)

    missing_columns = REQUIRED_COLUMNS - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    df["defect_rate"] = df["defect_qty"] / df["inspected_qty"]

    station_summary = (
        df.groupby("station", as_index=False)
        .agg(
            inspected_qty=("inspected_qty", "sum"),
            defect_qty=("defect_qty", "sum"),
            avg_delay_hours=("delay_hours", "mean"),
        )
        .assign(defect_rate=lambda data: data["defect_qty"] / data["inspected_qty"])
    )

    station_summary["station"] = pd.Categorical(
        station_summary["station"],
        categories=STATION_ORDER,
        ordered=True,
    )
    station_summary = station_summary.sort_values("station")

    defect_summary = (
        df.groupby("defect_type", as_index=False)
        .agg(defect_qty=("defect_qty", "sum"))
        .sort_values("defect_qty", ascending=False)
    )

    bottleneck_station = station_summary.sort_values(
        "avg_delay_hours", ascending=False
    ).iloc[0]

    output_path = reports_dir / "analysis_summary.txt"

    with output_path.open("w", encoding="utf-8") as report:
        report.write("Final Inspection Bottleneck Copilot - Analysis Summary\n")
        report.write("=" * 58 + "\n\n")
        report.write("Data safety statement:\n")
        report.write("- Synthetic or mock data only\n")
        report.write("- No company data\n")
        report.write("- No customer names\n")
        report.write("- No product names or part numbers\n")
        report.write("- No real yield or capacity data\n")
        report.write("- No internal production data\n\n")

        report.write(f"Input file: {input_csv.relative_to(repo_root)}\n\n")

        report.write("Station summary:\n")
        report.write(station_summary.to_string(index=False))
        report.write("\n\n")

        report.write("Defect type ranking:\n")
        report.write(defect_summary.to_string(index=False))
        report.write("\n\n")

        report.write("Bottleneck proxy:\n")
        report.write(
            f"- {bottleneck_station['station']} has the highest average "
            f"delay_hours value at {bottleneck_station['avg_delay_hours']:.2f} hours.\n"
        )

    print(f"Analysis summary written to {output_path.relative_to(repo_root)}")


if __name__ == "__main__":
    main()
