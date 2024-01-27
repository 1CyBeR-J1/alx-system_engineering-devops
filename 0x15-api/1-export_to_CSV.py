#!/usr/bin/python3
"""extend your Python script to export data in the CSV format"""

import requests
import sys

if __name__ == '__main__':
    empId = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + empId

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(empId, username, task.get('completed'),
                               task.get('title')))
