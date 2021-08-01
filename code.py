import pygame as p
import os
import random as r
p.init()
d=p.display.set_mode((540,570),p.FULLSCREEN)#display width
#quit image selection
qu=[]
for i in os.listdir("asset\\quit_photo"):# find the list of all files in the folder
    qu.append(i)
lu=r.randrange(len(qu))#select random image
a=p.image.load(os.path.join(os.getcwd(),"asset\\quit_photo\\"+qu[lu]))#quit image
#audio
qu=[]
for i in os.listdir("asset\\audio"):# find the list of all files in the folder
    qu.append(i)
lu=r.randrange(len(qu))#select random audio
p.mixer.music.load(os.path.join(os.getcwd(),"asset\\audio\\"+qu[lu]))#audio
p.mixer.music.play(-1)
#all photos of snake
pi=[]
for i in os.listdir("asset\\snake_photo"):
    img=p.image.load(os.path.join(os.getcwd(),"asset\\snake_photo\\"+i))
    pi.append(p.transform.scale(img,(30,30)))
p.display.set_icon(a)#icon photo
c = p.time.Clock() 
def fun(m):
    while True:
        a=p.transform.scale(pic,(d.get_size()[0],d.get_size()[1]))
        d.blit(a,(0,0))
        #quit text
        d.blit(p.font.SysFont("bahnschrift",25).render(m+"! Press C-Play Again or Q-Quit",True,(255,0,0)), [d.get_size()[0]/4,d.get_size()[1]/2])
        p.display.update() 
        for event in p.event.get():
               if event.type == p.KEYDOWN:
                  if event.key == p.K_q:
                     p.quit()
                     exit()
                  if event.key == p.K_c:
                     gameLoop()      
               if event.type==p.QUIT:
                   p.quit()
def gameLoop():
    #start index
    x1=270
    y1=240
    l=r.randrange(len(pi))
    x1_change=0
    y1_change=0
    sp=5
    sl=[]
    se=[pi[r.randrange(len(pi))]]
    foodx=r.randrange(18)*30
    foody=r.randrange(17)*30+60# +60 is so that food does not come on upper image
    sl.append([x1,y1])
    while True: 
        for event in p.event.get():
            if event.type==p.QUIT:
                p.quit()
            if event.type==p.KEYDOWN:
                if event.key == p.K_LEFT:
                    if x1_change ==30:#this is if snake is moving in right and we say to to go to left it should not overlap
                        break
                    x1_change = -30
                    y1_change = 0
                elif event.key == p.K_RIGHT:
                    if x1_change ==-30:
                        break
                    x1_change = 30
                    y1_change = 0
                elif event.key == p.K_UP:
                    if y1_change ==30:
                        break
                    y1_change = -30
                    x1_change = 0
                elif event.key == p.K_DOWN:
                    if y1_change ==-30:
                        break
                    y1_change = 30
                    x1_change = 0 
                elif event.key==p.K_ESCAPE:#escape to go to menu
                    fun("You press excape")
        x1 += x1_change
        y1 += y1_change
        if x1 >=d.get_size()[0] or x1 < 0 or y1>=d.get_size()[1] or y1 < 60:# this is if we go out of screen
            fun("You hit the boundry")
            return 0
        d.fill((150,150,0))
        qu=[]
        for i in os.listdir("asset\\birthday_photo"):# happy birthday photo
            qu.append(i)
        lu=r.randrange(len(qu))#select random audio
        b=p.image.load(os.path.join(os.getcwd(),"asset\\birthday_photo\\"+qu[lu]))#the birthday imae keep on blinking
        b=p.transform.scale(b,(d.get_size()[0],60))
        d.blit(b,(0,0))
        f=0
        if x1 == foodx and y1 == foody:
            sp+=0.2
            while True:
                foodx=r.randrange(18)*30
                foody=r.randrange(17)*30+60
                if [foodx,foody] not in sl:
                    break
            se.append(pi[l])
            f=1
            l=r.randrange(len(pi))
        d.blit(pi[l],(foodx,foody))
        msg="Your Score: "+str(len(sl)-1)
        d.blit(p.font.SysFont("bahnschrift",25).render(msg,True,(255,0,0)),[300,540])
        snake_Head=[x1,y1]
        if f==0:
            del sl[0]
        for x in sl[::-1]:#incase the snake colides to itself
            if x == snake_Head:
                fun("You have hit the snake")
        sl.append([x1,y1])
        for x in range(len(sl)-1,-1,-1):
             d.blit(se[x],(sl[x][0],sl[x][1]))
        p.display.update()    
        c.tick(sp)
pic=a        
gameLoop()