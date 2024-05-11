import datetime
import json
import requests

def display_menu():
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Exit")

def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append({"task": task, "done": False, "time": None})
    print("Task added succesfully!")

def view_tasks(todo_list):
    if not todo_list:
        print("No tasks yet!")
    else:
        for idx, task in enumerate(todo_list):
            status = "Done" if task["done"] else "Not done"
            completition_time = task["time"].strftime("%Y-%m-%d %H:%M:%S") if task["time"] else "N/A"
            print(f"{idx+1}. {task['task']} - {status} - Completion time: {completition_time}")
    
def mark_task_as_done(todo_list):
    view_tasks(todo_list)
    task_idx = int(input("Enter the index of the task to mark as done: ")) -1
    if 0 <= task_idx < len(todo_list):
        todo_list[task_idx]["done"] = True
        todo_list[task_idx]["time"] = datetime.datetime.now()
        print("Task marked as done!")
    else:
        print("Invalid task index.")

def fetch_tasks_from_server():
    try:
        response = requests.get('https://your-server-endpoint/tasks')
        response.raise_for_status()
        tasks = response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching tasks:", e)
        tasks = []
    return tasks

def send_updates_to_server(updated_tasks):
    try:
        response = requests.post('https://your-server-endpoint/tasks', json=updated_tasks)
        response.raise_for_status()
        print("Tasks updated successfully!")
    except requests.exceptions.RequestException as e:
        print("Error updating tasks:", e)


def main():
    todo_list = fetch_tasks_from_server()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            view_tasks(todo_list)
        elif choice == "3":
            mark_task_as_done(todo_list)
        elif choice == "4":
            send_updates_to_server(todo_list)
            print("Exiting...")
            break
        else:
            print("Wrong answer. Try again. ;)")
    
if __name__ == "__main__":
    main()
