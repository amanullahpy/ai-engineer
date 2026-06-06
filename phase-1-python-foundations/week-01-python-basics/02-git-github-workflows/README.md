# Concept Deep-Dive: Git & GitHub Workflows

Git is a distributed version control system that tracks file changes, enabling collaborative development and codebase history tracking. GitHub is a cloud platform hosting Git repositories, facilitating team collaboration, reviews, and automated deployment (CI/CD).

---

## 1. Core Git Commands Reference

Here is a cheat sheet of the standard commands you will use daily:

### Initialization & Remote Setup
```bash
# Initialize a local Git repository
git init

# Link local repository to a remote GitHub repository
git remote add origin https://github.com/USERNAME/REPO-NAME.git

# Verify remote URLs linked
git remote -v
```

### Staging & Committing
```bash
# Check status of modified and untracked files
git status

# Stage specific changes
git add filename.py

# Stage all files
git add .

# Save staged changes with a descriptive message
git commit -m "feat: implement expense calculation logic"
```

### Syncing with Remote
```bash
# Push local branch changes to GitHub (set upstream on first push)
git push -u origin main

# Pull remote changes and merge them locally
git pull origin main
```

### Branching & Merging
```bash
# List all local branches
git branch

# Create a new branch
git branch feature-api-integration

# Switch to the new branch
git checkout feature-api-integration

# Shortcut: Create and switch to new branch in one command
git checkout -b feature-api-integration

# Merge another branch into your current active branch
git merge feature-api-integration
```

---

## 2. Conventional Commits Standard

To build a professional repository, follow the **Conventional Commits** specification. This makes it easy for other developers (and automated release tools) to scan your commit history.

The structure of a conventional commit message is:
```text
<type>[optional scope]: <description>
```

### Common Commit Types:
*   `feat`: A new feature (e.g., `feat: add category filter to CLI expense tracker`)
*   `fix`: A bug fix (e.g., `fix: resolve crash when loading empty CSV files`)
*   `docs`: Documentation changes only (e.g., `docs: expand git workflow guide`)
*   `style`: Changes that do not affect the meaning of the code (formatting, missing semi-colons, white-space)
*   `refactor`: Code change that neither fixes a bug nor adds a feature (e.g., `refactor: clean up OOP classes for better encapsulation`)
*   `test`: Adding missing tests or correcting existing tests
*   `chore`: Changes to the build process, dependency updates, or auxiliary tools (e.g., `chore: update root requirements.txt`)

---

## 3. Resolving Merge Conflicts

A **merge conflict** occurs when Git cannot automatically decide which changes to keep. This usually happens when two developers modify the same lines of the same file in different branches.

### How Conflict Markers Look:
When a merge conflict occurs, Git halts the merge and inserts conflict markers directly into the affected files:

```python
<<<<<<< HEAD
print("User is logged in under local session.")
=======
print("User is authenticated via Clerk JWT token.")
>>>>>>> feature-auth
```

*   `<<<<<<< HEAD`: The start of your active branch's changes (what you currently have).
*   `=======`: The divider separating the local changes from the incoming changes.
*   `>>>>>>> feature-auth`: The end of the incoming branch's changes.

### Step-by-Step Resolution:
1.  Open the conflicted file in VS Code or Cursor. The editor will highlight conflicts in red and green and show helper buttons: `Accept Current Change`, `Accept Incoming Change`, `Accept Both Changes`.
2.  Choose which code block to keep, or edit the lines manually to combine them.
3.  **Delete the conflict marker lines** (`<<<<<<<`, `=======`, `>>>>>>>`).
4.  Save the file.
5.  Stage the resolved file:
    ```bash
    git add filename.py
    ```
6.  Complete the merge commit:
    ```bash
    git commit -m "merge: resolve conflict between main and feature-auth"
    ```

---

## 👥 4. GitHub Flow & Pull Requests (PRs)

When contributing to repositories or showing off your projects, follow the **GitHub Flow** workflow:

1.  **Branch:** Create a branch from `main` to work on your task (e.g., `git checkout -b feature-expense-csv`).
2.  **Commit:** Write code and make commits locally using the Conventional Commit standard.
3.  **Push:** Push your branch to GitHub (`git push -u origin feature-expense-csv`).
4.  **Pull Request:** Open a Pull Request (PR) on GitHub. Write a clear description of what your PR does, adding screenshot guides if there are visual changes.
5.  **Review & Merge:** Review the diff, run tests, and merge the PR into `main` on GitHub once verified.
