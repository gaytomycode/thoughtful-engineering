# Todo List

**Unit Test Status:** ![Build Status](https://github.com/gaytomycode/todo-list/actions/workflows/main.yml/badge.svg)

Todo List is a simple command-line application that allows users to manage their to-do list.

## Table of Contents

- [Features](#features)
- [How to Use](#how-to-use)
- [Developing](#developing)
- [Contributing](#contributing)

## Features

This application allows you to:

- Add a new task to your todo list.
- Remove a task from your todo list.
- View all the tasks in your todo list.

## How to Use

To use the tool, launch the application and interact with it in your terminal. Here are the commands you can use:

- `add [task]`: This command adds a new task to your todo list.
- `remove [task]`: This command removes a task from your todo list. If the task is not found in the list, an appropriate message will be shown.
- `view`: This command shows all the tasks currently in your todo list.
- `quit`: This command exits the application.

Replace `[task]` with the task that you want to add or remove. For instance, `add Wash clothes`.

## Developing

For any further development on this project, please make sure that the existing application functions as expected. Run the suite of unit tests to verify this:

```bash
pytest --cov
```

This will report which tests pass and which tests fail. Make sure all current tests pass before adding new features.

If you add any new features, please also create appropriate unit tests.

## Contributing

Contributions to this project are welcome! Please fork this repository and open a Pull Request to propose your changes.
