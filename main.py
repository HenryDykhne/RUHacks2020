from flask import Flask, render_template


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

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
