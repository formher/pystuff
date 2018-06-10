import json


## Adds new ASIN into config file "config.json"
def addasin(asin):
    with open ('config.json', 'r') as f:
        myjson = json.load(f)
        for key, value in myjson['LISTOFASINS'].items():
            # iterstart = key
            finalnumber = int(key[len(key)-1:])
            finalnumber += 1
        myjson['LISTOFASINS'].update({"ASIN" + str(finalnumber): asin})
    with open('config.json', 'w') as a:
        json.dump(myjson, a)


## Replaces colon from rank numbers
def replacelistitem(mylist, tofind, toreplace):
    for index, item in enumerate(mylist):
        mylist[index] = mylist[index].replace(tofind, toreplace)
    return mylist

## saving dict or anythin as json
def jsonsave(jsonitem, filename):
    with open (filename, 'w') as outfile:
        json.dump(jsonitem, outfile)

