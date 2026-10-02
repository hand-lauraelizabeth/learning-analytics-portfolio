"""AI-assisted technical learning extension for Laura Hand's public portfolio.

This module uses only the repository's fully synthetic sample data. It was added
as a technical translation/learning extension and should not be treated as
independent evidence of Python proficiency until Laura has personally run,
reviewed, and can explain the workflow.
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "sample_learning_activity.csv"
OUTPUT_DIR = ROOT / "outputs"

REQUIRED_COLUMNS = {
    "participant_id",
    "event_date",
    "organization_id",
    "topic",
    "delivery_format",
    "activity_type",
}
ALLOWED_ACTIVITY = {"registration", "attendance", "completion"}
EVENT_KEYS = [
    "participant_id",
    "event_date",
    "organization_id",
    "topic",
    "delivery_format",
]


def load_and_validate(path: Path = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["event_date"])
    missing = REQUIRED_COLUMNS.difference(df.columns)
    assert not missing, f"Missing required columns: {sorted(missing)}"
    assert not df[list(REQUIRED_COLUMNS)].isna().any().any(), "Required fields contain nulls"
    unexpected = set(df["activity_type"].unique()).difference(ALLOWED_ACTIVITY)
    assert not unexpected, f"Unexpected activity types: {sorted(unexpected)}"
    assert not df.duplicated().any(), "Duplicate activity rows found"
    return df


def build_event_funnel(df: pd.DataFrame) -> pd.DataFrame:
    funnel = (
        df.assign(value=1)
        .pivot_table(
            index=EVENT_KEYS,
            columns="activity_type",
            values="value",
            aggfunc="max",
            fill_value=0,
        )
        .reset_index()
    )
    for col in ["registration", "attendance", "completion"]:
        if col not in funnel.columns:
            funnel[col] = 0

    # Funnel integrity: downstream stages cannot exist without upstream stages.
    assert (funnel["attendance"] <= funnel["registration"]).all(), "Attendance without registration"
    assert (funnel["completion"] <= funnel["attendance"]).all(), "Completion without attendance"
    funnel["quarter"] = funnel["event_date"].dt.to_period("Q").astype(str)
    return funnel


def summarize(funnel: pd.DataFrame, group: str) -> pd.DataFrame:
    out = (
        funnel.groupby(group, as_index=False)
        .agg(
            registrations=("registration", "sum"),
            attendances=("attendance", "sum"),
            completions=("completion", "sum"),
        )
    )
    out["registration_to_attendance"] = out["attendances"].div(out["registrations"]).fillna(0)
    out["attendance_to_completion"] = out["completions"].div(out["attendances"]).fillna(0)
    return out


def main() -> None:
    df = load_and_validate()
    funnel = build_event_funnel(df)
    by_quarter = summarize(funnel, "quarter")
    by_topic = summarize(funnel, "topic")

    # Expected-result checks make silent logic drift visible in this tiny demo.
    assert len(df) == 36
    assert int(funnel["registration"].sum()) == 16
    assert int(funnel["attendance"].sum()) == 13
    assert int(funnel["completion"].sum()) == 7
    assert round(funnel["attendance"].sum() / funnel["registration"].sum(), 4) == 0.8125
    assert round(funnel["completion"].sum() / funnel["attendance"].sum(), 4) == 0.5385

    OUTPUT_DIR.mkdir(exist_ok=True)
    by_quarter.to_csv(OUTPUT_DIR / "funnel_by_quarter.csv", index=False)
    by_topic.to_csv(OUTPUT_DIR / "funnel_by_topic.csv", index=False)

    print("QA PASS: synthetic learning-activity funnel")
    print(f"Rows: {len(df)} | Registrations: 16 | Attendances: 13 | Completions: 7")
    print("\nQuarterly funnel")
    print(by_quarter.to_string(index=False))
    print("\nTopic funnel")
    print(by_topic.to_string(index=False))


if __name__ == "__main__":
    main()
