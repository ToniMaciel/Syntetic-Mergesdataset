import os
import json

new_data = list()

with open('data_base.json', 'r') as file:
    data = file.read()
    data_json = json.loads(data)

cwd = os.getcwd()

for item in data_json:
    for key in item['scenarioJars']:
        item['scenarioJars'][key] = os.path.join(cwd, item['scenarioJars'][key])
    new_data.append(item)

with open('data.json', 'w') as file:
    json.dump(new_data, file, indent=4)
