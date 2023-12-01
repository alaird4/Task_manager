# =====importing libraries===========
'''This is the section where you will import libraries'''
import datetime
import os

# ====Functions====


def reg_user():
    # only proceed if username is equal to admin to register new user
    if menu == "r" and username == 'admin':
        # ask the user to enter a new username and password
        new_username = input("Please enter a new username:")
        new_password = input("Please enter a new password:")
        confirm_password = input("Please confirm your new password:")

        # if the new password matches the confirmed password, proceed
        if new_password == confirm_password:
            # check if the new username already exists in user.txt
           
            with open("user.txt", "r") as file:
                current_usernames = [line.strip().split(", ")[0].strip() for line in file.readlines()]

            if new_username in current_usernames:
                print("Sorry, username already exists. Please try another!")
            else:
                # Add the new user to the user.txt file
                with open("user.txt", "a") as file:
                    file.write(f"\n{new_username}, {new_password}")
                print("New user has been successfully set up!")
        else:
            print("Password does not match! Please try another password")


def add_task():

    if menu == "a":
        # ask user to enter task information
        username = input("Enter the username of the assignee: ")
        title = input("Enter the title of the task: ")
        description = input("Enter a description of the task: ")
        due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
        status = "no"

    # use datetime import for the current date
    current_date = datetime.date.today()

    # write the task information to "tasks.txt" with the completion status set to 'No'
    with open("tasks.txt", "a") as file:
        file.write(f"\n{username}, {title}, {description},  {due_date}, {current_date}, {status}")
    
    print("Task has been added!")


def view_all():
    if menu == 'va':
        try:
            # open "tasks.txt" for reading
            with open("tasks.txt", "r") as file:
                tasks_data = file.read()

            # split the tasks data into individual tasks using a single new line
            tasks = tasks_data.strip().split("\n")
            # if no tasks, print no tasks found
            if not tasks:
                print("No tasks found.")
            else:
                print("Tasks:")
                # use enumerate to number tasks
                for index, task in enumerate(tasks, start=1):
                    task_lines = task.split(', ')
                    # how to print out the lines per task
                    print(f"{index}:")
                    print(f"   Assigned to: {task_lines[0].strip()}")
                    print(f"   Title: {task_lines[1].strip()}")
                    print(f"   Description: {task_lines[2].strip()}")
                    print(f"   Assigned Date: {task_lines[3].strip()}")
                    print(f"   Due Date: {task_lines[4].strip()}")
                    print(f"   Status: {task_lines[5].strip()}")
                    print("-" * 40)
        # except error
        except FileNotFoundError:
            print("The 'tasks.txt' file does not exist.")


def view_mine(username):
   
    if menu == 'vm':
      
        with open('tasks.txt', 'r') as file:
            
            # create a dictionary to store task data by task number
            task_data = {}
        
            # use enumerate to number tasks
            for i, line in enumerate(file, start=1):
                # strip and split the data to read file
                data = line.strip().split(', ')
            
                # ensure that the line has the expected number of elements
                if len(data) == 6:
                    assigned_to, title, description, assign_date, due_date, status = data
                    # check if the task is assigned to the username entered
                    if assigned_to == username:
                        task_data[i] = {
                            "title": title,
                            "description": description,
                            "assign_date": assign_date,
                            "due_date": due_date,
                            "status": status
                        }
            # if no task data, let user know
            if not task_data:
                print("You have no tasks assigned to you.")

            else:
                print("The following tasks are assigned to you: ")

            # print tasks in easy to read format
            for task_number, task_info in task_data.items():
                print(f"{task_number}: Title: {task_info['title']}")
                print(f"   Description: {task_info['description']}")
                print(f"   Assigned Date: {task_info['assign_date']}")
                print(f"   Due Date: {task_info['due_date']}")
                print(f"   Status: {task_info['status']}")
                print()

            # ask the user to select a task by entering a task number
            selected_task = int(input("Please enter a task number (or -1 to return to the main menu): "))

            if selected_task == -1:
                # return to the main menu
                return
            elif selected_task in task_data:
                # if task number is valid show options
                print("1. Mark as Complete")
                print("2. Edit Task")
                action = int(input("Choose an action (1 for Mark as Complete, 2 for Edit Task): "))

                if action == 1:
                    # mark as complete
                    if task_data[selected_task]["status"] == "no":
                        task_data[selected_task]["status"] = "yes"
                        print("Task successfully marked as complete.")
                    else:
                        print("Task is already marked as complete.")
                elif action == 2:
                    # edit task (only if the task is not completed)
                    # ask user for edits to the task
                    if task_data[selected_task]["status"] == "no":
                        new_assigned_to = input("Enter new username of assignee: ")
                        new_due_date = input("Enter new due date (YYYY-MM-DD): ")
                        task_data[selected_task]["assigned_to"] = new_assigned_to
                        task_data[selected_task]["due_date"] = new_due_date
                        print("Task has been edited.")
                    else:
                        print("Task can't be edited as already marked as complete.")   
            else:
                print("Invalid task number.")


def generate_reports():
    try:
        # read tasks from "tasks.txt"
        with open("tasks.txt", "r") as file:
            tasks_data = file.read().strip()
            tasks = tasks_data.split("\n")

        # variables for task statistics
        total_tasks = len(tasks)
        total_completed_tasks = 0
        total_uncompleted_tasks = 0
        total_overdue_tasks = 0

        # use datetime import for the current date
        current_date = datetime.date.today()

        # calculate task statistics
        for task in tasks:
            task_data = task.split(', ')
            if len(task_data) >= 6:
                assigned_to, title, description, due_date_str, current_date, status = [s.strip() for s in task_data]
                # use datatime to establish current and due dates
                current_date = datetime.datetime.strptime(current_date, "%Y-%m-%d").date()
                due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()

                if status.lower() == "no":
                    total_uncompleted_tasks += 1
                    if due_date < current_date:
                        total_overdue_tasks += 1
                elif status.lower() == "yes":
                    total_completed_tasks += 1

        # calculate percentages
        percentage_incomplete = (total_uncompleted_tasks / total_tasks) * 100
        percentage_overdue = (total_overdue_tasks / total_tasks) * 100

        # generate "task_overview.txt" with task statistics
        with open("task_overview.txt", "w") as task_file:
            task_file.write("Task Overview\n")
            task_file.write("-" * 20 + "\n")
            task_file.write(f"Total tasks: {total_tasks}\n")
            task_file.write(f"Total completed tasks: {total_completed_tasks}\n")
            task_file.write(f"Total uncompleted tasks: {total_uncompleted_tasks}\n")
            task_file.write(f"Total overdue tasks: {total_overdue_tasks}\n")
            task_file.write(f"Percentage incomplete: {percentage_incomplete:.2f}%\n")
            task_file.write(f"Percentage overdue: {percentage_overdue:.2f}%\n")

        # read and count usernames from the provided tasks data
        usernames = set()
        for task in tasks:
            task_data = task.split(', ')
            if len(task_data) >= 6:
                assigned_to = task_data[0].strip()
                usernames.add(assigned_to)

        # variables for user statistics
        total_users = len(usernames)
        total_user_tasks = {username: 0 for username in usernames}
        total_user_completed_tasks = {username: 0 for username in usernames}

        # calculate user statistics
        for task in tasks:
            task_data = task.split(', ')
            if len(task_data) >= 6:
                assigned_to = task_data[0].strip()
                status = task_data[5].strip()
                due_date_str = task_data[3].strip()
                due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
                current_date = datetime.date.today()

                if assigned_to in total_user_tasks:
                    total_user_tasks[assigned_to] += 1
                    if status.lower() == "yes":
                        total_user_completed_tasks[assigned_to] += 1

        # generate "user_overview.txt" with user statistics
        with open("user_overview.txt", "w") as user_file:
            user_file.write("User Overview\n")
            user_file.write("-" * 20 + "\n")
            user_file.write(f"Total users registered: {total_users}\n")

            for username in usernames:
                assigned_tasks = total_user_tasks[username]
                completed_tasks = total_user_completed_tasks[username]
                incomplete_tasks = assigned_tasks - completed_tasks
                overdue_tasks = 0

                # check if the user has no tasks assigned
                if assigned_tasks == 0:
                    percentage_completed = 0
                    percentage_incomplete = 0
                    percentage_overdue = 0
                else:
                    for task in tasks:
                        task_data = task.split(', ')
                        assigned_to = task_data[0].strip()
                        status = task_data[5].strip()
                        due_date_str = task_data[3].strip()
                        due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
                        current_date = datetime.date.today()

                        if assigned_to == username and status.lower() == "no":
                            if due_date < current_date:
                                overdue_tasks += 1

                    # calculate percentages for complete, incomplete, and overdue tasks
                    percentage_completed = (completed_tasks / assigned_tasks) * 100
                    percentage_incomplete = (incomplete_tasks / assigned_tasks) * 100
                    percentage_overdue = (overdue_tasks / assigned_tasks) * 100

                # write to the file with calculations
                user_file.write(f"Username: {username}\n")
                user_file.write(f"Total tasks assigned: {assigned_tasks}\n")
                user_file.write(f"Percentage completed: {percentage_completed:.2f}%\n")
                user_file.write(f"Percentage incomplete: {percentage_incomplete:.2f}%\n")
                user_file.write(f"Percentage overdue: {percentage_overdue:.2f}%\n")
                user_file.write("-" * 20 + "\n")
        # let user know reports are generated
        print("Reports generated successfully.")

    except FileNotFoundError:
        print("One or more required files ('tasks.txt') does not exist.") 

# if reports have not been generated to task & user overview files


# if reports haven't been created
def generate_reports_if_needed():
    if not os.path.isfile("task_overview.txt") or not os.path.isfile("user_overview.txt"):
        generate_reports()


def display_stats():
    # check if reports need to be generated
    generate_reports_if_needed()

    try:
        # display task statistics from "task_overview.txt"
        with open("task_overview.txt", "r") as task_file:
            task_data = task_file.read()
            print("Task Statistics:")
            print(task_data)

        # display user statistics from "user_overview.txt"
        with open("user_overview.txt", "r") as user_file:
            user_data = user_file.read()
            print("User Statistics:")
            print(user_data)
    # except error
    except FileNotFoundError:
        print("One or more required files do not exist or are not accessible.")

# print goodbye if user chooses to exit


def exit():
    print('Goodbye and thank you for visiting!!!')

# ====login section=====


def login(username, password):
    # open and read user.txt file
    with open('user.txt', 'r') as file:
        for line in file:
            current_username, current_password = line.strip().split(", ")
            
            # stored usernames and passwords to match for succesful login
            if username == current_username and password == current_password:
                return True
    return False

# ====main code ====


while True:
    # ask user for login username and password
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    if login(username, password):
        print("You are successfully logged in, welcome to the progam!")
        break
    else:
        print("username or password not recognised, please try again! Or ask the admin to add you to the system!")


if __name__ == "__main__":
    login(username, password)

while True:
    # present menu for user to choose from
    menu = input("""Please Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: """).lower()
    # use if/elif to return function for letter entered
    if menu == 'r':
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine(username)
    elif menu == 'gr':
        generate_reports()
    elif menu == 'ds':
        display_stats()
    elif menu == 'e':
        exit()
        break  # exit loop when 'e' is entered
    else:
        print("Please try another option!")
