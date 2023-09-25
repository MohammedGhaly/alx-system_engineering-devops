#!/usr/bin/python3
"""a script to export data in the JSON format"""
if __name__ == '__main__':
    import json
    import requests
    import sys

    employee_id = int(sys.argv[1])
    tasks_url = \
        f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    names_url = 'https://jsonplaceholder.typicode.com/users'

    res = requests.get(names_url)
    content = res.content.decode()
    names_list = json.loads(content)
    username = names_list[employee_id - 1]['username']

    res = requests.get(tasks_url)
    content = res.content.decode()
    employee_tasks_list = json.loads(content)

    report_list = []
    for task in employee_tasks_list:
        report_list.append({"task": task.get('title'), "completed": task.get(
            'completed'), "username": username})

    with open(f'{employee_id}.json', 'w', encoding='utf-8') as f:
        json.dump({f'{employee_id}': report_list}, f)
