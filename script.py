import os,shutil

def check_delete(path):
    if(os.path.exists(path)):
        os.remove(path)


def check_delete_dir(path):
    if(os.path.isdir(path)):
        shutil.rmtree(path)

check_delete("./data.dat")
check_delete("./StudentDetails.csv")

check_delete_dir("./Images")
check_delete_dir("./__pycache__")
