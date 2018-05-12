import shutil
import os
import _osx_support

#shutil.copy('testfile.txt','\epam1\\testfile.txt')
#os.chdir('//Users//mhermac//Dropbox//Scripts//Python/epam')
shutil.move('//Users//mhermac//Dropbox//Scripts//Python//epam//testfile.txt','//Users//mhermac//Dropbox//Scripts//Python//epam//testfile1.txt')

myfile=open('testfile.txt','r')

line1=myfile.readline()
line2=myfile.readline()

print(line1)
print(line2)


#myfile.write('Sa im arajin toxna. \ntenas enter tvec te che?')



myfile.close()
