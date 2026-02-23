def calculate_bill(status, usage, limit_gb, monthly_fee):
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
