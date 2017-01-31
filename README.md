## getdiskusage.py

### Purpose
Prints a list of all files in a directory and their total size in bytes in a JSON format.

### Example

./getdiskusage.py /tmp

{
    "files": {
        "/tmp/foo": 1000,
        "/tmp/bar": 1000000,
        "/tmp/buzzz": 42
    }
}

### Requirements
Requires at least Python 2.6 because of json library. Support for Python 3.x is unknown.

### Tests
./getdiskusage.py foobar

foobar is not a directory!

./getdiskusage.py /root

Cannot access /root directory!

./getdiskusage.py /foobar

Directory /foobar doesn't exist!
