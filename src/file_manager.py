import csv
import os
from src.expense import Expense

# Get absolute path of project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_FILE = os.path.join(BASE_DIR, "data", "expenses.csv")
BACKUP_FILE = os.path.join(BASE_DIR, "data", "expenses_backup.csv")

def load_expenses():
    expenses = []

    if not os.path.exists(DATA_FILE):
        return expenses

    with open(DATA_FILE, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                expenses.append(Expense(*row))

    return expenses

def save_expense(expense):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    with open(DATA_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(expense.to_list())

def backup_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as original, \
             open(BACKUP_FILE, "w", encoding="utf-8") as backup:
            backup.write(original.read())

def restore_data():
    if os.path.exists(BACKUP_FILE):
        with open(BACKUP_FILE, "r", encoding="utf-8") as backup, \
             open(DATA_FILE, "w", encoding="utf-8") as original:
            original.write(backup.read())
