#!/usr/bin/python3.6
import json, requests, re, time, datetime, logging, os, sys, csv
import my_func as mf
from bs4 import BeautifulSoup


currPath = os.getcwd()
os.chdir(currPath)
## Logging part
logging.basicConfig(filename=currPath + '/example.log',level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')

## Uncomment to add new asin
# mf.addasin('new_asin')

## Defining current time to calculate overall script running duration
start_time = time.time()

## Reading the config file
with open('/home/ec2-user/scraper/config.json', 'r') as f:
    configs = json.load(f)

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
listofurls = []
for key, asin in configs['LISTOFASINS'].items():
    listofurls.append(configs['MAIN']['BASEURL'] + asin)

data = {}

## Requesting and parsing the list of URLs
for url in listofurls:
    currenttime = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    try:
        response = requests.get(url, headers=headers) #, verify=True) ## For SSL verification, not sure how to use yet.
        soup = BeautifulSoup(response.content, "html.parser")
    except Exception as err:
        print(err)
        logging.warning(err)
        pass

    ## Extracting ASIN
    asinlist = url.split('/')
    finalasin = asinlist[len(asinlist)-1]

    ## Setting the product title as a parent
    title = str(soup.title.string)
    finaltitle = title[12:60]
    data[finaltitle] = {}

    ## Extracting the price
    try:
        price = soup.find('span', {'id': 'priceblock_ourprice'})
        searchObj = re.search(r'^\$(\d+[\.\d+]?\d+)', price.text, re.M | re.I)
        if searchObj:
            finalprice = searchObj.group(1)
            data[finaltitle].update({"Price":finalprice})
    except Exception as err:
        finalprice = 'No price'
        pass

    ## Extract the review count
    try:
        reviewcount = soup.find('span', {'id': 'acrCustomerReviewText'})
        searchObj1 = re.search(r'(\d+[\.\d+]?)(.*)', reviewcount.text, re.M | re.I)
        if searchObj1:
            finalreviewcount = searchObj1.group(1)
            data[finaltitle].update({"Review count":finalreviewcount})
    except Exception as err:
        print(err)
        logging.warning(err)
        pass

    ## Extract the rating avarage count
    try:
        ratingavarage = soup.find('span', {'id': 'acrPopover'})
        searchObj2 = re.search(r'(\d+[\.]?\d+)(.*)', ratingavarage.text, re.M | re.I)
        if searchObj2:
            finalratingavarage = searchObj2.group(1)
            data[finaltitle].update({"Rating avarage":searchObj2.group(1)})
    except Exception as err:
        finalratingavarage = 'No rating'
        pass

    ## Added lists to take only top category for each item
    ranktemp = []
    categorytemp = []

    ## Extracting main BSR and main category name
    try:
        for rank in soup.find_all('span'):
            searchObj3 = re.match(r'^\#(\d+[,]?\d+)([^(]*)', rank.text, re.M|re.I)
            if searchObj3:
                ranktemp.append(searchObj3.group(1))
                categorytemp.append(searchObj3.group(2).strip())
    except Exception as err:
        print(err)
        logging.warning(err)
        pass

    ## Removing colon from rank number from my custom function
    mf.replacelistitem(ranktemp, ',', '')

    ## Removing 'in ' from top category name from my custom function
    mf.replacelistitem(categorytemp, 'in ', '')

    ## Handling the csv
    finalcsvresult = currPath + '/results/' + finalasin + '.csv'
    ## For windows:
    #finalcsvresult = currPath + '\\results\\' + finalasin + '.csv'

    if os.path.exists('/home/ec2-user/scraper/results/' + finalasin + '.csv'):
        csv_open = open('/home/ec2-user/scraper/results/' + finalasin + '.csv', 'a') ## Add newline='' for windows
        csv_writer = csv.writer(csv_open)
    else:
        csv_open = open('/home/ec2-user/scraper/results/' + finalasin + '.csv', 'a') ## Add newline='' for windows
        csv_writer = csv.writer(csv_open)
        try:
            csv_writer.writerow(['Price', 'BSR', 'Rating avarage', 'Reviw count', 'Main category: ' + categorytemp[0], 'Link: ' + url, 'ASIN: ' + finalasin, 'Timestamp'])
        except Exception:
            csv_writer.writerow(['Price', 'BSR', 'Rating avarage', 'Reviw count', 'Main category: ' + 'no Category', 'Link: ' + url, 'ASIN: ' + finalasin, 'Timestamp'])
    try:
        csv_writer.writerow([finalprice, ranktemp[0], finalratingavarage, finalreviewcount, '', '', '', currenttime])
    except Exception:
        csv_writer.writerow([finalprice, 'No Rank', finalratingavarage, finalreviewcount, '', '', '', currenttime])

csv_open.close()


print("\n---Script took %f seconds ---" %(time.time() - start_time))

