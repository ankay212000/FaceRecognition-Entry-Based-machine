import os,shutil

os.remove("./data.dat")
os.remove("./StudentDetails.csv")

shutil.rmtree("./Images")
shutil.rmtree("./__pycache__")