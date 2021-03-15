import os
import pandas as pd
import firebase_admin
from firebase_admin import credentials,storage
from google.cloud import firestore
from firebase_admin import firestore
import csv
from Upload_to_storage import get_url
from datetime import date

def get_data(User_ID,DocumentID):
    db = firestore.client()
    doc_ref=db.collection(DocumentID)
    doc_ref.document(str(date.today()))
    doc_ref=db.collection(u"DateTime").document(str(date.today())).collection("Authorised")
    docs = doc_ref.stream()
    Time=[]
    for doc in docs:
        temp=doc.to_dict()
        if(User_ID==temp['User_ID']):
            Time.append(temp['Time'])
    return Time    