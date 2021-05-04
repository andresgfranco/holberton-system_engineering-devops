#!/usr/bin/python3
"""script to export data in the CSV format"""


if __name__ == "__main__":
    import requests
    from sys import argv
    import json
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    tasks = requests.get(url + "todos/?userId={}".format(user_id)).json()

    jsonDict = {}
    jsonDict[user_id] = []

    for task in tasks:
        jsonDict[user_id].append({"task": task["title"],
                                  "completed": task["completed"],
                                  "username": user["username"]})

    with open("{}.json".format(user_id), "w") as jsonfile:
        jsonfile.write((json.dumps(jsonDict)))
