import os
from datetime import datetime

print(os.getcwd())

## To change directory like cd /
os.chdir('/Users/mhermac/Dropbox/Wallpapers')

# to list directory structure along with files
dirs = os.listdir()

# for dir in dirs:
#     print(dir)

## To create directory structure
# os.mkdir('demofolder/demofolder2')
# os.makedirs('demofolder/demofolder2')

## TO remove dirs
# os.rmdir()
# os.removedirs()

## To rename dir or file
# os.rename('oldname', 'newname')


## To print info about file or folder, and to get the size for example. If this is run without .st_size you will get all the possible statistics
print(os.stat('gcer.jpg').st_size / 1024)

## Getting the last modified time of dir or file in a human readable format
# mod_time = os.stat('gcer.jpg').st_mtime
# print(datetime.fromtimestamp(mod_time))

## To list directory recursively
# for dirpath, dirnames, filenames in os.walk('/Users/mhermac/Dropbox/Wallpapers'):
#     print('Current dir path: ', dirpath)
#     print('Dirs names list: ', dirnames)
#     print('File names list: ', filenames)

## To get pathes of environment variable
print(os.environ.get('HOME'))

## To join pathes in order not to confuse slashes, this build a path for us.
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)