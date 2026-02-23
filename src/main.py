import logging
import os
from loader import load_subscriptions, load_usage
from usage_aggregator import aggregate_usage
from billing_engine import calculate_bill
from status_engine import evaluate_status
from reporter import generate_summary

import pandas as pd

logging.basicConfig(
    filename="logs/billing.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    subs = load_subscriptions("subscriptions.csv")
    usage = load_usage("usage.csv")

    aggregated_usage = aggregate_usage(usage)

    result = subs.merge(
        aggregated_usage,
        on="subscription_id",
        how="left"
    )

    result["total_usage_gb"] = result["total_usage_gb"].fillna(0)

    final_rows = []

    for _, row in result.iterrows():

        overage, bill = calculate_bill(
            row["status"],
            row["total_usage_gb"],
            row["usage_limit_gb"],
            row["monthly_fee"]
        )

        final_status = evaluate_status(
            row["status"],
            row["total_usage_gb"],
            row["usage_limit_gb"]
        )

        final_rows.append({
            "subscription_id": row["subscription_id"],
            "customer_id": row["customer_id"],
            "plan": row["plan"],
            "total_usage_gb": row["total_usage_gb"],
            "overage_gb": overage,
            "total_bill": bill,
            "final_status": final_status
        })

    output_df = pd.DataFrame(final_rows)

    output_df.to_csv("billing_output.csv", index=False)

    generate_summary(output_df)

if __name__ == "__main__":
    main()
