#!/usr/bin/python
#

import sys, os , errno, json

if len(sys.argv) != 2:
    print "Usage: " + sys.argv[0] + " /directory"
    sys.exit(1)

try:
    os.chdir(sys.argv[1])
except IOError as e:
    if e.errno == errno.ENOENT:
        print sys.argv[1] + " doesn't exist!"
        sys.exit(1)
    if e.errno == errno.EACCES:
        print "Cannot access " + sys.argv[1]
        sys.exit(1)

files = {}

for file in os.listdir(os.getcwd()):
    file = os.getcwd() + "/" + file
    files[file] = os.lstat(file).st_size

print json.dumps({"files" : [files]}, indent=4)