import os
import pandas as pd
import firebase_admin
from firebase_admin import credentials,storage
from google.cloud import firestore
from firebase_admin import firestore


def get_url(imagePath):
    bucket = storage.bucket()
    blob = bucket.blob(imagePath)
    blob.upload_from_filename(imagePath)
    blob.make_public()

    return blob.public_url    

