#!/usr/bin/python3
"""
script that for a given employee ID,
returns information about his progress
"""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    employee_tasks_url = \
        f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    names_url = 'https://jsonplaceholder.typicode.com/users'

    res = requests.get(names_url)
    content = res.content.decode()
    names_list = json.loads(content)
    name = names_list[employee_id - 1].get('name')

    res = requests.get(employee_tasks_url)
    content = res.content.decode()
    employee_tasks = json.loads(content)
    done_tasks = list(map(lambda x: x.get('title'),
                      filter(lambda x: x.get('completed'), employee_tasks)))

    print(f"Employee {name} is done with tasks({len(done_tasks)}/20):")
    for item in done_tasks:
        print(f"\t {item}")
