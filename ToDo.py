#!/usr/bin/env python3
"""
To-Do List
Tasks are stored in 'tasks.json' in the same folder.
"""

import json
import os
from datetime import datetime

FILE = "tasks.json"

# --------------------------------------------------
# Storage helpers
# --------------------------------------------------
def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

# --------------------------------------------------
# Core actions
# --------------------------------------------------
def add_task(tasks):
    title = input("Task description: ").strip()
    if not title:
        print("❌  Empty task, cancelled.")
        return
    tasks.append({
        "id": len(tasks) + 1,
        "title": title,
        "done": False,
        "created": datetime.now().isoformat(sep=" ", timespec="minutes")
    })
    print("✅  Task added.")

def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for t in tasks:
        status = "✓" if t["done"] else " "
        print(f"{t['id']:>2}. [{status}] {t['title']}  ({t['created']})")

def toggle_task(tasks):
    list_tasks(tasks)
    try:
        idx = int(input("ID to toggle: "))
        task = next(t for t in tasks if t["id"] == idx)
        task["done"] = not task["done"]
        print("✅  Updated.")
    except (StopIteration, ValueError):
        print("❌  Invalid ID.")

def delete_task(tasks):
    list_tasks(tasks)
    try:
        idx = int(input("ID to delete: "))
        tasks[:] = [t for t in tasks if t["id"] != idx]
        # Re-number IDs
        for i, t in enumerate(tasks, 1):
            t["id"] = i
        print("🗑️  Deleted.")
    except ValueError:
        print("❌  Invalid ID.")

# --------------------------------------------------
# Main menu loop
# --------------------------------------------------
MENU = """
========== TO-DO LIST ==========
1. Add task
2. List tasks
3. Toggle done/undone
4. Delete task
0. Exit
================================
Choice: """

def main():
    tasks = load_tasks()
    while True:
        choice = input(MENU).strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            toggle_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "0":
            save_tasks(tasks)
            print("Bye!")
            break
        else:
            print("Invalid option.")
        save_tasks(tasks)

if __name__ == "__main__":
    main()