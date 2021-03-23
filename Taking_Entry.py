import face_recognition as fr
import cv2
import numpy as np 
import pickle
import time
import os
from datetime import datetime
from Upload_to_storage import get_url
from Upload_to_firestore import Upload
from Export_Data_from_firebase import get_data

notif=""
def attend():
    global notif
    exist=os.path.isfile("data.dat")
    if(exist==False):
        notif="No Registration"
        return
    else:    
        font=cv2.FONT_HERSHEY_SIMPLEX

        #Loading data.dat file
        file=open("./data.dat",'rb')
        Ens,Ids,Names=pickle.load(file)
        file.close()
        f=0
        video = cv2.VideoCapture(0)
        width,height = int(video.get(3)), int(video.get(4))
        detected = False
        while(1):
            #Load test image
            check,img=video.read()
            img=cv2.flip(img,1)
            box_x,box_y,box_l =int((width - 0.5*height) // 2),int(0.25*height),int(0.5*height)
            cv2.rectangle(img,(box_x,box_y,box_l,box_l),(50,150,40),8)
            crop=img[box_y:box_y+box_l,box_x:box_x+box_l]
            #test=cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
            test=cv2.cvtColor(crop,cv2.COLOR_BGR2RGB)
            
            name="Unknown"
            if(f>40):
                faces_loc=fr.face_locations(test)
                en_faces=fr.face_encodings(test,faces_loc)
                notif = ""
                for (top,right,bottom,left),en in zip(faces_loc,en_faces):
                    #(top,right,bottom,left)=(top*4,right*4,bottom*4,left*4)
                    name="Unknown"
                    id=0
                    matches=fr.compare_faces(Ens,en,0.45)
                    
                    if(True in matches):
                        index=matches.index(True)
                        name=Names[index]
                        id=Ids[index]
                        notif="Entry Done Successfully"  
                    else:
                        notif = "" 
                        id = 0   
                    cv2.putText(img,f"{id} {name}",(left+180,top+100),font,1,(255,0,0),2)
                    cv2.rectangle(crop,(left,top),(right,bottom),(0,0,255),2)
                    if(name=="Unknown"):
                        notif=" "
                        if(f>43):
                            cv2.rectangle(img,(left+230,bottom+160),(left+450,bottom+130),(0,0,255),cv2.FILLED)
                            cv2.putText(img,"Please retry",(left+240,bottom+150),font,1,(255,255,255),2)
                    else:
                        cv2.rectangle(img,(left+190,bottom+160),(left+450,bottom+130),(0,0,255),cv2.FILLED)
                        cv2.putText(img,"Entry Taken",(left+240,bottom+155),font,1,(255,255,255),2)
                        # Upload to cloud here
                        # Image_Path1=f"Images/{id} {name}1.jpg"
                        # print(Image_Path1)
                        # Image=get_url(Image_Path1)

                        detected = True
                        notif="Entry Done Successfully"

                    f=f+1
            cv2.imshow("Capture",img)
            if(f>42 and name!="Unknown"):
                time.sleep(0.3)
                break
                
            if(f>48 and name=="Unknown"):
                time.sleep(0.3)
                break
            f=f+1
            key=cv2.waitKey(1)
            if(key==ord(' ')):
                break
            if(cv2.getWindowProperty("Capture",0)):
                break
    video.release()
    cv2.destroyAllWindows()
    if(detected):
        Time,Date,image,password=get_data(str(id),"User_Data")
        #print(Time,Date,image)
        Time.append(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        tmp={'User_ID':str(id),'Time':Time,'Name':str(name),'Date':Date,'Image':image,'Password':password}
        #print(tmp)
        Upload(tmp,'User_Data')
        Upload(tmp,'DateTime')