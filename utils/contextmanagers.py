import os
from contextlib import contextmanager
from typing import Iterator, IO


@contextmanager
def open_json(path: str, mode: str = "r") -> Iterator[IO]:
    if "w" in mode:
        os.makedirs(os.path.dirname(os.path.abspath(path)) or ".", exist_ok=True)

    f = open(path, mode, encoding="utf-8")
    try:
        yield f
    finally:
        f.close()


class TimerContext:
    def __init__(self, label: str = "block") -> None:
        self.label = label

    def __enter__(self):
        import time

        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        import time

        elapsed = time.perf_counter() - self.start
        print(f"{self.label} took {elapsed:.4f}s")
        return False
