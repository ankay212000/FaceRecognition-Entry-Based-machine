# importing the requests library 
import requests 
import pandas as pd
def req():
    # defining the api-endpoint 
    API_ENDPOINT = "http://sourav2k.pythonanywhere.com/api-view/studentmodel/"
    csvfile = "D:/Python/Project/FR-Based-Attendance-master/StudentDetails.csv"

    data = pd.read_csv(csvfile)

    for i in data.values:
        username = i[0]
        password = i[2]
        first_name = i[1]
        
        data  = {
            'username':username,
            'password':password,
            'first_name': first_name,
            'last_name':' ',
        }
        r = requests.post(url = API_ENDPOINT,data=data)
        print(r)
            