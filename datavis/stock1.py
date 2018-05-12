import matplotlib.pyplot as plt
import csv
from datetime import datetime


with open ('monthly_TSLA.csv', 'r') as csv_file:
    csvr = csv.reader(csv_file)
    next(csvr)
    close = []
    timestamp = []
    for line in csvr:
        ## Might be no BSR in some sells so putting None in place of them.
        try:
            closetofloat = float(line[2])
            close.append(closetofloat)
        except Exception as e:
            print(e)
        tmstoint = datetime.strptime(line[0], '%Y-%m-%d')
        ## For excel saved.
        # tmstoint = datetime.strptime(line[7], '%m/%d/%y %H:%M')
        timestamp.append(tmstoint)



fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))

ax1.plot_date(timestamp, close, '-', label='Actual data', color='r')
ax1.fill_between(timestamp, close, 250, facecolors='c', alpha=0.3)

for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)
ax1.grid(True)

# ax1.set_yticks([500, 700, 900, 1100, 1300])
# plt.bar(x, y, label='dummy data 1', color='red')
# plt.bar(x2, y2, label='dummy data 2')
plt.xlabel('Date')
plt.ylabel('Close value in US Dollars')
plt.title('MSFT Monthly Stock')
plt.subplots_adjust(bottom=0.18, left=0.15)

plt.show()