import os
path = "---add your basepath to this repository here ----"
folders = os.listdir("../Posters")
#remove the .py file from the list
folders.remove("rename.py")

for file in folders:
    for index, poster in enumerate(os.listdir(path+"/"+file)):
        print("Name: ", poster, "New Name: ", file+"_Poster"+str(index+1)+".pdf")
        os.rename(path+"/"+file+"/"+poster, "./"+file+"/"+file+"_Poster"+str(index+1)+".pdf")
    