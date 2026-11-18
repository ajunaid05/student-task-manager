# Lab Report - Assignment 4

**Course:** CSC418 DevOps for Cloud Computing
**Student:** Ahmad Junaid (FA23-BSE-019)
**Repository:** https://github.com/ajunaid05/student-task-manager

## 1. Git vs GitHub; add, commit, push

Git is the version control tool that runs on my computer and records the history of my files. GitHub is an online service that hosts Git repositories and adds things like Issues, Pull Requests and Actions. `git add` puts changed files into the staging area, `git commit` saves those staged changes as a snapshot with a message, and `git push` uploads my local commits to the remote repository on GitHub.

## 2. Branches, Pull Requests and merge conflicts

Branches let me work on a feature separately without breaking `main`. In this project each feature (add, complete, delete) had its own branch. A Pull Request is how I ask for a branch to be merged: it shows the changed files, allows review comments, and can run automatic tests before merging. A merge conflict happens when two branches change the same lines of the same file differently, so Git cannot decide which version to keep. I created one on purpose by changing the README status line differently on two branches.

## 3. Fetch vs pull, merge vs rebase

`git fetch` downloads new commits from the remote but does not change my working files. `git pull` does a fetch and then merges those changes into my current branch. A merge combines two branches by creating a merge commit and keeps the full history as it happened. A rebase replays my commits on top of another branch, which gives a straight, linear history but rewrites commits.

## 4. GitHub Issues and Actions

Issues track tasks, bugs and ideas in one place, with labels, so the team knows what needs to be done and who is working on it. Pull Requests can be linked to Issues so they close automatically. GitHub Actions runs workflows automatically, for example running the tests on every push and pull request, which catches bugs early. In this project the first CI run failed because of a real bug in `complete_task`, and it passed after the fix.

## 5. One difficulty and how I solved it

When I tried to push the GitHub Actions workflow file, GitHub rejected it because my access token did not have the `workflow` permission. I solved it by adding `.github/workflows/ci.yml` directly through the GitHub website on the feature branch instead. I also had conflicts in the header comment of `task_manager.py` when merging the feature branches, which I solved by merging `main` into each branch and keeping both features.
