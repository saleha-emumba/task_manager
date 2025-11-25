import json
from typing import List, Dict
from utils.contextmanagers import open_json


class JSONStorage:
    def __init__(self, path: str) -> None:
        self.path = path

    def load(self) -> List[Dict]:
        try:
            with open_json(self.path, "r") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    return []

                return data

        except FileNotFoundError:
            return []

    def save(self, tasks: List[Dict]) -> None:
        with open_json(self.path, "w") as f:
            json.dump(tasks, f, indent=2)
