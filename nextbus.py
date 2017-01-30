#!/usr/bin/python

import requests, sys, time

if len(sys.argv) != 4:
    print "Usage: " + sys.argv[0] + " route stop direction"
    sys.exit(1)

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

routeID = getData("Routes", "Description", "Route", sys.argv[1])

print routeID

directionID =  getData("Directions/" + routeID, "Text", "Value", sys.argv[3] )

print directionID

stopID = getData("Stops/" + routeID + "/" + directionID, "Text", "Value", sys.argv[2] )

print stopID

timeID = getData(routeID + "/" + directionID + "/" + stopID, "RouteDirection", "DepartureText", sys.argv[3])

print timeID