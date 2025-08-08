import sys

#### VARIABLES####
tasks = []


#### FUNCTIONS####
def add_a_task(id):
    task_to_add = input("Enter your task : ").strip()
    status = 'PENDING'
    tasks.append({"id": id+1, "task": task_to_add, "status": status})


def view_tasks():
    for task in tasks:
        print(f'{task["id"]} | {task["task"]} | {task["status"]}')


def mark_task_as_completed(id):
    for task in tasks:
        if task["id"] == id:
            task["status"] = "COMPLETED"


def delete_a_task(id):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)


#### REAL FUNCTIONALITY####
while True:
    print('''
----------------
1. Add a task
2. View tasks
3. Mark task as done
4. Delete a task
5. Exit
----------------
''')

    user_choice = input("enter your choice: ").strip()
    if not user_choice.isnumeric():
        print("enter a numeric value")
        sys.exit()

    user_choice = int(user_choice)
    if user_choice not in (1, 2, 3, 4, 5):
        print("Choose option from 1-5")

    if user_choice == 1:
        add_a_task(len(tasks))
    if user_choice == 2:
        view_tasks()
    if user_choice == 3:
        update_this_id = int(input("which task (enter the id) : ").strip())
        mark_task_as_completed(update_this_id)
    if user_choice == 4:
        update_this_id = int(input("which task (enter the id) : ").strip())
        delete_a_task(update_this_id)
    if user_choice == 5:
        sys.exit()
