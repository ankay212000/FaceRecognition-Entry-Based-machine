import numpy as np
import cv2
import time
import os



check=os.path.isdir("Images")
if(check==False):
    os.mkdir("Images")
 
def input(id=0,name=" "):
    font=cv2.FONT_HERSHEY_SIMPLEX
    video = cv2.VideoCapture(0)
    width,height = int(video.get(3)), int(video.get(4))
    

    f=0
    p=-1
    while(1):
        check,frame=video.read()
        frame=cv2.flip(frame,1)
        
        
        box_x,box_y,box_l =int((width - 0.6*height) // 2),int(0.2*height),int(0.6*height)

        cv2.rectangle(frame,(box_x,box_y,box_l,box_l),(0,0,0),2)
        crop=frame[box_y:box_y+box_l,box_x:box_x+box_l]
        
        frame[0:box_y,0:width]=50
        frame[box_y+box_l:height,0:width]=50
        frame[box_y:box_y+box_l,0:box_x]=50
        frame[box_y:box_y+box_l,box_x+box_l:width]=50
        
        key=cv2.waitKey(1)
        
        if(f==0):
            cv2.putText(frame,"Press Space to take image",(int(0.15*width),int(0.1*height)),font,1,(255,0,0),2)
            if(key==ord(' ')):
                time.sleep(0.5)
                cv2.imwrite(f"./Images/{id} {name}1.jpg",crop)
                cv2.putText(frame,"1/2 Image Saved",(int(0.3*width),int(0.1*height)),font,1,(255,0,0),2)
                f=1
        if(f>0 and f<=40):
            cv2.putText(frame,"1/2 Image Saved",(int(0.3*width),int(0.1*height)),font,1,(255,0,0),2)
            f=f+1
        if(f==41):
            p=0
        if(p==0):
            cv2.putText(frame,"Tilt your head slightly and press space.",((width-640)//2,int(0.1*height)),font,1,(255,0,0),2)
            f=f+1
            if(key==ord(' ')):
                time.sleep(0.5)
                cv2.imwrite(f"./Images/{id} {name}2.jpg",crop)
                cv2.putText(frame,"2/2 Image Saved",(int(0.3*width),int(0.1*height)),font,1,(255,0,0),2)
                p=1
        if(p>0):
            cv2.putText(frame,"2/2 Image Saved",(int(0.3*width),int(0.1*height)),font,1,(255,0,0),2)
            p=p+1
            if(p==50):
                break
            
        cv2.imshow("Capture",frame)
        if(key==27):
            break   
        
    video.release()
    cv2.destroyAllWindows()
