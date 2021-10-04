import json

import requests

# задание 1
with open('task_1.json', 'w') as f:
    username = 'VladimirZaharov'
    response = requests.get(f'https://api.github.com/users/{username}/repos')
    json.dump(response.json(), f)

# задание 2
with open('task_2.json', 'w') as p:
    appid = '14cac5349dd630993d512879942c76fd'
    city_name = 'Moscow'
    response_1 = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={appid}')
    json.dump(response_1.json(),p)

