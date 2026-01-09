from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
from datetime import datetime
from src.reports import category_wise_report, total_expense, average_expense

REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)

def generate_pdf_report(expenses):
    filename = os.path.join(REPORT_DIR, "Expense_Report.pdf")
    c = canvas.Canvas(filename, pagesize=A4)

    width, height = A4
    y = height - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Personal Finance Report")
    y -= 30

    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    y -= 40

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, f"Total Expense: ₹{total_expense(expenses):.2f}")
    y -= 20
    c.drawString(50, y, f"Average Expense: ₹{average_expense(expenses):.2f}")
    y -= 30

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Category-wise Breakdown:")
    y -= 20

    c.setFont("Helvetica", 10)
    for category, amount in category_wise_report(expenses).items():
        c.drawString(70, y, f"{category}: ₹{amount:.2f}")
        y -= 15

        if y < 100:
            c.showPage()
            y = height - 50

    c.save()
    print("PDF report generated:", filename)
