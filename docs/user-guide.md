# User Guide

## Starting the program

Open a terminal in the project folder and run:

```bash
python task_manager.py
```

You will see a menu with five options.

## Adding a task

1. Choose option **1**.
2. Type the task title and press Enter.
3. If the title is empty, the program shows an error and nothing is saved.

## Viewing tasks

Choose option **2**. Each task is shown as `[ID] status title`.
`○` means pending and `✓` means completed. The header shows how many tasks are done.

## Completing a task

1. Choose option **3**. The task list is shown first.
2. Enter the numeric ID of the task.
3. If the ID does not exist, or the task is already completed, a message is shown.

## Deleting a task

1. Choose option **4**. The task list is shown first.
2. Enter the numeric ID of the task to delete.
3. If the ID does not exist, nothing is changed and an error is shown.

## Exiting

Choose option **5**.

## Where data is stored

Tasks are saved in `tasks.json` in the folder where you run the program.
Delete that file to start fresh.
