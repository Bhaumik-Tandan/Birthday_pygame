import pygame as p
import os
import random as r
from json_get_data import *
from files_get_data import *
p.init()  
#audio
if fs:
    d=p.display.set_mode((ww,wh),p.FULLSCREEN)#display width
else:
    d=p.display.set_mode((ww,wh))
a=p.image.load(os.path.join(os.getcwd(),"asset\\quit_photo\\"+qi))#quit image
p.mixer.music.load(os.path.join(os.getcwd(),"asset\\audio\\"+qa))#audio
if aud:
    p.mixer.music.play(-1)
p.display.set_icon(a)#icon photo
pi=snake_photo(p,block_width,block_height)# retieve all photos
c = p.time.Clock() 
def quit(m):
    while True:
        a=p.transform.scale(pic,(d.get_size()[0],d.get_size()[1]))
        d.blit(a,(0,0))
        #quit text
        d.blit(p.font.SysFont(m_font_type,m_font_size).render(m+"! Press C-Play Again or Q-Quit",True,m_font_color), [d.get_size()[0]/15,d.get_size()[1]/2])
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
    x1=block_width*9
    y1=block_height*8
    l=r.randrange(len(pi))
    x1_change=0
    y1_change=0
    sp=speed
    sl=[]
    se=[pi[r.randrange(len(pi))]]
    foodx=r.randrange(ww//block_width)*block_width
    foody=r.randrange((wh-hbb)//block_height)*block_height+block_height*hbb# +60 is so that food does not come on upper image
    sl.append([x1,y1])
    while True: 
        for event in p.event.get():
            if event.type==p.QUIT:
                p.quit()
            if event.type==p.KEYDOWN:
                if event.key == p.K_LEFT or event.key == p.K_a:
                    if x1_change ==block_width and sp!=5:#this is if snake is moving in right and we say to to go to left it should not overlap and if it is only single then it may not be exceuted
                        break
                    x1_change = -block_width
                    y1_change = 0
                elif event.key == p.K_RIGHT or event.key == p.K_d:
                    if x1_change ==-block_width and sp!=5:
                        break
                    x1_change = block_width
                    y1_change = 0
                elif event.key == p.K_UP or event.key == p.K_w:
                    if y1_change ==block_height and sp!=5:
                        break
                    y1_change = -block_height
                    x1_change = 0
                elif event.key == p.K_DOWN or event.key == p.K_s:
                    if y1_change ==-block_height and sp!=5:
                        break
                    y1_change = block_height
                    x1_change = 0 
                elif event.key==p.K_ESCAPE:#escape to go to menu
                    quit("You press excape")
        x1 += x1_change
        y1 += y1_change
        if x1 >=d.get_size()[0] or x1 < 0 or y1>=d.get_size()[1] or y1 < block_width*hbb:# this is if we go out of screen
            quit("You hit the boundry")
            return 0
        d.fill("green")
        qu=[]
        for i in os.listdir("asset\\birthday_photo"):# happy birthday photo
            qu.append(i)
        lu=r.randrange(len(qu))#select random audio
        b=p.image.load(os.path.join(os.getcwd(),"asset\\birthday_photo\\"+qu[lu]))#the birthday imae keep on blinking
        b=p.transform.scale(b,(d.get_size()[0],block_width*hbb))
        d.blit(b,(0,0))
        f=0
        if x1 == foodx and y1 == foody:
            sp+=speed_increment
            while True:
                 foodx=r.randrange(ww//block_width)*block_width
                 foody=r.randrange((wh-hbb)//block_height)*block_height+block_height*hbb
                 if [foodx,foody] not in sl:
                    break
            se.append(pi[l])
            f=1
            l=r.randrange(len(pi))
        d.blit(pi[l],(foodx,foody))
        msg="Your Score: "+str(len(sl)-1)
        d.blit(p.font.SysFont(score_type,score_font_size).render(msg,True,score_font_color),[0+ww*(4/10),0+wh*(9/10)])
        snake_Head=[x1,y1]
        if f==0:
            del sl[0]
        for x in sl[::-1]:#incase the snake colides to itself
            if x == snake_Head:
                quit("You have hit the snake")
        sl.append([x1,y1])
        for x in range(len(sl)-1,-1,-1):
             d.blit(se[x],(sl[x][0],sl[x][1]))
        p.display.update()    
        c.tick(sp)
pic=a        
gameLoop()