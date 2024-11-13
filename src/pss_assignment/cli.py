from tms import Task, TaskManager
import argparse
from datetime import datetime, timezone


def main():
    parser = argparse.ArgumentParser(description="Task Management System CLI")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("--title", "-t", required=True, help="Task title")
    add_parser.add_argument(
        "--description", "-d", required=True, help="Task description"
    )

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument(
        "--uuid", "-u", required=True, type=int, help="Task UUID"
    )

    subparsers.add_parser("list", help="List all tasks")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    manager = TaskManager()

    if args.command == "add":
        current_time = datetime.now(timezone.utc).isoformat()
        task = Task(title=args.title, description=args.description, time=current_time)
        manager.add_task(task)
        print(f"Added task with UUID: {task.uuid}\nCreation time: {task.time}")

    elif args.command == "delete":
        if manager.delete_task(args.uuid):
            print(f"Deleted task with UUID: {args.uuid}")
        else:
            print(f"No task found with UUID: {args.uuid}")

    elif args.command == "list":
        tasks = manager.list_tasks()
        if not tasks:
            print("No tasks found")
            return

        output = []
        for task in tasks:
            output.append(
                f"UUID: {task.uuid}\n"
                f"Title: {task.title}\n"
                f"Description: {task.description}\n"
                f"Created: {task.time}\n"
                f"{'-' * 40}"
            )
        print("\n".join(output))


if __name__ == "__main__":
    main()
