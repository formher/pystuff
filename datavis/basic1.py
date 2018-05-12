import matplotlib.pyplot as plt
import csv
from datetime import datetime


with open ('/Users/mhermac/Dropbox/Scripts/Python/epam/amazon/results_from_live/B01MYRWIBV.csv', 'r') as csv_file:
    csvr = csv.reader(csv_file)
    next(csvr)
    bsr = []
    timestamp = []
    for line in csvr:
        ## TODO Find elements which are larger then previous one by 3000 points and exclude them from the list to avoid high peaks in graph
        ## Might be no BSR in some sells so putting None in place of them.
        try:
            bsrtoint = int(line[1]) # Line[1] is the second column => BSR
            bsr.append(bsrtoint)
        except:
            bsr.append(None)
            pass
        tmstoint = datetime.strptime(line[7], '%Y-%m-%d %H:%M:%S') ## line[7] is the date column
        ## When opened and saved by Excel the data format is changed for some reason. So we should use below formatting.
        # tmstoint = datetime.strptime(line[7], '%m/%d/%y %H:%M')
        timestamp.append(tmstoint)


fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))
## To invert y axis so to show real picture, where the lower the number the hugher the rating.
ax1.invert_yaxis()

ax1.plot_date(timestamp, bsr, '-', label='Actual data', color='r')

for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)
ax1.grid(True)
plt.xlabel('Day')
plt.ylabel('BSR')
plt.title('BSR Chart')
plt.subplots_adjust(bottom=0.18, left=0.15)

plt.show()
# plt.savefig('foo.png') ## Can save is PDF as well