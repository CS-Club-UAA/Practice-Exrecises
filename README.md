# Practice Exercises
This repository records the practice exercises we do as a club. You'll find lots of short exercises of varying difficulty, in various languages, along with their solutions.

## Contributions

If you have a good exercise, feel free to add it! Put it in a folder for the language it's written in, and include these 3 elements:
 - `README.md` -> Explains the problem and what the user should do to try solving it
 - The code file
 - The solution

## Saving your solution

You can add your solution in the same folder as the exercise. Just create a separate file named with your username + Solution. For example:
- Arthur's Solution.py

As developers, it's always great to learn from each other. Learning never stops!

## Workflow for members

The `main` branch is protected: you can't push to it directly. Every change must go through a Pull Request (PR) and be approved by at least one other member before it can be merged.

1. **Get the latest code**
   ```bash
   git checkout main
   git pull origin main
   ```

2. **Create a new branch** for your change (use a short, descriptive name)
   ```bash
   git checkout -b your-name/short-description
   # example: git checkout -b arthur/two-sum-solution
   ```

3. **Make your changes and commit them**
   ```bash
   git add .
   git commit -m "Add solution for Two Sum in Python"
   ```

4. **Push your branch to GitHub**
   ```bash
   git push -u origin your-name/short-description
   ```

5. **Open a Pull Request**
   - Go to the repository on GitHub. You'll see a **Compare & pull request** button for your branch.
   - Add a clear title and a short description of what you changed.
   - Request a review from another club member under **Reviewers**.

6. **Address review feedback**
   - If the reviewer asks for changes, commit them to the same branch and push again. The PR updates automatically.

7. **Merge**
   - Once your PR has at least one approval, click **Merge pull request**.
   - Afterwards, you can delete your branch and switch back to `main`:
     ```bash
     git checkout main
     git pull origin main
     ```

> **Note:** You can't approve your own PR, so ask another member to review it.
