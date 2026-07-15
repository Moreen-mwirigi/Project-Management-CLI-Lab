class Task:
    _id_counter = 1

    def __init__(self, title, project_id):
        self.id = Task._id_counter
        Task._id_counter += 1
        self.title = title
        self.project_id = project_id
        self._status = "TODO"

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        if value not in ["TODO", "IN_PROGRESS", "DONE"]:
            raise ValueError("Status must be TODO, IN_PROGRESS, or DONE")
        self._status = value

    def complete(self):
        self.status = "DONE"

    def to_dict(self):
        return {"id": self.id, "title": self.title, "project_id": self.project_id, "status": self.status}
    
    @classmethod
    def from_dict(cls, data):
        t = cls(data["title"], data["project_id"])
        t.id = data["id"]
        t.status = data["status"]
        Task._id_counter = max(Task._id_counter, data["id"] + 1)
        return t
    
    def __str__(self):
        return f"Task[{self.id}]: {self.title} - {self.status}"
        pass