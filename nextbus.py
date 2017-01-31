#!/usr/bin/python

import requests, sys, time

if len(sys.argv) != 4:
    print "Usage: " + sys.argv[0] + " route stop direction"
    sys.exit(1)

route = sys.argv[1]
stop = sys.argv[2]
direction = sys.argv[3]

url = "http://svc.metrotransit.org/NexTrip/"

def getData (uri, key, value, arg):
    resp = requests.get(url + uri + "?format=json")
    if resp.status_code != 200:
        # This means something went wrong.
        print "GET " + uri + " " + resp.status_code
        sys.exit(1)

    data = resp.json()

    dataID = -1

    for item in data:
        if item[key].lower().find(arg.lower()) > -1:
            dataID = item[value]
            break

    return dataID

routeID = getData("Routes", "Description", "Route", route)

if routeID < 0:
    print "Route " + route + " doesn't exist!"
    sys.exit(1)

uri = routeID
directionID =  getData("Directions/" + uri, "Text", "Value", direction)

if directionID < 0:
    print "Direction " + direction + " doesn't exist for route " + route + "!"
    sys.exit(1)

uri = uri + "/" + directionID
stopID = getData("Stops/" + uri, "Text", "Value", stop)

if stopID < 0:
    print "Stop " + stop + " doesn't exist for route " + route + " and direction " + direction + "!"
    sys.exit(1)

uri = uri + "/" + stopID
timeID = getData(uri, "RouteDirection", "DepartureTime", direction)

if timeID != -1:
    time = int((float(timeID[6:16]) - time.time()) // 60)
    if time > 1:
        print str(time) + " minutes"
    else:
        print "1 minute"