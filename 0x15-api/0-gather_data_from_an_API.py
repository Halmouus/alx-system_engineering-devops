#!/usr/bin/python3
""" script that, using this REST API,
for a given employee ID, returns information
about his/her todo list progress"""
import requests
import json
import sys

idVar = sys.argv[1]
user_data = requests.get(f'https://jsonplaceholder.typicode.com/users/{idVar}')

if user_data.status_code == 200:
    user_info = user_data.json()
    name = user_info['name']

todos_data = requests.get('https://jsonplaceholder.typicode.com/todos')

if todos_data.status_code == 200:
    title_list = []
    completed = 0
    non_completed = 0

    todos = todos_data.json()
    for todo in todos:
        if todo["userId"] == int(idVar):
            title_list.append(todo["title"])
            if todo["completed"]:
                completed += 1
            else:
                non_completed += 1

    print(f"Employee {name} is done with tasks\
          ({completed}/{non_completed + completed}):")
    for i in range(completed):
        print(f"\t {title_list[i]}")
