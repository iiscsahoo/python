## nextbus.py

### Purpose

A program which will tell you how long it is until the next bus on "BUS ROUTE" leaving from "BUS STOP NAME" going "DIRECTION"
using the api defined at http://svc.metrotransit.org/.

"BUS ROUTE" will be a substring of the bus route name which is only in one bus route, 
"BUS STOP NAME" will be a substring of the bus stop name which is only in one bus stop on that route, and
"DIRECTION" will be "north", "east", "west", or "south"

### Example

$ nextbus.py "metro blue line" "Target Field Station Platform 1" "south"

8 Minutes

### Requirements

Requires at least Python 2.6 because of requests library (https://github.com/kennethreitz/requests). Support for Python 3.x is unknown.

### Tests

$ nextbus.py "foobar" "Target Field Station Platform 1" "south"

Usage: nextbus.py route stop direction

$ nextbus.py "foobar" "Target Field Station Platform 1" "south"

Route foobar doesn't exist!

$ nextbus.py "METRO Blue Line" "Target Field Station Platform 1" "foobar"

Direction blah doesn't exist for route !