#!usr/bin/env python3

import os
import sys
import json

TASK_FILE = "task.json"

allowedstatus= {"Ongoing","Done","Todo"}

# create file if it does not exist
if not os.path.exists(TASK_FILE):
    with open(TASK_FILE, "w") as f:
        json.dump([], f)

with open(TASK_FILE, "r") as f:
    try:
        tasks = json.load(f)
    except json.JSONDecodeError as e:
        print(f"error loading {TASK_FILE}: {e}")
        tasks = []


def add_task(title=None, description=None):

    if title is None:
        print("Title is required.")
        return
    elif description is None:
        print("Description is required.")
        return


    task_id = 1 if not tasks else tasks[-1]["id"] + 1
    new_task = {
        "id": task_id,
        "title": title,
        "description" : description,
        "status": "Todo"
    }


    tasks.append(new_task)
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f)

def update_task(task_id, status):
    try:
        if not isinstance(task_id, int):
            raise ValueError("Task_id must be an integer")


        if not any(task["id"] == task_id for task in tasks):
            raise ValueError("Task ID is required.If you dont know, run the list task command.")


        if status not in allowedstatus:
            raise ValueError('Please enter if it is "Ongoing", "Done", or "Todo"')

        for task in tasks:
            if task["id"] == task_id:
                task["id"] = status
                print(f"the task:{task["id"]}, description{task["description"]} task has been updated to {task["status"]}!")

            with open(TASK_FILE,"w") as f:
                json.dump(tasks, f)

    except ValueError as e:
        print("Error:", e)
        return


 def list_tasks():
    try:
        print(tasks)
    except:

# def delete_task():

# def markasdone():

# def listdone():

# def listnotdone():

# def listpending():


command = sys.argv[1]
description = sys.argv[2]

if command == "add":


if command == "update":

if command == "finish":

if command == "listf":

if command == "listuf":

if command == "listnd":

if command == "listp":
    



