import requests
import json
import os
def getfilenames():
    os.system('ls *.html >files.txt')
    o=open ("files.txt","r")
    files=o.read().split('\n')
    return files;
    
files =getfilenames()
files=files[:-1]

#print(files)

def getconfig(text):
    t=text.split("var config =")
    t=t[1]
    t=t.split(";")
    return t[0]
g=open("download.bat","w")
#g.write("test")
#g.close()

def downloadfiles(array):
    i=1
    for element in array:
        f=open(element,"r")
        text=f.read()
        f.close()
        y = json.loads(getconfig(text))
        d=y['request']['files']['progressive']
        for profile in d:
            if profile["quality"]=="720p":
                os.system("wget "+profile["url"]+" -O "+str(i)+"-"+element.replace("html","mp4")+"\n")
                print("done "+str(i))
        i+=1
        

downloadfiles(files)
g.close()




