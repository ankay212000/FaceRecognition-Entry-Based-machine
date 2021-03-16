import pandas as pd
import numpy as np 
import pickle
import os
def do(id):
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

    #Creating data frame and storing in csv
    df = pd.DataFrame({'ID': ids, 'NAME': names} )
    df.set_index("ID", inplace=True)
    df.to_csv("StudentDetails.csv")
    # Upload User Data here