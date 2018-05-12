import json

filename = 'sample.json'
with open ('sample.json', 'r+') as myjsonobject:
    jsoncountries=json.load(myjsonobject)


print(jsoncountries)