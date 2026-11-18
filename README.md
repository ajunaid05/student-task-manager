# student-task-manager

Project status: Completed

A small Python console application for managing student tasks. It was built as
Lab Assignment 4 for **CSC418 DevOps for Cloud Computing** (COMSATS University
Islamabad, Lahore Campus) to practise a full Git and GitHub workflow.

## Features

- Add tasks (empty or whitespace-only titles are rejected)
- Display all tasks with status and a completed count
- Mark a task as completed (invalid IDs and already-completed tasks are handled)
- Delete a task by ID (invalid IDs are handled)
- Tasks are stored in a local `tasks.json` file
- Automated tests run on every push and pull request to `main` via GitHub Actions

## Setup

Requirements: Python 3.10 or newer. No third-party packages are needed.

```bash
git clone https://github.com/ajunaid05/student-task-manager.git
cd student-task-manager
```

## Usage

```bash
python task_manager.py
```

Choose an option from the menu:

| Option | Action |
|---|---|
| 1 | Add Task |
| 2 | View Tasks |
| 3 | Complete Task |
| 4 | Delete Task |
| 5 | Exit |

See [docs/user-guide.md](docs/user-guide.md) for a step-by-step guide.

## Running the tests

```bash
python -m unittest discover -s tests -v
```

## Project files

| Path | Purpose |
|---|---|
| `task_manager.py` | The application |
| `tests/` | unittest test cases |
| `.github/workflows/ci.yml` | GitHub Actions workflow |
| `docs/user-guide.md` | User guide |
| `LAB-REPORT.md` | Assignment report |
| `lab-evidence/` | Screenshots of key steps |

## License

Released under the [MIT License](LICENSE).
