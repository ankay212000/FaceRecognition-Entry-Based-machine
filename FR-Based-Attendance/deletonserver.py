import requests
def deser(id):

    API_ENDPOINT="http://sourav2k.pythonanywhere.com/api-view/delete/"
    data={
        'username':str(id),
    }
    rs=requests.post(url=API_ENDPOINT,data=data)