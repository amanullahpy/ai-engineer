# Project: CLI Expense Tracker

## 🎯 Project Goal
Build a terminal-based expense tracker application in Python that helps users record daily expenses, categorize them, store them in a persistent CSV file, and view summary statistics.

This project introduces you to Python file handling, standard libraries, control flow loops, and Object-Oriented Programming (OOP) classes.

---

## 🏗️ Architecture Design

To keep your code clean and prepare you for full-stack AI development (where logic must be separated from interfaces), implement the tracker using two classes:

1.  **`Expense`**: Represents a single expense entry.
2.  **`ExpenseTracker`**: Handles the storage, retrieval, calculation of stats, and file operations.

### Proposed Code Template (`tracker.py`)

You can use this structure as a starting point. Your job is to fill in the class methods and design the terminal menu interface.

```python
import csv
import os

class Expense:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = float(amount)
        self.category = category
        self.description = description

    def to_row(self):
        """Converts expense attributes to a list suitable for CSV writing."""
        return [self.date, self.amount, self.category, self.description]

class ExpenseTracker:
    def __init__(self, filepath="expenses.csv"):
        self.filepath = filepath
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        """Reads existing expenses from the CSV file and populates self.expenses."""
        if not os.path.exists(self.filepath):
            return
        
        with open(self.filepath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            # Skip header if it exists
            next(reader, None)
            for row in reader:
                if len(row) == 4:
                    self.expenses.append(Expense(row[0], row[1], row[2], row[3]))

    def add_expense(self, expense):
        """Adds an expense to the local list and saves it to the CSV file."""
        self.expenses.append(expense)
        self.save_to_csv()

    def save_to_csv(self):
        """Writes all expenses in self.expenses back to the CSV file."""
        header = ["Date", "Amount", "Category", "Description"]
        with open(self.filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for exp in self.expenses:
                writer.writerow(exp.to_row())

    def get_total_spend(self):
        """Returns the sum of all expenses."""
        return sum(exp.amount for exp in self.expenses)

    def get_category_breakdown(self):
        """Computes and returns a dictionary of category -> total amount."""
        breakdown = {}
        for exp in self.expenses:
            breakdown[exp.category] = breakdown.get(exp.category, 0.0) + exp.amount
        return breakdown

# --- Menu Loop ---
def show_menu():
    print("\n=== Expense Tracker CLI ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spend")
    print("4. View Category Summary")
    print("5. Exit")

def main():
    tracker = ExpenseTracker()
    
    while True:
        show_menu()
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ").strip()
            amount = input("Enter amount: ").strip()
            category = input("Enter category (e.g., Food, Travel, Rent): ").strip()
            description = input("Enter description: ").strip()
            
            # Validation
            try:
                new_expense = Expense(date, amount, category, description)
                tracker.add_expense(new_expense)
                print("Expense added successfully!")
            except ValueError:
                print("Error: Amount must be a valid number.")
                
        elif choice == "2":
            print("\n--- All Expenses ---")
            if not tracker.expenses:
                print("No expenses recorded yet.")
            for i, exp in enumerate(tracker.expenses, 1):
                print(f"{i}. [{exp.date}] {exp.category}: ${exp.amount:.2f} - {exp.description}")
                
        elif choice == "3":
            total = tracker.get_total_spend()
            print(f"\nTotal Spending: ${total:.2f}")
            
        elif choice == "4":
            print("\n--- Category Breakdown ---")
            breakdown = tracker.get_category_breakdown()
            if not breakdown:
                print("No expenses recorded yet.")
            for category, total in breakdown.items():
                print(f"{category}: ${total:.2f}")
                
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select 1-5.")

if __name__ == "__main__":
    main()
```

---

## 🚀 Requirements Checklist
- [ ] Implement input validation (prevent empty inputs or letters in the amount field).
- [ ] Save to `expenses.csv` and verify it persists after exiting the terminal.
- [ ] Support printing all entries formatted neatly as a table.
- [ ] Handle missing file errors or empty lists gracefully.

## 💻 How to Run
Once you have written your script inside `tracker.py`, run it via terminal:
```bash
python tracker.py
```

## 🎨 Frontend Integration Tips
Because we separated the model (`Expense` and `ExpenseTracker`) from the menu print statements, you can:
1. Import `ExpenseTracker` in a FastAPI web script.
2. Expose GET and POST routes (e.g. `/api/expenses` and `/api/expenses/add`).
3. Build a beautiful React/Next.js dashboard utilizing TailwindCSS grids, form inputs, and animated charts showing category totals.
4. Instead of writing print statements, return the data as JSON, fetch it from your frontend React client, and render it dynamically!
