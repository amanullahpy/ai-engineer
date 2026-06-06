import csv
import os
from datetime import datetime

class Expense:
    """Represents a single expense entry with date, amount, category, and description."""
    def __init__(self, date_str, amount_str, category, description):
        self.date = self.validate_date(date_str)
        self.amount = self.validate_amount(amount_str)
        self.category = self.validate_text(category, "Category")
        self.description = self.validate_text(description, "Description")

    @staticmethod
    def validate_date(date_str):
        """Validates date string is in YYYY-MM-DD format. Defaults to today's date if empty."""
        date_str = date_str.strip()
        if not date_str:
            return datetime.today().strftime('%Y-%m-%d')
        try:
            valid_date = datetime.strptime(date_str, "%Y-%m-%d")
            return valid_date.strftime("%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format (or leave empty for today).")

    @staticmethod
    def validate_amount(amount_str):
        """Validates that the amount is a positive number."""
        try:
            amount = float(amount_str.strip())
            if amount <= 0:
                raise ValueError()
            return amount
        except ValueError:
            raise ValueError("Amount must be a positive number (greater than 0).")

    @staticmethod
    def validate_text(text, field_name):
        """Ensures text fields are not empty."""
        text = text.strip()
        if not text:
            raise ValueError(f"{field_name} cannot be empty.")
        return text

    def to_row(self):
        """Converts expense attributes to a list suitable for CSV writing."""
        return [self.date, self.amount, self.category, self.description]


class ExpenseTracker:
    """Handles loading, storing, calculating statistics, and saving expenses to a CSV file."""
    def __init__(self, filepath="expenses.csv"):
        self.filepath = filepath
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        """Reads existing expenses from the CSV file and populates self.expenses."""
        if not os.path.exists(self.filepath):
            return
        
        try:
            with open(self.filepath, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                # Skip header
                next(reader, None)
                for row_num, row in enumerate(reader, 2):
                    if len(row) == 4:
                        try:
                            self.expenses.append(Expense(row[0], row[1], row[2], row[3]))
                        except ValueError as e:
                            print(f"Skipping corrupt row {row_num} in CSV: {e}")
        except Exception as e:
            print(f"Error loading CSV file: {e}")

    def add_expense(self, expense):
        """Adds an expense to the local list and saves it to the CSV file."""
        self.expenses.append(expense)
        self.save_to_csv()

    def save_to_csv(self):
        """Writes all expenses back to the CSV file."""
        header = ["Date", "Amount", "Category", "Description"]
        try:
            with open(self.filepath, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                for exp in self.expenses:
                    writer.writerow(exp.to_row())
        except Exception as e:
            print(f"Error saving to CSV: {e}")

    def get_total_spend(self):
        """Returns the sum of all expense amounts."""
        return sum(exp.amount for exp in self.expenses)

    def get_category_breakdown(self):
        """Computes and returns a dictionary of category -> total amount."""
        breakdown = {}
        for exp in self.expenses:
            breakdown[exp.category] = breakdown.get(exp.category, 0.0) + exp.amount
        return breakdown


# --- CLI Interface Functions ---

def print_header(title):
    print("\n" + "=" * 50)
    print(f" {title.center(48)} ")
    print("=" * 50)

def show_menu():
    print("\n[1] Add New Expense")
    print("[2] View All Expenses")
    print("[3] View Total Spending")
    print("[4] View Category Summary")
    print("[5] Exit")

def main():
    tracker = ExpenseTracker()
    
    print_header("WELCOME TO CLI EXPENSE TRACKER")
    print(f"Tracking file: {os.path.abspath(tracker.filepath)}")
    
    while True:
        show_menu()
        choice = input("\nSelect an option (1-5): ").strip()
        
        if choice == "1":
            print_header("ADD NEW EXPENSE")
            date_in = input("Date (YYYY-MM-DD or leave empty for Today): ").strip()
            amount_in = input("Amount ($): ").strip()
            category_in = input("Category (e.g. Food, Rent, Transport): ").strip()
            desc_in = input("Description: ").strip()
            
            try:
                new_expense = Expense(date_in, amount_in, category_in, desc_in)
                tracker.add_expense(new_expense)
                print("\n✔️ Expense added and saved successfully!")
            except ValueError as e:
                print(f"\n❌ Input Error: {e}")
                
        elif choice == "2":
            print_header("ALL RECORDED EXPENSES")
            if not tracker.expenses:
                print("No expenses recorded yet.")
            else:
                # Print as a neat aligned table
                print(f"{'#':<3} | {'Date':<10} | {'Category':<12} | {'Amount':<10} | {'Description'}")
                print("-" * 65)
                for i, exp in enumerate(tracker.expenses, 1):
                    print(f"{i:<3} | {exp.date:<10} | {exp.category:<12} | ${exp.amount:<9.2f} | {exp.description}")
                print(f"\nTotal Entries: {len(tracker.expenses)}")
                
        elif choice == "3":
            print_header("TOTAL SPENDING")
            total = tracker.get_total_spend()
            print(f"Your total spending is: ${total:.2f}")
            
        elif choice == "4":
            print_header("CATEGORY BREAKDOWN")
            breakdown = tracker.get_category_breakdown()
            if not breakdown:
                print("No expenses recorded yet.")
            else:
                print(f"{'Category':<15} | {'Total Spent':<12} | {'Percentage'}")
                print("-" * 45)
                total_spend = tracker.get_total_spend()
                for category, amount in breakdown.items():
                    percentage = (amount / total_spend) * 100 if total_spend > 0 else 0
                    print(f"{category:<15} | ${amount:<11.2f} | {percentage:.1f}%")
                    
        elif choice == "5":
            print("\nExiting. Thank you for tracking your expenses! Keep saving.")
            break
        else:
            print("\n❌ Invalid choice! Please select a option between 1 and 5.")

if __name__ == "__main__":
    main()
