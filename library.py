import json


class Library:
    def __init__(self, json_path: str) -> None:
        try:
            with open(json_path, "r") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}

    def count_books(self) -> int:
        return len(self.data["books"])
