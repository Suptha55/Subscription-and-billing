def evaluate_status(previous_status, usage, limit_gb):
    if previous_status == "CANCELLED":
        return "CANCELLED"

    if usage > 1.5 * limit_gb:
        return "SUSPENDED"

    if previous_status == "SUSPENDED" and usage <= limit_gb:
        return "ACTIVE"

    return previous_status
