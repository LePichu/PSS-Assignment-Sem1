from dataclasses import dataclass, asdict, field
from typing import List, Optional
import json
from uuid import uuid4
from pathlib import Path
from datetime import datetime


@dataclass
class Task:
    title: str
    description: str
    time: str
    uuid: int = field(default_factory=lambda: uuid4().int)

    def __post_init__(self):
        try:
            datetime.fromisoformat(self.time)
        except ValueError:
            raise ValueError(
                f"Invalid ISO 8601 time format. Expected format: YYYY-MM-DDTHH:MM:SS+HH:MM. Got: {self.time}"
            )


class TaskManager:
    STORAGE_PATH = Path("tms.data.json")

    def __init__(self):
        self.tasks: List[Task] = []
        self.load()

    def add_task(self, task: Task) -> Task:
        self.tasks.append(task)
        self.offload()
        return task

    def get_task(self, uuid: int) -> Optional[Task]:
        return next((task for task in self.tasks if task.uuid == uuid), None)

    def update_task(self, uuid: int, **kwargs) -> Optional[Task]:
        if "time" in kwargs:
            try:
                datetime.fromisoformat(kwargs["time"])
            except ValueError as e:
                raise ValueError(
                    f"Invalid ISO 8601 time format. Expected format: YYYY-MM-DDTHH:MM:SS+HH:MM. Got: {kwargs['time']}"
                )

        task = self.get_task(uuid)
        if task:
            for key, value in kwargs.items():
                if hasattr(task, key):
                    setattr(task, key, value)
            self.offload()
            return task
        return None

    def delete_task(self, uuid: int) -> bool:
        task = self.get_task(uuid)
        if task:
            self.tasks.remove(task)
            self.offload()
            return True
        return False

    def list_tasks(self) -> List[Task]:
        return self.tasks

    def offload(self) -> None:
        data = [asdict(task) for task in self.tasks]
        with self.STORAGE_PATH.open("w") as f:
            json.dump(data, f, indent="\t")

    def load(self) -> None:
        if self.STORAGE_PATH.exists():
            with self.STORAGE_PATH.open("r") as f:
                data = json.load(f)
                self.tasks = [Task(**task_dict) for task_dict in data]
