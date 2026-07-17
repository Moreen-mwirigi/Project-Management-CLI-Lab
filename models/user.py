class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def email (self):
        return self._email
    
    @email.setter
    def email (self, value):
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email format")
        self._email = value

    def __str__(self):
        return f"{self.name} < {self.email}>"
        pass
        pass
    
class User(Person):
    _id_counter = 1
    def __init__(self, name, email):
        super().__init__(name, email)
        self.id = User._id_counter
        User._id_counter += 1
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "project_ids":[p.id for p in self.projects]
        }
    @classmethod
    def from_dict(cls, data):
        user = cls(data["name"], data["email"])
        user.id = data["id"]
        user._id_counter = max(User._id_counter, data["id"] + 1)
        return user
    
    def __str__(self):
        return f"User [{self.id}]: {self.name} <{self.email}>"