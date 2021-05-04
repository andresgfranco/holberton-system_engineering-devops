#!usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TO-DO list progress."""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    tasks = requests.get(url + "todos/?userId={}".format(user_id)).json()

    completed_task = [(i) for i in tasks if i.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(user["name"],
          len(completed_task), len(tasks)))
    for task in completed_task:
        print("\t", task["title"])
