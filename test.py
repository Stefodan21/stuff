#!usr/bin/env python3

import os
import sys
import json

TASK_FILE = "task.json"

def load_tasks():
    if not os.path.exist(TASK_FILE):
        with open(TASK_FILE, "w") as f:
            json.dump([], f)
        print("File doesn't exist, so created one instead.")

    with open(TASK_FILE, "r") as f:
        try:
            tasks = json.load(f)
            print(tasks)
        except json.JSONDecodeError as e:
            print(f"error loading {file}: {e}")


def add_task(description):
    if not os.path.exist(TASK_FILE):
        print("Please run load tasks first!")
    
    tasks = load_tasks()

    new_id = 1 if not tasks else tasks[-1]["id"] + 1

    new_task = {
        "id": new_id,
        "description" : description,
        
    }



# def update_task():

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
    



