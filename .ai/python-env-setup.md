# 🐍 Root Python Virtual Environment Setup

To keep this multi-week repository clean and efficient, we use a **single, shared virtual environment (`.venv`) at the root of the project** instead of creating separate virtual environments in each individual week or project directory.

## Why this is Optimal:
1. **Saves Disk Space:** A single PyTorch/TensorFlow installation can take 2-3 GB of disk space. Installing it 24 separate times would take up over 50 GB.
2. **Simplified IDE Configuration:** You only need to set your Python interpreter once in VS Code or Cursor, and all your scripts will run with the correct dependencies.
3. **Common Dependency Base:** Basic packages (NumPy, Pandas, Requests) will be shared across all weeks, while you can add advanced libraries (PyTorch, LangChain) as you progress.

---

## 🛠️ Step-by-Step Setup Guide

Follow these steps from the root directory of your workspace (`ai-engineer`):

### Step 1: Create the Virtual Environment
Run the following command to create a virtual environment named `.venv`:
```bash
python -m venv .venv
```

### Step 2: Activate the Virtual Environment
Activate the environment based on your operating system and shell:

*   **Windows (PowerShell - Recommended):**
    ```powershell
    .\.venv\Scripts\Activate.ps1
    ```
    *(Note: If you get an execution policy error, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` first)*
*   **Windows (CMD):**
    ```cmd
    .\.venv\Scripts\activate.bat
    ```
*   **macOS / Linux:**
    ```bash
    source .venv/bin/activate
    ```

When active, you should see `(.venv)` displayed in your terminal prompt.

### Step 3: Upgrade pip & Install Initial Packages
It is best practice to upgrade pip first:
```bash
python -m pip install --upgrade pip
```

Then install the initial packages using the root `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## ⚙️ Editor Configuration (VS Code / Cursor / Windsurf)

To ensure your editor recognizes the environment:
1. Open the project root folder.
2. Open a Python file or press `Ctrl + Shift + P` (or `Cmd + Shift + P` on Mac).
3. Search for and select **Python: Select Interpreter**.
4. Choose the interpreter pointing to your virtual environment (usually labeled `('.venv': venv) ./ .venv/Scripts/python.exe`).
5. Your editor will now automatically highlight syntax and provide autocomplete for all installed packages!
