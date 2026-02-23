import json

def generate_summary(df, output_json="billing_summary.json"):
    summary = {
        "total_subscriptions": len(df),
        "active_subscriptions": int((df["final_status"] == "ACTIVE").sum()),
        "suspended_subscriptions": int((df["final_status"] == "SUSPENDED").sum()),
        "cancelled_subscriptions": int((df["final_status"] == "CANCELLED").sum()),
        "total_revenue": float(df["total_bill"].sum()),
        "average_bill": float(df["total_bill"].mean()) if len(df) > 0 else 0
    }

    with open(output_json, "w") as f:
        json.dump(summary, f, indent=4)

    return summary
