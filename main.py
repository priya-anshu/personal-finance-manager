from src.menu import (
    show_menu,
    add_expense,
    show_reports,
    show_category_chart,
    show_monthly_chart,
    generate_pdf_report
)
from src.file_manager import load_expenses, backup_data, restore_data

def main():
    while True:
        expenses = load_expenses()
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_reports(expenses)
        elif choice == "3":
            show_category_chart(expenses)
        elif choice == "4":
            show_monthly_chart(expenses)
        elif choice == "5":
            backup_data()
            print("Backup completed.")
        elif choice == "6":
            restore_data()
            print("Data restored.")
        elif choice == "7":
            generate_pdf_report(expenses)
            print("PDF report generated.")
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
