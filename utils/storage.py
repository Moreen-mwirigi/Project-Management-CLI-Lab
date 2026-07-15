import json
import os
from models.user import User
from models.project import Project
from models.task import Task

DATA_FILE = "data/data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return [], [], []
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("warning: data.json corrupted. Starting fresh.")
        return [], []
    
    users = [User.from_dict(u) for u in data.get("users", [])]
    projects = [Project.from_dict(p) for p in data.get("projects", [])]
    tasks = [Task.from_dict(t) for t in data.get("tasks", [])]

    for u in users:
        u.projects = [p for p in projects if p.owner_email == u.email]
    for p in projects:
        p.tasks = [t for t in tasks if t.project_id == p.id]

    return users, projects, tasks

def save_data(users, projects, tasks):
    os.makedirs("data", exist_ok=True)
    data = {
        "users": [u.to_dict() for u in users],
        "projects": [p.to_dict() for p in projects],
        "tasks": [t.to_dict() for t in tasks]
    }
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")