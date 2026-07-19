from datetime import datetime
#from dateutil import parser

class Project:
    _id_counter = 1

    def __init__(self, title, description, owner_email, due_date):
        self.id = Project._id_counter
        Project._id_counter += 1
        self.title = title
        self.description = description
        self.owner_email = owner_email
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_progress(self):
        if not self.tasks: return 0
        done = len([t for t in self.tasks if t.status == "DONE"])
        return int((done / len(self.tasks)) * 100)
    
    def to_dict(self):
        return {
            "id": self.id, "title": self.title, "description": self.description,
            "owner_email": self.owner_email, "due_date": str(self.due_date),
            "task_ids": [t.id for t in self.tasks]
        }
    
    @classmethod
    def from_dict(cls, data):
        p = cls(data["title"], data["description"], data["owner_email"], data["due_date"])
        p.id = data["id"]
        Project._id_counter = max (Project._id_counter, data["id"] + 1)
        return p
    
    def __str__(self):
        return f" Project[{self.id}]: {self.title} - {self.get_progress()}% done"
        pass
        pass