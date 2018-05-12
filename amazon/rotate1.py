import os
from datetime import datetime

## Rotates the result file if they are larger than 1MB

path = '/Users/mhermac/Dropbox/Scripts/Python/epam/amazon/results_from_live/'

currtime = datetime.now()
finaldate = currtime.strftime('%Y%m%d_%M%S')


def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

for file in files(path):
    abspath = os.path.abspath(file)
    os.chdir(path)
    filesize = os.stat(file).st_size # in bytes
    if filesize < 1000000: # in bytes
        finalfilename = os.path.splitext(file)[0] + '_' + finaldate + '.csv'
        os.rename(file, finalfilename)
