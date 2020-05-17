import requests
import json

def tripDuration(origin, destination, transportMode):
    parameters = {"origins": origin, "destinations": destination, "mode": transportMode, "key": "AIzaSyBD2wdIZTDbNHGb1KjLLneHmqtxo-IMF5A"}
    response = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?", params=parameters)
    
    if response.ok:
        content = response.json()
        return content["rows"][0]["elements"][0]["duration"]["value"]
    else:
        raise ValueError('failed to get duration')
    

#tripDuration("toronto", "california", "driving")