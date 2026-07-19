import argparse
import logging
from rich.table import Table
from rich.console import Console
from utils.storage import load_data, save_data
from models.user import User
from models.project import Project
from models.task import Task

logging.basicConfig(filename="debug.log", level=logging.INFO, format="%(asctime)s - %(message)s")
console = Console

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI")
    subparsers = parser.add_subparsers(dest="command")

    p1 = subparsers.add_parser("add-user")
    p1.add_argument("--name", required=True)
    p1.add_argument("--email", required=True)

    p2 = subparsers.add_parser("add-project")
    p2.add_argument("--email", required=True)
    p2.add_argument("--title", required=True)
    p2.add_argument("--desc", required=True)
    p2.add_argument("--due", required=True)

    p3 = subparsers.add_parser("add-task")
    p3.add_argument("--project-id", type=int, required=True)
    p3.add_argument("--title", required=True)

    p4 = subparsers.add_parser("list-projects")
    p4.add_argument("--email", required=True)

    p5 = subparsers.add_parser("update-task")
    p5.add_argument("--task-id", type=int, required=True)
    p5.add_argument("--status", required=True, choices=['TODO', 'IN_PROGRESS', 'DONE'])

    p6 = subparsers.add_parser("complete-task")
    p6.add_argument("--task-id", type=int, required=True)

    args = parser.parse_args()
    users, projects, tasks = load_data()

    if args.command == "add-user":
        user = User(args.name, args.email)
        users.append(user)
        logging.info(f"Added user {user.email}")
        print(f"User added: {user}")
        save_data(users, projects, tasks)

    elif args.command == "add-project":
        user = next((u for u in users if u.email == args.email), None)
        if not user: parser.error("User not found")
        project = Project(args.title, args.desc, args.email, args.due)
        projects.append(project)
        user.add_project(project)
        print(f"Project added: {project}")

    elif args.command == "add-task":
        project = next((p for p in projects if p.id == args.project_id), None)
        if not project: parser.error("Project not found")
        task = Task(args.title, args.project_id)
        tasks.append(task)
        project.add_task(task)
        print(f"Task added: {task}")

    elif args.command == "list-projects":
        console = Console()
        table = Table(title=f"Projects for {args.email}")
        table.add_column("ID")
        table.add_column("Title")
        table.add_column("Progress")
        for p in [p for p in projects if p.owner_email == args.email]:
            table.add_row(str(p.id), p.title, f"{p.get_progress()}%")
        console.print(table)

    elif args.command == "complete-task":
        task = next((t for t in tasks if t.id == args.task_id), None)
        if not task: parser.error("Task not found")
        task.complete()
        print(f"Task completed: {task}")

    save_data(users, projects, tasks)

if __name__ == "__main__":
    main()