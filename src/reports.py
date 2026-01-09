import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime
import os

# Global chart style (safe + professional)
plt.style.use("ggplot")

REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)


def total_expense(expenses):
    return sum(exp.amount for exp in expenses)


def average_expense(expenses):
    return total_expense(expenses) / len(expenses) if expenses else 0


def category_wise_report(expenses):
    report = defaultdict(float)
    for exp in expenses:
        report[exp.category] += exp.amount
    return report


def plot_category_chart(expenses):
    data = category_wise_report(expenses)

    if not data:
        print("No data available for category chart.")
        return

    categories = list(data.keys())
    amounts = list(data.values())

    plt.figure(figsize=(8, 5))
    bars = plt.bar(categories, amounts)

    plt.title("Category-wise Expense Distribution", fontsize=14)
    plt.xlabel("Category")
    plt.ylabel("Amount Spent")
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:.0f}",
            ha="center",
            va="bottom",
            fontsize=9
        )

    plt.tight_layout()
    plt.savefig(os.path.join(REPORT_DIR, "category_expense_chart.png"))
    plt.show()


def plot_monthly_trend(expenses):
    monthly = defaultdict(float)

    for exp in expenses:
        month = datetime.strptime(exp.date, "%Y-%m-%d").strftime("%Y-%m")
        monthly[month] += exp.amount

    if not monthly:
        print("No data available for monthly trend.")
        return

    months = sorted(monthly.keys())
    amounts = [monthly[m] for m in months]

    plt.figure(figsize=(9, 5))
    plt.plot(months, amounts, marker="o", linewidth=2)

    plt.title("Monthly Expense Trend", fontsize=14)
    plt.xlabel("Month")
    plt.ylabel("Total Expense")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig(os.path.join(REPORT_DIR, "monthly_expense_trend.png"))
    plt.show()
