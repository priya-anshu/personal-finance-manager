from datetime import datetime

MONTHLY_BUDGET = 5000  # configurable

def check_budget(expenses):
    total = sum(exp.amount for exp in expenses)
    if total > MONTHLY_BUDGET:
        return True, total
    return False, total

def validate_amount(value):
    try:
        amount = float(value)
        if amount <= 0:
            raise ValueError
        return amount
    except ValueError:
        raise ValueError("Amount must be a positive number")

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")
