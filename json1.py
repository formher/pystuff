import json

countries = ['USA','Armenia','Georgia']
filename='countries.json'

with open (filename,'w') as myjsonobject:
    json.dump(countries,myjsonobject)


with open (filename) as myjsonobject1:
    jsoncountries=json.load(myjsonobject1)
    print(jsoncountries)

