import logging
import os
import sys

def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))
print(get_script_path())

currPath = get_script_path()

logging.basicConfig(filename=currPath + '/example.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(message)s')

a = 1
b = 3
c = a + b

try:
    a + b
except Exception as err:
    # logging.debug(err)
    logging.info(err)
    # logging.warning(err)

logging.info('Your answer is ' + str(c))


