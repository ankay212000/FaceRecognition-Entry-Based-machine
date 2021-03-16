import numpy as np 
from pickle import dump,load
fileobj1=open("data.dat",'rb')
a,b,c=load(fileobj1)
print("IDs and Names =>")
print(b,c,"\n")
fileobj1.close()
fileobj=open("passdata.dat",'rb')
r=load(fileobj)
print("Password dictionary=>")
print(r)
fileobj.close()