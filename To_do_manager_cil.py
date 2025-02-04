import argparse
import json
import os

#Name a file to store tasks
TASKS_FILE = 'tasks.json'

#To load tasks from the JSON file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

#To save tasks to the JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

#To add a new task
def add_task(describe):
    tasks = load_tasks()
    tasks.append({'id': len(tasks) + 1, 'describe': describe, 'completed': False})
    save_tasks(tasks)
    print(f' Task added successfully: "{describe}"')

#To update an existing task
def update_task(task_id, new_describe):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['describe'] = new_describe
            save_tasks(tasks)
            print(f' Task updated successfully: "{new_describe}"')
            return
    print(f' Sorryyyy, task with ID {task_id} not found.')

#To delete a task
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f'Task with ID {task_id} has been deleted.')

#To list all tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print('No tasks found!!!!!. Let’s add some!')
        return
    print("Here are your current tasks.Lets begin!!!:")
    for task in tasks:
        status = '✅' if task['completed'] else '❌'
        print(f"[{status}] ID {task['id']}: {task['describe']}")


def main():
    parser = argparse.ArgumentParser(description='Welcome to your personal to-do list manager! ')
    parser.add_argument('--add', type=str, help='Add a new task to your list')
    parser.add_argument('--update', type=int, help='Update an existing task by ID')
    parser.add_argument('--describe', type=str, help='New description for the task')
    parser.add_argument('--delete', type=int, help='Delete a task by ID')
    parser.add_argument('--list', action='store_true', help='List all your tasks')

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.update and args.describe:
        update_task(args.update, args.describe)
    elif args.delete:
        delete_task(args.delete)
    elif args.list:
        list_tasks()
    else:
        print(" Hmmmmmmmm, it seems like something went wrong. Please use one of the following commands:")
        parser.print_help()


main()