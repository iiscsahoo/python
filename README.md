## nextbus.py

### Purpose

A program which will tell you how long it is until the next bus on "BUS ROUTE" leaving from "BUS STOP NAME" going "DIRECTION"
using the api defined at http://svc.metrotransit.org/.

"BUS ROUTE" will be a substring of the bus route name which is only in one bus route, 
"BUS STOP NAME" will be a substring of the bus stop name which is only in one bus stop on that route, and
"DIRECTION" will be "north", "east", "west", or "south"

The program won’t return anything if the last bus for the day has already left.
The bus route, stop and direction are all case insensitive.
If using partial names for routes and stops the first occurrence returned will be used.


### Example

$ nextbus.py "metro blue line" "target field station platform 1" "south"

8 Minutes

### Requirements

Requires at least Python 2.6 because of requests library (https://github.com/kennethreitz/requests).
Request library can be installed via pip (pip install requests).
Support for Python 3.x is unknown.

### Tests

$ nextbus.py "foobar" "target field station platform 1" "south"

Usage: nextbus.py route stop direction

$ nextbus.py "foobar" "target field station platform 1" "south"

Route foobar doesn't exist!

$ nextbus.py "metro blue line" "target field station platform 1" "foobar"

Direction foobar doesn't exist for route metro blue line!

$ nextbus.py "metro blue line" "foobar" "south"

Stop foobar doesn't exist for route metro blue line and direction south!