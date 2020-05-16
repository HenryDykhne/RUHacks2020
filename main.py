from flask import Flask, render_template

import utility
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime, timedelta

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'ru-hacks-2020',
})

db = firestore.client()

app = Flask(__name__)

@app.route("/")
def home():
    writeEvents()
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

def writeEvents():
    doc_ref = db.collection(u'users').document(u'userID')
    doc_ref.set({
        u'events': [
            u'dummyEvent1',
            u'dummyEvent2'
        ]
    })

if __name__ == "__main__":
    app.run(debug=True)
