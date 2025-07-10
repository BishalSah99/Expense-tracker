# Expense-tracker
🔧 Modules Used
csv: For reading/writing expense records to a file.

os: To check if the file exists.

datetime: For parsing and comparing dates.

matplotlib.pyplot: To visualize monthly expense distribution.

collections.defaultdict: To simplify the summation of category-wise expenses.

📌 Key Functions
1. add_expense()
Prompts user for:

date (format: YYYY-MM-DD)

category (like Food, Transport)

amount (float)

Appends the input to expenses.csv.

2. read_expenses()
Reads from expenses.csv (if it exists).

Converts date strings to datetime objects.

Returns a list of tuples: (date_obj, category, amount).

3. monthly_report()
Asks for a target month in MM-YYYY format.

Filters expenses for that month.

Sums amounts by category using defaultdict(float).

Displays the total per category.

Draws a pie chart using matplotlib for visualization.

4. menu()
CLI interface loop:

1: Add a new expense

2: Generate monthly report

3: Exit

Invalid inputs are handled with an error message.

📂 File Initialization
Before the menu starts:

python
Copy
Edit
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        # No header needed for simplicity
Creates expenses.csv if it doesn’t exist.

📈 Output Example
Input:
mathematica
Copy
Edit
Enter date (YYYY-MM-DD): 2025-07-10
Enter category (Food, Transport, Rent, etc.): food
Enter amount: 250
Report:
sql
Copy
Edit
Enter month and year (MM-YYYY): 07-2025

Monthly Report:
Food: ₹250.00
