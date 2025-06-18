import sys

TASKS_FILE = "tasks.txt"

def read_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = f.read().splitlines()
        return tasks
    except FileNotFoundError:
        return []

def write_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task(task):
    tasks = read_tasks()
    tasks.append(task)
    write_tasks(tasks)
    print(f"Adăugat: {task}")

def list_tasks():
    tasks = read_tasks()
    if not tasks:
        print("Niciun task.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

def remove_task(index):
    tasks = read_tasks()
    try:
        removed = tasks.pop(index - 1)
        write_tasks(tasks)
        print(f"Șters: {removed}")
    except IndexError:
        print("Index invalid.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Comenzi: add [task], list, remove [număr]")
    elif sys.argv[1] == "add":
        add_task(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "list":
        list_tasks()
    elif sys.argv[1] == "remove":
        try:
            index = int(sys.argv[2])
            remove_task(index)
        except ValueError:
            print("Trebuie să fie un număr.")
