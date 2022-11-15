import json

data = open('data.json').read()

x = json.loads(data)

print(x)