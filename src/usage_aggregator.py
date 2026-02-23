import pandas as pd
import logging

logger = logging.getLogger(__name__)

def aggregate_usage(usage_df):

    if usage_df.empty:
        return pd.DataFrame(columns=["subscription_id", "total_usage_gb"])

    # Parse dates
    usage_df["usage_date"] = pd.to_datetime(
        usage_df["usage_date"],
        errors="coerce"
    )

    # Retry if needed (DD-MM-YYYY)
    if usage_df["usage_date"].isna().all():
        usage_df["usage_date"] = pd.to_datetime(
            usage_df["usage_date"],
            dayfirst=True,
            errors="coerce"
        )

    # Remove invalid dates
    usage_df = usage_df.dropna(subset=["usage_date"])

    # Filter only March 2024
    usage_df = usage_df[
        (usage_df["usage_date"].dt.month == 3) &
        (usage_df["usage_date"].dt.year == 2024)
    ]

    # Detect duplicate records
    duplicate_count = usage_df.duplicated().sum()
    if duplicate_count > 0:
        logger.warning(f"{duplicate_count} duplicate usage records detected and removed.")
        usage_df = usage_df.drop_duplicates()

    # Convert usage safely
    usage_df["data_used_gb"] = pd.to_numeric(
        usage_df["data_used_gb"],
        errors="coerce"
    ).fillna(0)

    # Aggregate
    aggregated = (
        usage_df.groupby("subscription_id")["data_used_gb"]
        .sum()
        .reset_index()
    )

    aggregated.rename(
        columns={"data_used_gb": "total_usage_gb"},
        inplace=True
    )

    return aggregated
