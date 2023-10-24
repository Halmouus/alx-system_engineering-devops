#!/usr/bin/python3
import requests
import json
import pandas as pd
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

    print(f"Employee {name} is done with tasks ({completed}/{non_completed + completed}):")
    for i in range(completed):
        print(f"\t {title_list[i]}")
"""    
    with open('data.json', 'w') as json_file:
        json.dump(response_data, json_file, indent=4)
    #df = pd.DataFrame.from_dict(response_data)
    #df.to_csv('data.csv', index=False)
else:
    print (resp.status_code)
"""