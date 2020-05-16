import itertools
from datetime import datetime, timedelta
##events passed to this function must be ordered by time
def checkRoute(events):
    onTimeList = []
    for first, second in itertools.izip(l, l[1:]): 
        onTimeList.append(onTime(first, second, first.transportMode))
    return onTimeList

def onTime(firstEvent, secondEvent, transportMode):
    transitTime = 13000##dummy. this is where transit time must be calculated
    earlyBy = secondEvent.start.dateTime - (firstEvent.end.dateTime + timedelta(seconds=transitTime))
    if earlyBy >= 0 
        onTime = True
    else
        onTime = False

    return {
            u'onTime': onTime,
            u'transitTime': transitTime,
            u'earlyBy': earlyBy
        }

ev = [{"start":{"dateTime":}, ""}]
print(checkRoute(ev)):