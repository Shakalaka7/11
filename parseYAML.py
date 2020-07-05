import yaml
from yaml import load, load_all

stream = open('Yaml1.yaml','r')
documents = load_all(stream, Loader=yaml.FullLoader)

print(type(documents))

for doc in documents:
    print(doc)

    print(doc['people'][1]['LastName'])
