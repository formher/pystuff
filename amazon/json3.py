import json

data = {}
data['Product 1'] = {}
data['Product 2'] = {}
data['Product 3'] = {}


data['Product 1'] = {
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
}
data['Product 2'] = {
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
}
data['Product 3'] = {
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
}
print(type(data))


with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

filename = 'sample.json'
with open ('sample.json', 'r+') as myjsonobject:
    jsoncountries=json.load(myjsonobject)



with open('data.json', 'r+') as file:
    myfile = json.load(file)

myfile['Products'] = {}

myfile['Products'].update({"new key": 'new value'})

with open('data.json', 'w') as outfile:
    json.dump(myfile, outfile)

print(myfile)

