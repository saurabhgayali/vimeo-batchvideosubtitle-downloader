import requests
def getsubtitle(filename):
    
    f=open(filename,'r')
    t=f.read().split('var config =')
    t=t[1]
    t=t.split('captions":"')
    t=t[1]
    t=t.split('"')
    t=t[0]
    
    m=requests.get(t)
    m=m.text.split('URI="../../../../')
    m=m[1]
    m=m.split('"')
    m=m[0]
    
    t1=t.split('video')
    t1=t1[0]
    s=t1+m
    
    
    o=requests.get(s)
    o=o.text
    o=o.split('../../')
    o=o[1]
    o=o.split('\n')
    o=o[0]
    outurl=t1+o
    
    #outdata=requests.get(outurl).text
    
    
    #print(m)
    #print(t)
    #print(s)
    return outurl


import requests
import os

def getfilenames():
    os.system('ls *.html >files.txt')
    o=open ("files.txt","r")
    files=o.read().split('\n')
    return files;
    
files =getfilenames()
files=files[:-1]

#print(files)

#g=open("download.bat","w")
#g.write("test")
#g.close()

def downloadfiles(array):
    i=1
    for element in array:
        #print(element)
        f=open(element,"r")
        html=f.read()
        #print(html)
        f.close()
        y = getsubtitle(element)
        print(y)
        os.system("wget "+y+" -O "+str(i)+"-"+element.replace("html","vtt")+"\n")
        print("done "+str(i))
        i+=1
        

downloadfiles(files)
#g.close()












filename='377560358.html'
getsubtitle(filename)