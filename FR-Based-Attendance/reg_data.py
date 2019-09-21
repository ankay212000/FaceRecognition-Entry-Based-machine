import pandas as pd
import numpy as np 
import pickle
import os
def do(id,password):
    #Getting data in random order
    fileobj = open("./data.dat", 'rb')
    tup = pickle.load(fileobj)
    q, r = tup[1], tup[2]
    fileobj.close()

    l=len(q)
    idd=q[0:l:2]
    named=r[0:l:2]
    #------Now idd,named contains required but unsorted data-----

    #Sorting...
    z=zip(idd,named)
    res = sorted(z, key=lambda x: x[0])
    ids=np.array([])
    ids=ids.astype('int32')
    names=np.array([])

    #Saving sorted values in ids,names array
    for i,n in res:
        ids=np.append(ids,[i])
        names=np.append(names,[n])

    #PASSWORD HANDLING..
    exists = os.path.isfile('./passdata.dat')
    if(exists):
        fileobj = open("passdata.dat", 'rb')
        pass_dict=pickle.load(fileobj)
        fileobj.close()
        pass_dict[id]=password
        fileobj1=open("passdata.dat",'wb')
        pickle.dump(pass_dict,fileobj1)
        fileobj1.close()
    else:
        pass_dict={id:password}
        fileobj = open("passdata.dat", 'wb')
        pickle.dump(pass_dict,fileobj)
        fileobj.close()
    lst = sorted(pass_dict.items())
    lst2 = []
    for i in lst:
        lst2.append(i[1])

    #Creating data frame and storing in csv
    df = pd.DataFrame({'ID': ids, 'NAME': names,"PASSWORD":lst2} )
    df.set_index("ID", inplace=True)
    df.to_csv("StudentDetails.csv")
    #problems

