from flask import Flask, render_template, request, jsonify
import storage
import utility
import json
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calendar")
def calendar():
    return render_template("calendar.html")

@app.route("/test")
def test():
    ev = [
        {"start":{"dateTime": datetime(2020, 12, 1, 1, 2, 3)}, "end":{"dateTime": datetime(2020, 12, 1, 4, 2, 3)}, "location": "toronto",  "transportMode": "driving"},
        {"start":{"dateTime": datetime(2020, 12, 2, 6, 2, 3)}, "end":{"dateTime": datetime(2020, 12, 8, 1, 2, 3)}, "location": "florida",  "transportMode": "driving"},
        {"start":{"dateTime": datetime(2020, 12, 3, 9, 2, 3)}, "end":{"dateTime": datetime(2020, 12, 3, 11, 2, 3)}, "location": "vaughan ontario",  "transportMode": "driving"}
    ]
    return utility.checkRoute(ev)

@app.route("/getEvents", methods=['GET', 'POST']) 
def getEvents():
    data = request.form['userID']
    return storage.getEvents(data)

import re

def date_hook(json_dict):
    for (key, value) in json_dict.items():
        if type(value) is str and re.match('\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d:[0-5]\d(?:\.\d+)?Z?', value):
            json_dict[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
        else:
            pass

    return json_dict


@app.route("/getOnTimeList", methods=['GET', 'POST']) 
def getOnTimeList():
    data = json.loads(request.form['events'], object_hook=date_hook)
    print(data[0]["location"])
    print("data: " + str(data))
    return utility.checkRoute(data)



if __name__ == "__main__":
    app.run(debug=True)
