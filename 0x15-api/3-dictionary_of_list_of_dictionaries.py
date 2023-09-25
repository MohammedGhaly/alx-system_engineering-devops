#!/usr/bin/python3
"""a script to export data in the JSON format"""
if __name__ == '__main__':
    import json
    import requests

    names_url = 'https://jsonplaceholder.typicode.com/users'
    all_emps_all_tasks = {}
    for em_id in range(1, 11):
        res = requests.get(names_url)
        content = res.content.decode()
        names_list = json.loads(content)
        username = names_list[em_id - 1]['username']

        task_url = f'https://jsonplaceholder.typicode.com/users/{em_id}/todos'
        res = requests.get(task_url)
        content = res.content.decode()
        employee_tasks_list = json.loads(content)

        report_list = []
        for task in employee_tasks_list:
            report_list.append({"username": username, "task": task.get(
                'title'), "completed": task.get('completed')})

        all_emps_all_tasks[f'{em_id}'] = report_list

    with open('todo_all_employees.json', 'w', encoding='utf-8') as f:
        json.dump(all_emps_all_tasks, f)
