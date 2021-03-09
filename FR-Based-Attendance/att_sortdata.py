import pandas as pd
import numpy as np
import datetime
import os


def att(id,name):

    exists = os.path.isfile("Attendance.csv")
    if(exists):
        df = pd.read_csv("Attendance.csv")
        df.set_index("ID", inplace=True)
        df1 = pd.DataFrame({"ID": [id], "NAME": [name]})
        df1.set_index("ID", inplace=True)
        df = df.append(df1, sort=False)
        df = df.sort_index()

        df.to_csv("Attendance.csv")

    else:
        df = pd.read_csv("StudentDetails.csv")
        df.set_index("ID", inplace=True)
        df=df.drop("PASSWORD",axis=1)
        #Adding days
        for i in range(1, 32):
            st = str(i) if i>10 else "0"+str(i)
            df["Day  "+st] = ""
        df.to_csv("Attendance.csv")
        



