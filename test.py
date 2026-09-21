#!usr/bin/env python3

import os
import sys
import json

TASK_FILE = "task.json"

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
    if any(task["title"] == title for task in tasks):
        print(f"Task with title '{title}' already exists.")
        return
        task_id = 1 if not tasks else tasks[-1]["id"] + 1

        new_task = {
            "id": task_id,
            "title": title,
            "description" : description,
            "done": False
        }


    tasks.append(new_task)
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f)

# def update_task(description, ):

# def delete_task():

# def markasdone():

# def listdone():

# def listnotdone():

# def listpending():


command = sys.argv[1]

if command == "add":


if command == "update":

if command == "finish":

if command == "listf":

if command == "listuf":

if command == "listnd":

if command == "listp":
    



