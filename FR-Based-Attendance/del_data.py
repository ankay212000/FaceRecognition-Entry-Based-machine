import pandas as pd

import datetime

def deld(id):
    #StudentDetails file
    df = pd.read_csv("StudentDetails.csv")
    df.set_index("ID",inplace=True)
    #-----Making backup------
    df.to_csv("StudentDetailsBackup.csv")
    #------------------------
    df=df.drop([id],axis=0)
    df.to_csv("StudentDetails.csv")