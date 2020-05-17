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
    print("hello")
    data = request.form['userID']
    print("data: " + data)
    return storage.getEvents(data)

if __name__ == "__main__":
    app.run(debug=True)
