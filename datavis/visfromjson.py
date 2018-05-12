import requests, json
import matplotlib.pyplot as plt
from datetime import datetime

def getData(stockname):
    ## URL below is for stock market
    # url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=' + stockname + '&outputsize=full&apikey=YSG3QYKIOSVJ42W8'
    url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=' + stockname + '&market=CNY&apikey=YSG3QYKIOSVJ42W8'
    response = requests.get(url)
    myjson = response.json()
    print('parsing {}'.format(myjson['Meta Data']['2. Digital Currency Code']))
    ## Returns json
    return myjson

def parseTimestamp(json):
    timestamp = []
    for key, value in json['Time Series (Digital Currency Daily)'].items():
        tmstoint = datetime.strptime(key, '%Y-%m-%d')
        timestamp.append(tmstoint)
    ## Returns list
    return timestamp
#
def parseCloseValue(json):
    metricvalues = []
    for key, value in json['Time Series (Digital Currency Daily)'].items():
        metricvalues.append(float(json['Time Series (Digital Currency Daily)'][key][metric]))
    ## Returns list
    return metricvalues


def genGraph(x, y):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    ax1.plot(x, y, label='Actual data', color='r')
    ax1.fill_between(x, y, 0.8, facecolors='c', alpha=0.4)

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True)

    # ax1.set_yticks([0, 0.5, 1, 1.5, 2, 3])
    # plt.bar(x, y, label='dummy data 1', color='red')
    # plt.bar(x2, y2, label='dummy data 2')
    plt.xlabel('Date')
    plt.ylabel('Close value in US Dollars')
    plt.title('{} Daily Stock'.format(stockname))
    plt.subplots_adjust(bottom=0.18, left=0.15)

    plt.show()
    # plt.savefig(stockname + '.png')

## Configs
stockname = 'XRP'
metric = '4b. close (USD)'
mydata = getData(stockname)

## Defining the lists of timestamp and values
x = parseTimestamp(mydata)
y = parseCloseValue(mydata)

def lastMonth(mylist):
    counter = 0
    newlist = []
    while counter < 30:
        newlist.append(mylist[counter])
        counter += 1
    return newlist

x = lastMonth(x)
y = lastMonth(y)

print(x, y)
# genGraph(x, y)
