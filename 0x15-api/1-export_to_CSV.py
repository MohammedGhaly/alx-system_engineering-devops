#!/usr/bin/python3
import csv
import json
import requests
import sys

employee_id = int(sys.argv[1])
tasks_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
names_url = 'https://jsonplaceholder.typicode.com/users'

res = requests.get(names_url)
content = res.content.decode()
names_list = json.loads(content)
username = names_list[employee_id - 1]['username']


res = requests.get(tasks_url)
content = res.content.decode()
employee_tasks = json.loads(content)

done_tasks = list(map(lambda x: x['title'],
                      filter(lambda x: x['completed'], employee_tasks)))

tasks_report = []
for task in employee_tasks:
    tasks_report.append({'name': username, 'id': employee_id, 'com': task.get(
        'completed'), 'title': task.get('title')})

with open(f"{employee_id}.csv", "w") as f:
    writer = csv.DictWriter(
        f, fieldnames=['id', 'name', 'com', 'title'], quoting=csv.QUOTE_ALL)
    writer.writerows(tasks_report)
