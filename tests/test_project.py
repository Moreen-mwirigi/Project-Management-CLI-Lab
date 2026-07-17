from models.project import Project
from models.task import Task

def test_project_creation():
    p = Project("Website", "Build site", "alex@mail.com", "2026-08-07")
    assert p.title == "Website"
    assert p.get_progress() == 0

def test_project_progress():
    p = Project("App", "Build app", "alex@mail.com", "2026-08-07")
    t1 = Task("Design", p.id)
    t2 = Task("Code", p.id)
    t1.complete()
    p.add_task(t1)
    p.add_task(t2)
    assert p.get_progress() == 50

def test_due_date_parsing():
    p = Project("Test", "Desc", "alex@mail.com", "2026-08-07")
    assert str(p.due_date) == "2026-08-07"
    
