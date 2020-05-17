import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime, timedelta
from flask import jsonify

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'ru-hacks-2020',
})

db = firestore.client()

def writeEvents():
    doc_ref = db.collection(u'users').document(u'userID')
    doc_ref.set({
        u'events': [
            u'dummyEvent1',
            u'dummyEvent2'
        ]
    })

def getEvents(userID):
    doc_ref = db.collection(u'users').document(userID)

    doc = doc_ref.get().to_dict()
    if doc:
        print(doc)
        return jsonify(doc)
    else:
        raise ValueError('failed to get document')

##getEvents("userID")