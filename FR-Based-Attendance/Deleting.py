import numpy as np 
import pickle
import os
import del_data
check=0
ch=""
notif = ""
def delete(id):
    global notif
    if(id.isdigit()):
        id=int(id)
    else:
        notif = "Invalid ID Please Retry"
        return
        #print("Invalid ID Please Retry")

    fileobj=open("data.dat",'rb')
    p,q,r=pickle.load(fileobj)
    fileobj.close()
    
    def upgrade(id,p,q,r):
        
        global notif,ch,check
        index=np.where(q==id)[0][0]
        name=r[index]
        notif=f"ID= {id} found with name= {name}."
        check=1
        #print(f"\nID= {id} found with name= {name}.")
        if("n" in ch):
            notif="ID not deleted."
            check=0
            ch=""
            return
        elif("y" in ch):
            if(os.path.isfile("data_last_backup.dat")):
                os.remove("data_last_backup.dat")
            else:
                os.rename("data.dat","data_last_backup.dat")
            p=np.delete(p,[index,index+1],axis=0)
            q=np.delete(q,[index,index+1])
            r=np.delete(r,[index,index+1])

            fileobj1=open("data.dat",'wb')
            pickle.dump((p,q,r),fileobj1)
            fileobj1.close()
            notif = f"ID={id}, with Name= {name} deleted."
            ch=""
            check=0
            del_data.deld(id)
            # Delete on cloud here
            return
        
        

    if(id in q):
        upgrade(id,p,q,r)
        
    else:
        notif="ID not in database."
        return







