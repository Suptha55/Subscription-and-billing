import pandas as pd
from datetime import datetime


def calculate_prorated_fee(monthly_fee, start_date, end_date):
    """
    Calculates prorated monthly fee for March 2024.
    """

    march_start = datetime(2024, 3, 1)
    march_end = datetime(2024, 3, 31)

    start_date = pd.to_datetime(start_date, errors="coerce")
    end_date = pd.to_datetime(end_date, errors="coerce")

    if pd.isna(start_date):
        start_date = march_start

    if pd.isna(end_date):
        end_date = march_end

    active_start = max(start_date, march_start)
    active_end = min(end_date, march_end)

    if active_start > active_end:
        return 0

    active_days = (active_end - active_start).days + 1
    total_days = 31

    return monthly_fee * (active_days / total_days)


def calculate_bill(status, usage, limit_gb, monthly_fee):
    """
    Existing billing logic — unchanged behavior.
    """

    if status == "CANCELLED":
        return 0, 0

    overage = max(0, usage - limit_gb)

    if status == "SUSPENDED":
        return 0, monthly_fee

    if usage <= limit_gb:
        return 0, monthly_fee

    overage_charge = overage * 10
    total_bill = monthly_fee + overage_charge

    return overage, total_bill
