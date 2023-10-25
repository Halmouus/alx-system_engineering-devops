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
        todos = todos_data.json()
        dict_list = [
            {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": username
            }
            for todo in todos
            if todo["userId"] == int(idVar)
        ]
        global_dict = {idVar: dict_list}
        json_todo = json.dumps(global_dict)
        jsonfile = f"{idVar}.json"
        with open(jsonfile, 'w') as json_file:
            json_file.write(json_todo)
