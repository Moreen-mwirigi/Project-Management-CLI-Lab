import pytest
from models.task import Task

def test_task_creation():
    t = Task("Write code", 1)
    assert t.title == "Write code"
    assert t.status == "TODO"

def test_task_status_encapsulation():
    t = Task("Test", 1)
    t.status = "IN_PROGRESS"
    assert t.status == "IN_PROGRESS"

def test_invalid_status():
    t = Task("Test", 1)
    with pytest.raises(ValueError):
        t.status = "INVALID"

def test_complete_method():
    t = Task("Finish", 1)
    t.complete()
    assert t.status == "DONE"
    