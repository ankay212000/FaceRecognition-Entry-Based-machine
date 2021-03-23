import os
import pandas as pd
import firebase_admin
from firebase_admin import credentials,storage
from google.cloud import firestore
from firebase_admin import firestore
import csv
from Upload_to_storage import get_url
from datetime import date
from Initialise_firebase import initialise

def get_admin():
    db = firestore.client()
    doc_ref=db.collection('admin')
    docs = doc_ref.stream()
    temp={}
    for doc in docs:
        temp=doc.to_dict()  
    return temp    
