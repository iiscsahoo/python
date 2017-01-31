#!/usr/bin/python
#

import sys, os , errno, json

# Check for exactly 2 arguments: script directory
if len(sys.argv) != 2:
    print "Usage: " + sys.argv[0] + " /directory"
    sys.exit(1)

try:
    # Try changing directory to directory passed in to find any access problems
    os.chdir(sys.argv[1])
except OSError as e:
    # If the directory doesn't exist
    if e.errno == errno.ENOENT:
        print "Directory " + sys.argv[1] + " doesn't exist!"
        sys.exit(1)
    # If the script doesn't have privileges to access directory
    if e.errno == errno.EACCES:
        print "Cannot access " + sys.argv[1] + " directory!"
        sys.exit(1)
    # If the value passed in is not a directory
    if e.errno == errno.ENOTDIR:
        print sys.argv[1] + " is not a directory!"
        sys.exit(1)

files = {}

# Loop through each file in the current working directory, excluding symlinks, which should be the directory passed in
for file in os.listdir(os.getcwd()):
    file = os.path.join(os.getcwd(), file)
    # If the file is a file add it to the list
    if os.path.isfile(file):
        files[file] = os.lstat(file).st_size

# Print the list in a JSON format
print json.dumps({"files" : files}, indent=4)