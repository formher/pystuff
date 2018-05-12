import json, requests, re, time, datetime, logging, os, sys, csv
import my_func as mf
from bs4 import BeautifulSoup


## Logging part
currPath = os.getcwd() # os.path.dirname(os.path.realpath(sys.argv[0]))
logging.basicConfig(filename=currPath + '/example.log',level=logging.INFO,format='%(asctime)s %(levelname)s %(name)s %(message)s')

## Uncomment to add new asin
# mf.addasin('new_asin')

## Defining current time to calculate overall script running duration
start_time = time.time()

## Reading the config file
with open('config.json', 'r') as f:
    configs = json.load(f)

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
listofurls = []
for key, asin in configs['LISTOFASINS'].items():
    listofurls.append(configs['MAIN']['BASEURL'] + asin)

data = {}

## Requesting and parsin the list of URLs
for url in listofurls:
    currenttime = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    try:
        response = requests.get(url, headers=headers) #, verify=True) ## For SSL verification, not sure how to use yet.
        soup = BeautifulSoup(response.content, "html.parser")
    except Exception as err:
        print(err)
        logging.warning(err)
        pass


    ## Asin variable set
    asinlist = url.split('/')
    finalasin = asinlist[len(asinlist)-1]


    ## Setting the product title as a parent
    title = str(soup.title.string)
    finaltitle = title[12:60]
    data[finaltitle] = {}

    ## Finding out if the item is unavailable
    try:
        availability = soup.find('div', {'id': 'availability'})
        if availability.span.text.strip() == 'Price is currently unavailable.':
            finaprice = availability.span.text.strip()
            data[finaltitle].update({"Price":finalprice})
    except Exception:
        finaprice = 'No price'
        pass

    ## Extracting the price
    try:
        price = soup.find('span', {'id': 'priceblock_ourprice'})
        searchObj = re.search(r'^\$(\d+[\.\d+]?\d+)', price.text, re.M | re.I)
        if searchObj:
            finalprice = searchObj.group(1)
            data[finaltitle].update({"Price":finalprice})
        else: available = False
    except Exception as err:
        print('The product which doesn\'t have price: ' + url)
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

    ## Currently this takes only top level rank. Include all the ranks in the future. E.g. .update({"Rank":ranktemp[len(ranktemp)-1]})
    try:
        data[title[12:60]].update({"Rank Top":ranktemp[0]})
        data[title[12:60]].update({"Category Top":categorytemp[0]})
    except Exception:
        data[title[12:60]].update({"Rank Top": 'No rank'})
        data[title[12:60]].update({"Category Top": 'No category'})
        pass
    data[title[12:60]].update({"Link":url})
    data[title[12:60]].update({"ASIN":finalasin})
    data[title[12:60]].update({"Timestamp":currenttime})

    ## Handling the csv
    finalcsvresult = currPath + '/results/' + finalasin + '.csv'
    ## For windows:
    #finalcsvresult = currPath + '\\results\\' + finalasin + '.csv'
    if os.path.exists(finalcsvresult):
        csv_open = open(finalcsvresult, 'a') ## Add newline='' for windows
        csv_writer = csv.writer(csv_open)
    else:
        csv_open = open(finalcsvresult, 'a') ## Add newline='' for windows
        csv_writer = csv.writer(csv_open)
        csv_writer.writerow(['Price', 'BSR', 'Rating avarage', 'Reviw count', 'Main category name', 'Link: ' + url, 'ASIN: ' + finalasin, 'Timestamp'])
    csv_writer.writerow([finalprice, ranktemp[0], finalratingavarage, finalreviewcount, categorytemp[0], '', '', currenttime])

## Adding top parent into dict
data = {'Products': data}

csv_open.close()

## Writing to json from my custom function

mf.jsonsave(data, 'data.json') # Item to save, filename to save


print("\n---Script took %f seconds ---" %(time.time() - start_time))

