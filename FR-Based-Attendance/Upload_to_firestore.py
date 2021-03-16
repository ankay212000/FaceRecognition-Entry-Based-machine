import os
import pandas as pd
import firebase_admin
from firebase_admin import credentials,storage
from google.cloud import firestore
from firebase_admin import firestore
import csv
from Upload_to_storage import get_url
from datetime import date

def Upload(tmp,DocumentID):
    db = firestore.client()
    doc_ref = db.collection(DocumentID)
    '''if(DocumentID=="DateTime"):
        doc_ref.document(str(date.today()))
        doc_ref=db.collection(u"DateTime").document(str(date.today())).collection("Authorised")
        doc_ref.document(tmp['User_ID']).set(tmp)
        #list(map(lambda x: doc_ref.document(x['User_ID']).set(x), tmp))'''
    doc_ref.document(tmp['User_ID']).set(tmp)        
