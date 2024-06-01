#!workspace/bin/python

import requests
import json


OBJECT = requests.get("https://api.github.com/users/ilonaserg")

# if site is working
if OBJECT.status_code == 200:
    # convert data to json
    content = json.loads(OBJECT.text)
    # print to screen
    print(content["login"])