import pytest
from models.user import User

def test_user_creation():
    user = User("Bob", "bob@gmail.com")
    assert user.name == "Bob"
    assert user.email == "bob@gmail.com"

def test_email_validation():
    with pytest.raises(ValueError):
        User("Bob", "bademail")

def test_add_project():
    user = User("Alex", "alex@mail.com")
    from models.project import Project
    p = Project("CLI", "Build CLI", "alex@mail.com", "2026-01-01")
    user.add_project(p)
    assert len(user.projects) == 1
    
    