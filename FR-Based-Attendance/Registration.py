import face_recognition as fr
import numpy as np 
from os import path
import pickle
import selfie
import reg_data
from datetime import datetime
from Upload_to_storage import get_url
from Upload_to_firestore import Upload
from Export_Data_from_firebase import get_data

notif=""
#Taking input...
def registration(id,name):
    
    global notif
    if(name == ""):
        notif = "Name is required."
        return
    if(id.isdigit()):
        id=int(id)
    else:
        notif="Invalid ID Please Retry"
        return    
#Checking if file already exists...
    exists = path.isfile('./data.dat')
    f=  True
#If exists then append...
    if(exists):
    #Read data from the data.dat file and check if id already exists.
        fileobj=open("data.dat",'rb')
        r_ens,r_ids,r_names=pickle.load(fileobj)
        fileobj.close()
        if(id in r_ids):
            lst=r_ids.tolist()
            notif=f"Id= {id} already registered,\nWith Name = {r_names[lst.index(id)]}."    
            return

        name=name[0].upper() + name[1:].lower()

    # Code for Taking the photo and saving it in f"{name}.jpg" 
        selfie.input(id,name)

    #Code for creating a face_encodings,id,name array of current user.
        try:
            img1=fr.load_image_file(f"./Images/{id} {name}1.jpg")
            en1=fr.face_encodings(img1)[0]

            img2=fr.load_image_file(f"./Images/{id} {name}2.jpg")
            en2=fr.face_encodings(img2)[0]


            Ids=np.array([id,id])
            Names=np.array([name,name])
            Ens=np.array([en1,en2])

    #Appending manuallly..
    
    #Add more data,i.e. the data of current user.
            Ens=np.append(r_ens,Ens,axis=0)
            Ids=np.append(r_ids,Ids)
            Names=np.append(r_names,Names)
    
    #Overwriting the data file with new data.
            fileobj1=open("data.dat",'wb')
            pickle.dump((Ens,Ids,Names),fileobj1)
            Image_Path1=f"Images/{id} {name}1.jpg"
            Image=get_url(Image_Path1)
            print(Image)    
            Time=[(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))]
            tmp={'User_ID':str(id),'Time':Time,'Name':str(name),'Image':Image,'Date':datetime.today()}
            #print(tmp)
            Upload(tmp,'User_Data')
            notif=f"[Id= {id} , Name= {name}] registered."
            fileobj1.close()
        except:
            notif="Please Retry"
            f = False 

#If not exists then create..
    else:
        #name=input("Enter Name- ")
        name=name[0].upper() + name[1:].lower()

    # Code for Taking the photo and saving it in f"{name}.jpg" 
        selfie.input(id,name)
    

    #Code for creating a face_encodings,id,name array of current user.
        if(1):
            img1=fr.load_image_file(f"./Images/{id} {name}1.jpg")
            en1=fr.face_encodings(img1)[0]

            img2=fr.load_image_file(f"./Images/{id} {name}2.jpg")
            en2=fr.face_encodings(img2)[0]

            Ids=np.array([id,id])
            Names=np.array([name,name])
            Ens=np.array([en1,en2])

    #Create first data file
            fileobj=open("data.dat",'wb')
            pickle.dump((Ens,Ids,Names),fileobj)
            Image_Path1=f"Images/{id} {name}1.jpg"
            Image=get_url(Image_Path1)
            Time=[(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))]
            tmp={'User_ID':str(id),'Time':Time,'Name':str(name),'Image':Image,'Date':datetime.today()}
            #print(tmp)
            Upload(tmp,'User_Data')
            notif=f"[Id= {id} , Name= {name}] registered."
            fileobj.close()
        else:
            notif="Please Retry"
            f = False
    if(f):           
        reg_data.do(id)