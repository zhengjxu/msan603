import subprocess
import sys
import os
from datetime import datetime

def rotate_log(when, path, prefix, filename):
    '''
    This process change the file name to a suffixed version, as log rotation does

    :param when: 'S' -> second, 'M' -> minute
    :param path: path of file that needs to be rotated
    :param prefix: prefix
    :param filename: Raw.txt or proc.txt
    '''
    file='%s/%s/%s'%(path,prefix,filename)
    print(file)

    now = datetime.now()
    date=now.date()
    H=now.hour
    M=now.minute
    S=now.second

    suffix=None
    if when == 'S':
        suffix = "%s-%s-%s-%s"%(date,H,M,S)

    elif when == 'M':
        suffix = "%s-%s-%s" % (date, H, M)

    result_file = '%s/%s/%s'%(path,prefix,('-'+suffix+'.').join(filename.split('.')))

    # command line rename file
    if os.path.isfile(file):
        subprocess.call(['mv %s %s'%(file,result_file)],shell=True)


if __name__ == '__main__':
    when = 'S' # should change to 'M'

    # should change for test or homework
    path ='/srv/runme'

    prefix = sys.argv[1]
    rotate_log(when, path, prefix, 'Raw.txt')
    rotate_log(when, path, prefix, 'proc.txt')