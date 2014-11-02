import os
import pickle
import fnmatch

tup=()
lis=[]


for dirpath,dirs,files in os.walk(r"C:\Users\keerthana\Desktop\fortune1"):
    for file in files:
        file_path = os.path.abspath(os.path.join(dirpath, file))
        if (fnmatch.fnmatch(file, "*.txt")or fnmatch.fnmatch(file, "*.log")):
            f = open(os.path.join(dirpath, file))
            data=f.read()
            tup=(file_path, data)
            lis.append(tup)




temp=open("raw_data.pickle","bw")
pickle.dump(lis,temp)

temp.close()


