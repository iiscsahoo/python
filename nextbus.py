#!/usr/bin/python
#
# script to call metro transit api to find the next bus leaving from a stop for a certain route
#
# Usage: nextbus.py route stop direction
#
import requests, sys, time

if len(sys.argv) != 4:
    print "Usage: " + sys.argv[0] + " route stop direction"
    sys.exit(1)

# populate values from cli arguments
route = sys.argv[1]
stop = sys.argv[2]
direction = sys.argv[3]

url = "http://svc.metrotransit.org/NexTrip/"

# uri: the URI stem of the request
# key: the key of the value we need to match on in the response
# value: the key for the value we need to return with
# arg: the value we need to match on in the response
def getData (uri, key, value, arg):
    resp = requests.get(url + uri + "?format=json")
    # If we don't get a 200 response back exit with status code
    if resp.status_code != 200:
        print "GET " + uri + " " + str(resp.status_code)
        sys.exit(1)

    data = resp.json()

    # default value for value not found
    dataID = -1

    for item in data:
        # if substring of value found in response
        if item[key].lower().find(arg.lower()) > -1:
            dataID = item[value]
            break

    return dataID

# get the ID of the route from the route value entered
routeID = getData("Routes", "Description", "Route", route)

# if the route wasn't found in the response
if routeID < 0:
    print "Route " + route + " doesn't exist!"
    sys.exit(1)

# start building URI stem for future calls
uri = routeID

# get the ID of the direction from the direction value entered
directionID =  getData("Directions/" + uri, "Text", "Value", direction)

# if the direction wasn't found in the response
if directionID < 0:
    print "Direction " + direction + " doesn't exist for route " + route + "!"
    sys.exit(1)

uri = uri + "/" + directionID

# get the ID of the stop from the stop value entered
stopID = getData("Stops/" + uri, "Text", "Value", stop)

# if the stop wasn't found in the response
if stopID < 0:
    print "Stop " + stop + " doesn't exist for route " + route + " and direction " + direction + "!"
    sys.exit(1)

uri = uri + "/" + stopID

# get the timestamp of the next bus leaving on route, direction, and stop entered
timeID = getData(uri, "RouteDirection", "DepartureTime", direction)

# if default value isn't present figure out when next bus departing
if timeID != -1:
    # get 10 digit timestamp from response, subtract from current time, and dive by 60 to get minutes as an integer
    time = int((float(timeID[6:16]) - time.time()) // 60)
    # if more than 1 minute until arrival, otherwise always print 1 minute
    if time > 1:
        print str(time) + " minutes"
    else:
        print "1 minute"