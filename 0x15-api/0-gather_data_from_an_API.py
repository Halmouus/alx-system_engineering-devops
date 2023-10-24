#!/usr/bin/python3
""" script that, using this REST API,
for a given employee ID, returns information
about his/her todo list progress"""
import json
import requests
import sys

if __name__ == "__main__":
    idVar = sys.argv[1]
    resp = requests.get(f'https://jsonplaceholder.typicode.com/users/{idVar}')

    if resp.status_code == 200:
        user_info = resp.json()
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

        print(f"Employee {name} is done with tasks"
              f"({completed}/{non_completed + completed}):")
        for i in range(completed):
            print(f"\t {title_list[i]}")
