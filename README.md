# Project Management CLI
A command-line tool to manage users, projects and tasks With persistent JSON storage. Built with OOP, encapsulation and tested with pytest.

## Features
**User Management**: Create users with email validation.
**Project Management**: Create projects with due dates and track progress %.
**Task Management**: Add tasks to projects, update status: TODO, IN_PROGRESS, DONE.
**Persistent Storage**: Sll ddata saved to `data/data.json`
**Rich UI**: Table output using `rich`
**Tested**: Pytest tests covering all models.

## Installation.
1. Clone the repository.
2. Install dependencies with Pipenv
    pipenv install
    pipenv installrich pytest
3. Activate the virtyal environment.
    pipenv shell

## Usage
- Run all commands with :
    pipenv run `python main.py <command> [option]`
1. Add User
    pipenv run `python main.py add-user --name "Alex" --email "alex@mail.com"`
2. Add a Project
    pipenv run `python main.py add-project --title "Application" --desc "Build portifolio" --email "alex@mail.com" --due "2026-12-31"`
3. List Projects for a user
    pipenv run `python main.py list-projects --email"alex@mail.com"`
4. Add a Task to a project
    pipenv run `python main.py add-task --title "Desig UI" --project-id 1`
5. Update Task Status
    pipenv run `python main.py update-task --task-id 1 --status IN_PROGRESS`
6. Complete a Task
    pipenv run `python main.py complete-task --task-id 1`

## Running Tests
- Run all tests to verify functionality:
    `pipenv run pytest -v`
Tests cover:
- test_project.py: Project creation, progress calculation.
- test_task.py: Task status changes, validation
- test_user.py: User creation, email validation, encapsulation

## Project Structure
Project-Management-Cli
|- data/
    data.json # Persistent storage
|- models/
    __init__.py
    user.py # User + Person classes with validation
    project.py # Project class with progress logic
    task.py # Task class with status encapsulation
|- tests/
    __init__.py
    test_user.py
    test_project.py
    test_task.py
|- utils/
    __init__.py
    storage.py # JSON load/save functions
|- main.py # CLI entry pointwith argparse
|- pipfile 
|- READNE.md
|- requirements.txt
