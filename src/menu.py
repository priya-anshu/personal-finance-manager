from src.pdf_report import generate_pdf_report
from src.expense import Expense
from src.utils import validate_amount, validate_date, check_budget
from src.file_manager import save_expense, backup_data, restore_data, load_expenses
from src.reports import (
    total_expense,
    average_expense,
    category_wise_report,
    plot_category_chart,
    plot_monthly_trend
)


def show_menu():
    print("\n==== Personal Finance Manager ====")
    print("1. Add Expense")
    print("2. View Summary Report")
    print("3. Show Category Chart")
    print("4. Show Monthly Trend Chart")
    print("5. Backup Data")
    print("6. Restore Data")
    print("7. Generate PDF Report")
    print("8. Exit")


def add_expense():
    try:
        amount = validate_amount(input("Amount: "))
        category = input("Category: ").strip() or "Others"
        date = validate_date(input("Date (YYYY-MM-DD): "))
        description = input("Description: ")

        expense = Expense(amount, category, date, description)
        save_expense(expense)

        print("Expense added successfully.")

        # Budget check
        expenses = load_expenses()
        exceeded, total = check_budget(expenses)

        if exceeded:
            print(f"⚠ WARNING: Monthly budget exceeded! Total spent: ₹{total:.2f}")

    except ValueError as ve:
        print("Input Error:", ve)
    except Exception as e:
        print("Unexpected Error:", e)


def show_reports(expenses):
    print("\n--- Expense Report ---")
    print(f"Total Expense: ₹{total_expense(expenses):.2f}")
    print(f"Average Expense: ₹{average_expense(expenses):.2f}")

    print("\nCategory-wise:")
    for cat, amt in category_wise_report(expenses).items():
        print(f"{cat}: ₹{amt:.2f}")


def show_category_chart(expenses):
    plot_category_chart(expenses)


def show_monthly_chart(expenses):
    plot_monthly_trend(expenses)


def generate_pdf(expenses):
    generate_pdf_report(expenses)
