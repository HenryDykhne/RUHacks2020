import distance
import json
from datetime import datetime, timedelta

##events passed to this function must be ordered by time
def checkRoute(events):
    onTimeList = []
    for firstEvent, secondEvent in zip(events, events[1:]): 
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


