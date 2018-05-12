import os, re
os.chdir('testfolder/')
dirs = os.listdir()

files = [f for f in dirs if re.match(r'.*\.txt', f)] ## to find the files matching regex pattern
filefpath = []
for file in files:
    fpath = os.path.abspath(file) ## to extract the absolute path of the file
    filefpath.append(fpath)


for file in filefpath:
    with open (file, 'r') as infile:
        content = infile.readlines()

    with open(file, 'w') as outfile:
        for line in content:
            pattern = re.search(r'(^row third:)(.*)', line)
            if pattern:
                outfile.write('row third: with new config\n')
            else:
                outfile.write(line)