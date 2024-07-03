import csv
from tabulate import tabulate
import re

"""
Name: Yunus Hossain
EdX Username: justuraveragelolguy
GitHub Username: lolguy118
Location: Bay Shore, NY, United States of America
Date: July 2, 2024
"""


def main():
    table_of_commands = [
        {"Command": "add", "Description": "Adds a task to the list"},
        {"Command": "view", "Description": "Shows all current tasks on the list"},
        {
            "Command": "remove",
            "Description": "Takes a task off the list; can be used if task is complete",
        },
        {"Command": "edit", "Description": "Edits the task, date, or time of an item"},
        {"Command": "exit", "Description": "Exits the program"},
    ]
    while True:
        print(tabulate(table_of_commands, headers="keys", tablefmt="simple_grid"))
        action = input("Desired Action: ")
        match action:
            case "add":
                add_item()
            case "view":
                view_all_items()
            case "remove":
                remove_an_item()
            case "edit":
                edit_an_item()
            case "exit":
                exit()
            case _:
                continue


def add_item():
    while True:
        task = input("Task Needing Completion: ")
        if not task:
            continue
        break
    while True:
        deadline_date = input("Date The Task Should Be Done By (mm/dd/yy): ")
        if not verify_date(deadline_date):
            continue
        break
    while True:
        deadline_time = input(
            "Time The Task Should Be Done By (24 hour and 12 hour supported; put a 0 before the hour if only one digit ex. 07:30): "
        )
        if not verify_time(deadline_time):
            continue
        break
    with open("tasks.csv", "a") as tasks:
        task_to_be_written = {
            "task": task,
            "deadline_date": deadline_date,
            "deadline_time": deadline_time,
        }
        writer = csv.DictWriter(
            tasks, fieldnames=["task", "deadline_date", "deadline_time"], delimiter="|"
        )
        writer.writerow(task_to_be_written)


def view_all_items():
    with open("tasks.csv") as tasks:
        reader = csv.DictReader(tasks, delimiter="|")
        print(tabulate(reader, headers="keys", tablefmt="simple_grid"))


def remove_an_item():
    with open("tasks.csv") as tasks:
        reader = list(csv.DictReader(tasks, delimiter="|"))
        id_number = 1
        for row in reader:
            row["id"] = id_number
            id_number += 1
        print(tabulate(reader, headers="keys", tablefmt="simple_grid"))
    while True:
        try:
            id_of_task_to_be_deleted = int(input("ID of Task to Delete: "))
        except ValueError:
            continue
        else:
            id_exists = False
            for row in reader:
                if row["id"] == id_of_task_to_be_deleted:
                    id_exists = True
                    break
            if not id_exists:
                continue
            else:
                break
    for row in reader:
        if row["id"] == id_of_task_to_be_deleted:
            reader.remove(row)
            break
    with open("tasks.csv", "w") as tasks:
        writer = csv.DictWriter(
            tasks,
            fieldnames=["task", "deadline_date", "deadline_time"],
            delimiter="|",
            extrasaction="ignore",
        )
        writer.writeheader()
        for row in reader:
            writer.writerow(row)


def edit_an_item():
    with open("tasks.csv") as tasks:
        reader = list(csv.DictReader(tasks, delimiter="|"))
        id_number = 1
        for row in reader:
            row["id"] = id_number
            id_number += 1
        print(tabulate(reader, headers="keys", tablefmt="simple_grid"))
    while True:
        try:
            id_of_task_to_be_edited = int(input("ID of Task to Edit: "))
        except ValueError:
            continue
        else:
            id_exists = False
            for row in reader:
                if row["id"] == id_of_task_to_be_edited:
                    id_exists = True
                    break
            if not id_exists:
                continue
            else:
                break
    while True:
        field_to_be_edited = input("Field to be Edited (task, date, or time): ")
        match field_to_be_edited:
            case "task":
                new_task = input("New Task: ")
                for row in reader:
                    if row["id"] == id_of_task_to_be_edited:
                        row["task"] = new_task
                        break
                break
            case "date":
                while True:
                    new_date = input("New Date: ")
                    if not verify_date(new_date):
                        continue
                    break
                for row in reader:
                    if row["id"] == id_of_task_to_be_edited:
                        row["deadline_date"] = new_date
                        break
                break
            case "time":
                while True:
                    new_time = input("New Time: ")
                    if not verify_time(new_time):
                        continue
                    break
                for row in reader:
                    if row["id"] == id_of_task_to_be_edited:
                        row["deadline_time"] = new_time
                        break
                break
            case _:
                continue
    with open("tasks.csv", "w") as tasks:
        writer = csv.DictWriter(
            tasks,
            fieldnames=["task", "deadline_date", "deadline_time"],
            delimiter="|",
            extrasaction="ignore",
        )
        writer.writeheader()
        for row in reader:
            writer.writerow(row)


def verify_date(date):
    match = re.match("^([0-9][0-9])/([0-9][0-9])/([0-9][0-9][0-9][0-9])$", date)
    if not match:
        return False
    if not (1 <= int(match.group(1)) <= 12) or not (1 <= int(match.group(1)) <= 31):
        return False
    return True


def verify_time(time):
    match = re.match("^([0-9][0-9]):([0-9][0-9]) ?(AM|PM)?$", time)
    if not match:
        return False
    if match.group(3) in ("AM", "PM"):
        if not (1 <= int(match.group(1)) <= 12) or not (0 <= int(match.group(2)) <= 59):
            return False
    else:
        if not (1 <= int(match.group(1)) <= 23) or not (0 <= int(match.group(2)) <= 59):
            return False
    return True


if __name__ == "__main__":
    main()
