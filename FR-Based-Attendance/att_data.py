import pandas as pd
import numpy as np
import datetime

def present(id):

    k = str(datetime.datetime.today())
    k=k[8:10]
    df = pd.read_csv("Attendance.csv")
    df.set_index("ID",inplace=True)
    df["Day  "+k][id]="Present"
    df.to_csv("Attendance.csv")


