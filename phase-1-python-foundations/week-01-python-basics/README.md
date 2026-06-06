# Week 1: Python Basics & Setup

Welcome to the first week of your transition into AI Engineering! This week is dedicated to setting up your workspace, getting comfortable with Python's syntax and Object-Oriented Programming (OOP) model, and establishing git workflows for your code.

---

## ⚙️ Root Virtual Environment Setup

Before writing any Python code, set up a shared virtual environment at the **root** of this repository. This prevents packages like NumPy and PyTorch from bloating your folder size and simplifies configuration.

1. Open your terminal at the project root (`ai-engineer`).
2. Run this command to create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate it:
   * **Windows (PowerShell):** `.\.venv\Scripts\Activate.ps1`
   * **Windows (CMD):** `.\.venv\Scripts\activate.bat`
   * **macOS / Linux:** `source .venv/bin/activate`
4. Install the initial packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Configure your IDE (Cursor / VS Code) interpreter to point to `.venv` (see [.ai/python-env-setup.md](../../.ai/python-env-setup.md) for detailed help).

---

## 📚 Concepts & Explanations

Here is a simplified overview of what you are learning this week.

### 1. Python Syntax & Control Flow
Unlike Javascript, Python uses **indentation** (4 spaces) rather than curly braces `{}` to define blocks of code (loops, functions, classes).

*   **Variables & Typing:** Python is dynamically typed but strongly typed. You don't declare variables with `let` or `const`:
    ```python
    user_name = "Alice"  # String
    user_age = 25        # Integer
    is_active = True     # Boolean
    ```
*   **Lists and Dictionaries:**
    ```python
    # Lists are like JS arrays
    hobbies = ["reading", "coding", "gaming"]
    
    # Dictionaries are like JS objects
    user_profile = {"name": "Alice", "age": 25}
    ```
*   **Conditionals & Loops:**
    ```python
    if user_age >= 18:
        print("Adult")
    else:
        print("Minor")
        
    for hobby in hobbies:
        print(f"I like {hobby}")
    ```

### 2. Object-Oriented Programming (OOP) in Python
OOP allows you to structure programs by bundling related properties and behaviors into individual objects. This is a critical concept since all deep learning frameworks (like PyTorch) use OOP to define neural network models.

*   **Classes and Objects:**
    ```python
    class Developer:
        # The constructor method (like constructor() in JS)
        def __init__(self, name, language):
            self.name = name          # Instance variable
            self.language = language  # Instance variable
            
        # A custom method
        def introduce(self):
            return f"Hi, I'm {self.name} and I code in {self.language}!"
            
    # Creating an instance (No 'new' keyword required!)
    dev = Developer("Aman", "Python")
    print(dev.introduce())
    ```
    *Note: The `self` parameter is a reference to the current instance of the class and is passed automatically to methods. You must define it as the first parameter of any class method.*

### 3. Git & GitHub Workflows
As you build projects, committing modular changes and pushing them to GitHub will serve as your public learning log.
*   `git init`: Initialize repository.
*   `git add .`: Stage modifications.
*   `git commit -m "feat: setup initial folders"`: Save staged changes.
*   `git push origin main`: Upload changes to GitHub.

---

## 🛠️ Weekly Project: CLI Expense Tracker
This week, you will build a command-line interface (CLI) to track daily expenses. 

*   **Goal:** Build a script that prompts users for expense details (amount, category, description), appends it to a local CSV file, and calculates summary metrics (total spend, category breakdown).
*   **Key Learnings:**
    *   Using python's built-in `csv` module to read and write files.
    *   Accepting user inputs using `input()`.
    *   Leveraging OOP (e.g., creating an `Expense` class and an `ExpenseTracker` manager class).
*   **Frontend Integration Tip:** Keep the storage logic separate from the prompt print loops. This ensures you can easily import your tracker class into a web API backend (FastAPI) later without rewriting the core tracking logic.

👉 Detailed Project instructions are in **[projects/cli-expense-tracker](./projects/cli-expense-tracker/README.md)**.

---

## 📓 Weekly Reflection & Notes
Use the subdirectories to log your study notes:
- **[01-python-syntax-oop](./01-python-syntax-oop/README.md):** Write syntax notes and object-oriented exercises.
- **[02-git-github-workflows](./02-git-github-workflows/README.md):** Document useful command commands and git practices.
