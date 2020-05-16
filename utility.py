import itertools
import distance
from datetime import datetime, timedelta

##events passed to this function must be ordered by time
def checkRoute(events):
    onTimeList = []
    for firstEvent, secondEvent in itertools.izip(events, events[1:]): 
        onTimeList.append(onTime(firstEvent, secondEvent, firstEvent["transportMode"]))

    return onTimeList

def onTime(firstEvent, secondEvent, transportMode):
    try:
        transitTime = distance.tripDuration(firstEvent["location"], secondEvent["location"], transportMode)  
    except Exception as error:
        return {"error": error}
    
    earlyBy = secondEvent["start"]["dateTime"] - (firstEvent.get["end"]["dateTime"]  + timedelta(seconds = transitTime))
    if earlyBy >= 0:
        onTime = True
    else:
        onTime = False

    return {
        u'onTime': onTime,
        u'transitTime': transitTime,
        u'earlyBy': earlyBy
    }
ev = [
    {"start":{"dateTime": 100000}, "end":{"dateTime": 200000}, "location": "toronto",  "transportMode": "driving"},
    {"start":{"dateTime": 400000}, "end":{"dateTime": 500000}, "location": "florida",  "transportMode": "driving"},
    {"start":{"dateTime": 800000}, "end":{"dateTime": 900000}, "location": "vaughan ontario",  "transportMode": "driving"}
]
print(checkRoute(ev))
