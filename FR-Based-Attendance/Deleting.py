import numpy as np 
import pickle
import os
import del_data
import deletonserver as ds
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
    fileob=open("passdata.dat",'rb')
    pass_dict=pickle.load(fileob)
    fileob.close()
    print(type(pass_dict))
    print(pass_dict)
    def upgrade(id,p,q,r):
        
        global notif,ch,check
        index=np.where(q==id)[0][0]
        name=r[index]
        notif=f"Id= {id} found with name= {name}."
        check=1
        #print(f"\nId= {id} found with name= {name}.")
        if("n" in ch):
            notif="Id not deleted."
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
            del pass_dict[id]
            fileob1=open("passdata.dat",'wb')
            pickle.dump(pass_dict,fileob1)
            fileob1.close()
            fileobj1=open("data.dat",'wb')
            pickle.dump((p,q,r),fileobj1)
            fileobj1.close()
            notif = f"Id={id}, with Name= {name} deleted."
            #print(f"\nId={id}, with Name= {name} deleted.")
            ch=""
            check=0
            del_data.deld(id)
            ds.deser(id)
            return
        
        

    if(id in q):
        upgrade(id,p,q,r)
        
    else:
        notif="Id not in database."
        return







