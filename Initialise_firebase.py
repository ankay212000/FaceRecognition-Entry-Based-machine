import firebase_admin
from firebase_admin import credentials,storage
from google.cloud import firestore
from firebase_admin import firestore

def initialise():
    cred = credentials.Certificate(r".\jsonKeys\ServiceAccountKey.json")
    firebase_admin.initialize_app(cred, {"databaseURL": "https://face.firebaseio.com/",'storageBucket': 'face-b84fc.appspot.com'})
    