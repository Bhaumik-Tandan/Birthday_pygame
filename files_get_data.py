import os
import random as r
qu=[]
for i in os.listdir("asset\\quit_photo"):# find the list of all files in the folder
    qu.append(i)
lu=r.randrange(len(qu))#select random image
qi=qu[lu]
#audio
qu=[]
for i in os.listdir("asset\\audio"):# find the list of all files in the folder
    qu.append(i)
#select random audio
qa=qu[r.randrange(len(qu))]
#all photos of snake
def snake_photo(p,w,h):
    pi=[]
    for i in os.listdir("asset\\snake_photo"):
        img=p.image.load(os.path.join(os.getcwd(),"asset\\snake_photo\\"+i))
        pi.append(p.transform.scale(img,(w,h)))
    return pi