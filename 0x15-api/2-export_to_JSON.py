#!/usr/bin/python3
""" script that, using this REST API,
for a given employee ID, returns information
about his/her todo list andexport data in the CSV format."""
import csv
import json
import requests
import sys

if __name__ == "__main__":
    idVar = sys.argv[1]
    resp = requests.get(f'https://jsonplaceholder.typicode.com/users/{idVar}')

    if resp.status_code == 200:
        user_info = resp.json()
        username = user_info['username']

    todos_data = requests.get('https://jsonplaceholder.typicode.com/todos')

    if todos_data.status_code == 200:
        dict_list = []
        todos = todos_data.json()
        for todo in todos:
            if todo["userId"] == int(idVar):
                todo_dict = {}
                todo_dict["USER_ID"] = f"{idVar}"
                todo_dict["USERNAME"] = f"{username}"
                todo_dict["TASK_COMPLETED_STATUS"] = f"{todo['completed']}"
                todo_dict["TASK_TITLE"] = f"{todo['title']}"
                dict_list.append(todo_dict)
                
    json_todo = dict_list.json()
    jsonfile = f"{idVar}.json"
    with open(jsonfile, 'w') as json_file:
        json.dump(json_todo, json_file, indent=4)
