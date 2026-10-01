from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "sample_learning_activity.csv"


def load_activity(path: Path = DATA_PATH) -> pd.DataFrame:
 df = pd.read_csv(path, parse_dates=["event_date"])

 required = {
        "participant_id",
        "event_date",
        "organization_id",
        "topic",
        "delivery_format",
        "activity_type",
    }
 missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

 allowed_activity = {"registration", "attendance", "completion"}
 unexpected = set(df["activity_type"].dropna().unique()).difference(allowed_activity)
    if unexpected:
        raise ValueError(f"Unexpected activity types: {sorted(unexpected)}")

 df = df.drop_duplicates().copy()
 df["quarter"] = df["event_date"].dt.to_period("Q").astype(str)
 df["participant_event"] = (
 df["participant_id"].astype(str)
 + "|"
 + df["event_date"].dt.strftime("%Y-%m-%d")
    )
    return df


def safe_rate( umerator: int, denominator: int) -> float:
    return umerator / denominator if denominator else 0.0


def summarize(df: pd.DataFrame) -> None:
 registered = set(df.loc[df["activity_type"] == "registration", "participant_event"])
 attended = set(df.loc[df["activity_type"] == "attendance", "participant_event"])
 completed = set(df.loc[df["activity_type"] == "completion", "participant_event"])

    print("LEARNING ANALYTICS SUMMARY")
    print("=" * 28)
    print(f"Activity records: {len(df):,}")
    print(f"Unique participants: {df['participant_id'].nunique():,}")
    print(f"Active organizations: {df['organization_id'].nunique():,}")
    print(f"Attendance conversion: {safe_rate(len(attended), len(registered)):.1%}")
    print(f"Completion conversion: {safe_rate(len(completed), len(attended)):.1%}")

    print("\nActivity by quarter")
    print(df.groupby("quarter").size().rename("activities").to_string())

    print("\nActivity by topic")
    print(
 df.groupby("topic")
 .size()
 .sort_values(ascending=False)
 .rename("activities")
 .to_string()
    )

    print("\nActivity by delivery format")
    print(
 df.groupby("delivery_format")
 .size()
 .sort_values(ascending=False)
 .rename("activities")
 .to_string()
    )


if __name__ == "__main__":
 activity = load_activity()
    summarize(activity)
