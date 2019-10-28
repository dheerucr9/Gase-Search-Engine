# -*- coding: cp1252 -*-
import pygame,sys
from pygame.locals import *
from stack import stack
import webbrowser
pygame.init()
#clock=pygame.time.Clock()

screen=pygame.display.set_mode((1366,768),FULLSCREEN)
pygame.display.set_caption("Search Engine")

background=pygame.Surface(screen.get_size())
background=background.convert()

stacking=stack()
def init():
    background.fill((255,255,255)) 
    #font=pygame.font.SysFont('Times New Roman',120)
    #text=font.render("GASÉ",1,(15,15,15))
    text=pygame.image.load('GASE LOGO.jpg')
    textpos=text.get_rect()
    textpos.centerx=background.get_rect().centerx
    textpos.centery=background.get_rect().centery-100
    background.blit(text,textpos)
    return textpos

def bo(textpos):

    box=pygame.Rect(textpos.centerx-400,textpos.bottom,800,50)
    pygame.draw.rect(background,(0,0,0),box,2)
    return box

def search(box):

    font=pygame.font.SysFont('Times New Roman',40)
    s=font.render("Search",1,(155,155,155))
    spos=s.get_rect()
    spos.centerx=box.left+spos.centerx+5
    spos.centery=box.centery
    background.blit(s,spos)
    return spos

def adv(box):

    font=pygame.font.SysFont('Times New Roman',30)
    a=font.render("Advanced",1,(255,255,255))
    apos=a.get_rect()
    apos.centerx=box.left+apos.centerx
    apos.centery=box.bottom+apos.centery+10
    #apos=apos.move(500,0)
    pygame.draw.rect(background,(0,0,0),apos)
    background.blit(a,apos)
    return apos

def backbox(box):
    im=pygame.image.load('back.jpg')
    bbox=im.get_rect()
    bbox=pygame.Rect(box.left-71,box.top,71,50)
    #pygame.draw.rect(background,(0,0,0),bbox,2)
    background.blit(im,bbox)
    return bbox

     
#Main
t=init()
box=bo(t)
spos=search(box)
apos=adv(box)

cap=0
screen.blit(background,(0,0))
pygame.display.flip()
about=0
i=1
frame=0
back=0
b=''
searc=0
abit=0
ent=0
count=0
categ=''
lstring=['amrita','sport','arts','technology','food','music','socialmedia','entertainment']
  
def advanced():
    l=[]
    background.fill((236,248,241))
    t1=pygame.image.load('Amrita_logo.jpg')
    t1=background.blit(t1,(50,350))
    l.append(t1)
    
    t2=pygame.image.load('logosport1.png')
    t2=background.blit(t2,(t1.right+10,200))
    l.append(t2)
    
    t3=pygame.image.load('artya.png')
    t3=background.blit(t3,(t2.right+30,300))
    l.append(t3)
    
    t4=pygame.image.load('tech_logo1.png')
    t4=background.blit(t4,(t3.right+30,200))
    l.append(t4)

    t3=pygame.image.load('food.png')
    t3=background.blit(t3,(t4.right+30,250))
    l.append(t3)

    t4=pygame.image.load('yoyo.png')
    t4=background.blit(t4,(t3.centerx-130,t3.bottom+100))
    l.append(t4)

    #t4=pygame.image.load('social-media-logos1.png')
    #t4=background.blit(t4,(50,300))
    #l.append(t4)

    t3=pygame.image.load('social-media-logos1.png')
    t3=background.blit(t3,(70,t1.bottom+60))
    l.append(t3)
    
    t4=pygame.image.load('entertainment1.png')
    t4=background.blit(t4,(t3.right+100,t3.top-50))
    l.append(t4)

    bo(t)
    search(box)
    return l

    #screen.blit(background,(0,0))
    #pygame.display.flip()# pygame.key.set_repeat()


def web(q,s,bot):
    background.fill((236,248,241))
    pygame.draw.rect(background,(255,255,255),q.move(0,-350))
    pygame.draw.rect(background,(0,0,0),bot.move(0,-350),2)
    background.blit(s,se.move(0,-350))
    return adv(q.move(0,-350))
                
def searchprint():
    webl=[]
    #if categ=='':
        #call general search fn
    #else:
        #call advanced search fn
    #q=pygame.draw.rect(background,(255,255,255),box)
    #bo(t)
    #font=pygame.font.SysFont('Times New Roman',40)
    #s=font.render(b,1,(0,0,0))
    #background.blit(s,spos)
    font=pygame.font.SysFont('Times New Roman',20)
    data=font.render("Facebook",1,(0,0,0))
    datapos=data.get_rect()
    website=font.render("www.facebook.com",1,(0,0,0))
    webpos=website.get_rect()
    datapos=datapos.move(100,300)
    alpha=pygame.Rect(datapos.left,datapos.top,600,20)
    for w in range(4):
        pygame.draw.rect(background,(255,255,255),alpha)
        data=font.render("Facebook",1,(0,0,0))
        website=font.render("www.facebook.com",1,(0,0,0))
        webpos.left=alpha.right+10
        webpos.top=alpha.top
        background.blit(website,webpos)
        background.blit(data,datapos)
        datapos=datapos.move(0,27)
        alpha=alpha.move(0,27)

    webl=[webpos,webpos.move(0,-27),webpos.move(0,-54),webpos.move(0,-81)]
    screen.blit(background,(0,0))
    pygame.display.flip()
    return webl
                
while 1:
    if back==1:
        bbox=backbox(box)
    for event in pygame.event.get():
        if event.type==KEYDOWN  and event.key==K_ESCAPE:
            pygame.quit()
            sys.exit()
        elif event.type==KEYDOWN and event.key==K_HOME:
            t=init()
            box=bo(t)
            spos=search(box)
            apos=adv(box)
                
            cap=0
            #screen.blit(background,(0,0))
               #pygame.display.flip()
            about=0
            i=1
            frame=0
            back=0
            b=''
            searc=0
            abit=0
            ent=0
            categ=''
            lstring=['amrita','arts','food','sport','maths','music','socialmedia','technology','entertainment']
  

        elif event.type==MOUSEBUTTONDOWN:
            (x,y)=pygame.mouse.get_pos()
            if abit==0:
                if box.collidepoint((x,y)) and i==1:
                    b=''
                    i=2
            #advanced
                if apos.collidepoint((x,y)) and frame==0:
                    b=''
                    i=1
                    frame=1
                    about=1
                    abit=1
                    if searc>0:
                        t=t.move(0,350)
                        box=box.move(0,350)
                        spos=spos.move(0,350)
                        apos=adv(box)
                        back=0
                        searc=0
                        
                    #searc=0
                    l=advanced()
                
            #about
                elif t.collidepoint((x,y)) and frame==0 and about==0 and (i==1 or i==2):
                    background.fill((236,248,241))
                    frame=1
                    i=3

            if abit==1:
                for z in range(len(l)):
                    if l[z].collidepoint((x,y)):
                        categ=lstring[z]
                        print categ
                        abit=0
                        break
            if back==1:
                if bbox.collidepoint((x,y)):
                    if stacking.isempty():
                        back=0
                        background.fill((255,255,255))
                        init()
                        font=pygame.font.SysFont('Times New Roman',25)
                        ret=font.render("Press 'Home' to return",1,(0,0,0))
                        retpos=ret.get_rect()
                        retpos.centerx=background.get_rect().centerx
                        retpos.centery=background.get_rect().centery+50
                        background.blit(ret,retpos)
                    else:
                        b=stacking.pop()
                        print b
                        webl=searchprint()
            if searc>0:
                for z in range(4):
                    if webl[z].collidepoint(pygame.mouse.get_pos()):
                        webbrowser.open('www.facebook.com')

        elif event.type==KEYDOWN and i==2:
            count+=1
            if event.key==K_RETURN:
                stacking.push(b)
                print b
                frame=1
                count=0
                back=1
                about=1
                searc+=1
                i=1
                ent=1
                
            elif event.key==K_BACKSPACE:
                b=b[0:-1]
                count-=2
            elif event.key==K_SPACE:
                b=b+' '
            elif event.key==K_TAB:
                b=b+'   '
            elif event.key==K_CAPSLOCK:
                if cap==0:
                    cap=1
                elif cap==1:
                    cap=0
                
            elif (event.key in range(97,123)) or (event.key in range(48,58)):
                a=pygame.key.name(event.key)
                if cap==1:
                    a=a.upper()
                b=b+a
            else:
                continue
            
            #if i==2:
            q=pygame.draw.rect(background,(255,255,255),box)
            bo(t)
            font=pygame.font.SysFont('Times New Roman',40)
            s=font.render(b,1,(0,0,0))
            if s.get_rect().width>box.width:
                k=s.get_rect().width-box.width
                bprint=b[count-30:-1]
                
            else:
                bprint=b
            print bprint
            s=font.render(bprint,1,(0,0,0))
            se=background.blit(s,spos)
            if b=='':
                search(box)
            if ent==1:
                if searc==1:
                    t=t.move(0,-350)
                    box=box.move(0,-350)
                    spos=spos.move(0,-350)
                    apos=web(q,s,box)
            
                frame=0
                ent=0
                webl=searchprint()

    screen.blit(background,(0,0))
    pygame.display.flip()



