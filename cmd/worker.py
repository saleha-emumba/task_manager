import argparse
from typing import Optional
from storage.json_storage import JSONStorage
from models.task import Task, TaskCollection
from utils.decorators import timeit, validate_not_empty


STORAGE_FILE = "storage/storage_file/tasks.json"


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Modular Task Manager")
    sub = p.add_subparsers(dest="cmd")

    add = sub.add_parser("add")
    add.add_argument("title")
    add.add_argument("--desc", "-d", default="")
    add.add_argument("--due", default=None)

    sub.add_parser("list").add_argument("--all", action="store_true")

    comp = sub.add_parser("complete")
    comp.add_argument("id", type=int)

    rem = sub.add_parser("remove")
    rem.add_argument("id", type=int)

    return p


def cli(argv: Optional[list[str]] = None) -> None:
    parser = _build_parser()
    args = parser.parse_args(argv)

    storage = JSONStorage(STORAGE_FILE)
    collection = TaskCollection(storage.load())

    if args.cmd == "add":
        task = Task.create(title=args.title, description=args.desc, due_date=args.due)
        collection.add(task)
        storage.save(collection.to_list())
        print(f"Added task: {task.id} - {task.title}")

    elif args.cmd == "list":
        for t in collection:
            status = "✓" if t.completed else " "
            if hasattr(args, "all") and args.all:
                print(
                    f"{t.id}: [{status}] {t.title} - description: '{t.description}' - due: {t.due_date}"
                )

            else:
                print(f"{t.id}: [{status}] {t.title} -- due: {t.due_date}")

    elif args.cmd == "complete":
        if collection.mark_completed(args.id):
            storage.save(collection.to_list())
            print(f"Marked {args.id} completed")

        else:
            print(f"Task {args.id} not found")

    elif args.cmd == "remove":
        if collection.remove(args.id):
            storage.save(collection.to_list())
            print(f"Removed {args.id}")

        else:
            print(f"Task {args.id} not found")

    else:
        parser.print_help()
