import requests
from bs4 import BeautifulSoup
# import html5lib
import re
import time
import datetime
import csv

## Defining current time to calculate overall script running duration and include the current timestamp in json
start_time = time.time()
currenttime = datetime.datetime.now()


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
origurl = 'https://www.amazon.com/dp/'
listofasin = ['B0795YVPTT', 'B079MCFWMH', 'B074KJ519P']
listofurls = [origurl + i for i in listofasin]

# with open ('amazon.txt', 'w') as amazon:
#     amazon.write(response.text)

category = []
dict1 = {}
counter = 0
result = [('Rank', 'Category')]
# result = []


for url in listofurls:
    counter += 1
    response = requests.get(url, headers=headers) #, verify=True)
    soup = BeautifulSoup(response.content, "html.parser")

    for link in soup.find_all('span'):
        searchObj = re.match(r'(\#)(\d+[,]?\d+)(.*)', link.text, re.M|re.I)
        if searchObj:
            result.append(searchObj.group(2, 3))

## Printing the list
for i in result:
    print(i)

## Printing the dicitionary
# for key, value in dict1.items():
#     print(key, value)

with open('report.csv', 'a') as f:  # Just use 'w' mode in 3.x
    wr = csv.writer(f) #, quoting=csv.QUOTE_ALL)
    wr.writerows(result)

print("\n--- %f seconds ---" % (time.time() - start_time))


