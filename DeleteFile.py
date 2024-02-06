import os 
import shutil

path = "test0.txt"

try:
    #os.remove(path)
    #os.rmdir(path)
    shutil.rmtree(path)
except FileNotFoundError:
    print("HMM, THERE IS NO FILE srry caps")
else:
    print("Path was deleted!")