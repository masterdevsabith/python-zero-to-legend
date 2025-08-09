import sys

print('''
----------------
1. Add a task
2. View tasks
3. Mark task as done
4. Delete a task
5. Menu
6. Exit
----------------
''')

#### VARIABLES####
tasks = []


#### FUNCTIONS####
def add_a_task():
    task_to_add = input("Enter your task : ").strip().lower()
    status = 'PENDING'
    tasks.append({"task": task_to_add, "status": status})


def view_tasks():
    for index, task in enumerate(tasks, start=1):
        print(f'{index} | {task["task"]} - {task["status"]}')


def mark_task_as_completed(id):
    if id < 0 or id >= len(tasks):
        print("Invalid ID")
    elif id <= len(tasks):
        for index, task in enumerate(tasks[:], start=0):
            if index == id:
                tasks[index]['status'] = 'DONE'


def delete_a_task(id):
    if id < 0 or id >= len(tasks):
        print("Invalid ID")
    elif id <= len(tasks):
        for index, task in enumerate(tasks[:], start=0):
            if index == id:
                tasks.remove(tasks[index])


def see_menu_options():
    print('''
----------------
1. Add a task
2. View tasks
3. Mark task as done
4. Delete a task
5. Menu
6. Exit
----------------
''')

    #### REAL FUNCTIONALITY####
while True:
    user_choice = input("enter your choice: ").strip()
    if not user_choice.isnumeric():
        print("enter a numeric value")

    user_choice = int(user_choice)
    if user_choice not in (1, 2, 3, 4, 5, 6):
        print("Choose option from 1-6")

    if user_choice == 1:
        add_a_task()
    if user_choice == 2:
        view_tasks()
    if user_choice == 3:
        update_this_id = input("which task DONE ? (enter the id) : ").strip()

        if not update_this_id.isnumeric():
            print("Enter a valid ID")
        else:
            update_this_id = int(update_this_id)
            mark_task_as_completed(update_this_id-1)
    if user_choice == 4:
        delete_this_id = input(
            "which task to delete ? (enter the id) : ").strip()
        if not delete_this_id.isnumeric():
            print("Enter a valid ID")
        else:
            delete_this_id = int(delete_this_id)
            delete_a_task(delete_this_id-1)
    if user_choice == 5:
        see_menu_options()
    if user_choice == 6:
        sys.exit()
