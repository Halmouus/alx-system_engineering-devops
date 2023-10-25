#!/usr/bin/python3
""" script that, using this REST API,
records all tasks from all employees
and export data in the JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    todos_data = requests.get(f"{url}todos")

    if todos_data.status_code == 200:
        todos = todos_data.json()
        todo_dict = {}
        for i in range(1, 10):
            resp = requests.get(f'{url}/users/{i}')
            if resp.status_code == 200:
                user_info = resp.json()
                username = user_info['username']
                dict_list = [
                    {
                        "username": username,
                        "task": todo['title'],
                        "completed": todo['completed'],
                    }
                    for todo in todos
                    if todo["userId"] == i
                ]
                todo_dict[i] = dict_list
        json_todo = json.dumps(todo_dict)
        jsonfile = "todo_all_employees.json"
        with open(jsonfile, 'w') as json_file:
            json_file.write(json_todo)
