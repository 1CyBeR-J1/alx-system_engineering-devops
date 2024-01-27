#!/usr/bin/python3
"""extend your Python script to export data in the JSON format."""

import json
import requests
import sys

if __name__ == '__main__':
    empId = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + empId

    response = requests.get(url)
    username = response.json().get('username')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    dictionary = {empId: []}
    for task in tasks:
        dictionary[empId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(empId), 'w') as f:
        json.dump(dictionary, f)
