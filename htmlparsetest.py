import requests
from bs4 import BeautifulSoup
# import html5lib
import re
import time

start_time = time.time()


origurl = 'https://www.amazon.com/dp/B079MCFWMH'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

result = []

r = requests.get(origurl, headers=headers)
soup = BeautifulSoup(r.content, "html.parser")
# info = str(info)

price = soup.find('span', {'id': 'priceblock_ourprice'})
print(price.text)


# soup2 = BeautifulSoup(info.content, "html.parser")

# info = soup.findAll('table', {'class': 'a-keyvalue prodDetTable'})
#
# print(type(info.text))
#
# searchObj = re.search(r'(\#)(\d+[,]?\d+)(.*)', info.text, re.M|re.I)
# if searchObj:
#     print(searchObj)
#     result.append(searchObj.group(2, 3))
#
#
# print(result)
#
#
# print("\n--- %f seconds ---" % (time.time() - start_time))
