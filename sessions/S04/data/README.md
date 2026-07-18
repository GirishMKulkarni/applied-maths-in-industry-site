# Data for S04 — there isn't any, and that is the point

This session has **no dataset**. The three notebooks use only tiny examples typed
straight into the cells, so they run anywhere with no downloads.

What this folder holds instead is a **cheat-sheet of the Git commands** for the
lab. The first notebook, `notebooks/01_git_save_points.ipynb`, already runs these
for you inside a throwaway folder so you can watch them work. Here they are in one
place, in the order you will actually type them when you publish your own repo.
Work through them once on a throwaway folder, then again for real in the lab.

Remember the picture: a **commit** is a save point that keeps your whole project at
that moment. GitHub is where those save points live online, so the work is safe and
shareable.

## The five commands you'll use 95% of the time

```bash
git init                 # start watching this folder (creates the hidden .git history)
git add <file>           # put a change on the "tray" for the next save point
git commit -m "message"  # freeze the tray as a save point, with a note on what changed
git push                 # send your save points up to GitHub (so they are safe and shared)
git pull                 # bring teammates' save points down to your copy
```

## A first repository, start to finish

```bash
# 1. Make a folder and start watching it.
mkdir my-first-repo
cd my-first-repo
git init

# 2. Tell Git who you are (only needed once per machine).
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"

# 3. Add the template files (see ../repo-template/) and check what changed.
git status               # shows what is new or modified
git add README.md requirements.txt
git status               # the files are now staged (on the tray)

# 4. Make your first save point.
git commit -m "Add README and requirements"

# 5. See your history — these are your save points.
git log --oneline

# 6. Connect to GitHub and push (create the empty repo on GitHub first).
git remote add origin https://github.com/<your-username>/my-first-repo.git
git branch -M main
git push -u origin main
```

## Useful day-to-day

```bash
git status               # what has changed and what is staged
git log --oneline        # your save points, one line each
git diff                 # the exact lines you changed but have not staged yet
git branch my-experiment # make a parallel line of history to try something
git switch my-experiment # move onto that branch
git switch main          # go back to the main line
```

## Keep junk OUT of the repo — use a `.gitignore`

Never commit your virtual environment, large data files, or secrets (API keys,
passwords). A committed secret stays in the history forever, even if you delete the
file later. Create a file called `.gitignore` with lines like:

```
.venv/
__pycache__/
*.csv
.env
```

## Remember

- **Commit often**, in small focused save points, each with a clear message.
- A commit should do **one thing**; giant commits are impossible to review.
- Write the `README.md` first — it is the front page a recruiter actually reads.
- See [`../repo-template/`](../repo-template/) for a README and `requirements.txt`
  you can copy as a starting point.
