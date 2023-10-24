#!/usr/bin/python3
import requests
import json
import pandas as pd
import sys

idVar = sys.argv[1]
resp_name = requests.get(f'https://jsonplaceholder.typicode.com/users/{idVar}')
resp = requests.get(f'https://jsonplaceholder.typicode.com/todos/{idVar}')
if resp_name.status_code == 200:
    respdata = resp_name.json()
    name = respdata['name']
    print(name)
if resp.status_code == 200:
    response_data = resp.json()
    print(f"User id: {response_data['userId']}")
    print(f"id: {response_data['id']}")
    print(f"name: {name}")
    print(f"title: {response_data['title']}")
    print(f"title: {response_data['title']}")
    print(f"title: {response_data['title']}")
    print(f"completed: {response_data['completed']}\n")
    
    with open('data.json', 'w') as json_file:
        json.dump(response_data, json_file, indent=4)
    #df = pd.DataFrame.from_dict(response_data)
    #df.to_csv('data.csv', index=False)
else:
    print (resp.status_code)
