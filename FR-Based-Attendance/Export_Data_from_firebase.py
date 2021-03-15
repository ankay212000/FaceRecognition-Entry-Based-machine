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

def get_data(User_ID,DocumentID):
    db = firestore.client()
    doc_ref=db.collection(DocumentID)
    docs = doc_ref.stream()
    Time=[]
    Date=0
    image=""
    for doc in docs:
        temp=doc.to_dict()
        if(User_ID==temp['User_ID']):
            Time=(temp['Time'])  
            Date=temp['Date']
            image=temp['Image'] 
            return Time,Date,image    
