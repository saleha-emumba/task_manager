from models.task import TaskCollection, Task


def test_add_and_iter():
    c = TaskCollection()
    t = Task.create("t1")
    c.add(t)
    assert len(list(c)) == 1


def test_mark_complete_and_remove():
    c = TaskCollection()
    t = c.add(Task.create("t2"))
    assert c.mark_completed(t.id) is True
    assert c.remove(t.id) is True
