from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Iterable, Iterator, List, Optional


@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    due_date: Optional[str] = None
    completed: bool = False

    @staticmethod
    def create(title: str, description: str = "", due_date: Optional[str] = None):
        return Task(id=-1, title=title, description=description, due_date=due_date)


class TaskCollection:
    def __init__(self, tasks: Optional[List[dict]] = None) -> None:
        self._tasks: List[Task] = []
        self._next_id = 1
        if tasks:
            for t in tasks:
                task = Task(**t)
                self._tasks.append(task)
                self._next_id = max(self._next_id, task.id + 1)

    def add(self, task: Task) -> Task:
        task.id = self._next_id
        self._next_id += 1
        self._tasks.append(task)
        return task

    def to_list(self) -> List[dict]:
        return [asdict(t) for t in self._tasks]

    def __iter__(self) -> Iterator[Task]:
        return iter(self._tasks)

    def iter_filtered(self, completed: Optional[bool] = None) -> Iterator[Task]:
        for t in self._tasks:
            if completed is None or t.completed == completed:
                yield t

    def mark_completed(self, task_id: int) -> bool:
        for t in self._tasks:
            if t.id == task_id:
                t.completed = True
                return True

        return False

    def remove(self, task_id: int) -> bool:
        for i, t in enumerate(self._tasks):
            if t.id == task_id:
                del self._tasks[i]
                return True

        return False
