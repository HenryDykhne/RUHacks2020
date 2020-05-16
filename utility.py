import itertools
import distance
import json
from datetime import datetime, timedelta

##events passed to this function must be ordered by time
def checkRoute(events):
    onTimeList = []
    for firstEvent, secondEvent in itertools.izip(events, events[1:]): 
        onTimeList.append(onTime(firstEvent, secondEvent, firstEvent["transportMode"]))

    return json.dumps(onTimeList)

def onTime(firstEvent, secondEvent, transportMode):
    try:
        transitTime = distance.tripDuration(firstEvent["location"], secondEvent["location"], transportMode)  
    except Exception as error:
        return {"error": error}
    
    earlyBy = secondEvent["start"]["dateTime"] - (firstEvent["end"]["dateTime"] + timedelta(seconds = transitTime))
    if earlyBy >= timedelta(seconds = 0):
        onTime = True
    else:
        onTime = False

    return {
        u'onTime': onTime,
        u'transitTime': transitTime,
        u'earlyBy': str(earlyBy)
    }

ev = [
    {"start":{"dateTime": datetime(2020, 12, 1, 1, 2, 3)}, "end":{"dateTime": datetime(2020, 12, 1, 4, 2, 3)}, "location": "toronto",  "transportMode": "driving"},
    {"start":{"dateTime": datetime(2020, 12, 2, 6, 2, 3)}, "end":{"dateTime": datetime(2020, 12, 8, 1, 2, 3)}, "location": "florida",  "transportMode": "driving"},
    {"start":{"dateTime": datetime(2020, 12, 3, 9, 2, 3)}, "end":{"dateTime": datetime(2020, 12, 3, 11, 2, 3)}, "location": "vaughan ontario",  "transportMode": "driving"}
]
print(checkRoute(ev))
