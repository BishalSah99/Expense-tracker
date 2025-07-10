import csv
import os
import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

# File to store expenses
FILE_NAME = "expenses.csv"

# Function to add expense
def add_expense():
    date_str = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Transport, Rent, etc.): ").capitalize()
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date_str, category, amount])

    print("Expense added successfully!\n")

# Function to read expenses
def read_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    expenses = []
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            date_str, category, amount = row
            expenses.append((datetime.datetime.strptime(date_str, "%Y-%m-%d"), category, float(amount)))
    return expenses

# Function to show monthly report
def monthly_report():
    expenses = read_expenses()
    if not expenses:
        print("No data available.\n")
        return

    month = input("Enter month and year (MM-YYYY): ")
    month_dt = datetime.datetime.strptime(month, "%m-%Y")

    category_totals = defaultdict(float)

    for date, category, amount in expenses:
        if date.year == month_dt.year and date.month == month_dt.month:
            category_totals[category] += amount

    if not category_totals:
        print("No expenses found for this month.\n")
        return

    print("\nMonthly Report:")
    for category, total in category_totals.items():
        print(f"{category}: ₹{total:.2f}")

    # Plot pie chart
    plt.figure(figsize=(6,6))
    plt.pie(category_totals.values(), labels=category_totals.keys(), autopct='%1.1f%%')
    plt.title(f"Expenses for {month}")
    plt.show()

# CLI Menu
def menu():
    while True:
        print("Expense Tracker CLI")
        print("1. Add Expense")
        print("2. Monthly Report")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            monthly_report()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    # Create file with header if doesn't exist
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            # No header needed for simplicity
    menu()
