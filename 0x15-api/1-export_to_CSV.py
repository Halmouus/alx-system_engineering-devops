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
                todo_dict["USER_ID"] = idVar
                todo_dict["USERNAME"] = username
                todo_dict["TASK_COMPLETED_STATUS"] = todo["completed"]
                todo_dict["TASK_TITLE"] = todo["title"]
                dict_list.append(todo_dict)

    csv_file = f"{idVar}.csv"
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=dict_list[0].keys())
        for todo_dict in dict_list:
            writer.writerow(todo_dict)
