# -*- coding: cp1252 -*-
import pygame
import sys
from pygame.locals import *
from stack import stack
import webbrowser

class ds:
    def __init__(self):
        pygame.init()
        self.cap=0
        self.about=0
        self.i=1
        self.frame=0
        self.back=0
        self.b=''
        self.searc=0
        self.abit=0
        self.ent=0
        self.count=0
        self.categ=''
        self.stacking=stack()
        self.lstring=['amrita','arts','food','sport','maths','music','socialmedia','technology','entertainment']

        self.textpos=0#Position of logo
        self.box=0#Position of search box
        self.spos=0#Position the search in search box
        self.apos=0#Position of the advanced box

    def logo(self):
        self.background.fill((255,255,255))
        text=pygame.image.load('GASE LOGO.jpg')
        self.textpos=text.get_rect()
        self.textpos.centerx=self.background.get_rect().centerx
        self.textpos.centery=self.background.get_rect().centery-100
        self.background.blit(text,self.textpos)
        return self.textpos

    def bo(self):
        self.box=pygame.Rect(self.textpos.centerx-400,self.textpos.bottom,800,50)
        pygame.draw.rect(self.background,(0,0,0),self.box,2)
        return self.box
    
    def search(self):
        font=pygame.font.SysFont('Times New Roman',40)
        s=font.render("Search",1,(155,155,155))
        self.spos=s.get_rect()
        self.spos.centerx=self.box.left+self.spos.centerx+5
        self.spos.centery=self.box.centery
        self.background.blit(s,self.spos)
        return self.spos
    
    def adv(self):
        font=pygame.font.SysFont('Times New Roman',30)
        a=font.render("Advanced",1,(255,255,255))
        self.apos=a.get_rect()
        self.apos.centerx=self.box.left+self.apos.centerx
        self.apos.centery=self.box.bottom+self.apos.centery+10
        pygame.draw.rect(self.background,(0,0,0),self.apos)
        self.background.blit(a,self.apos)
        return self.apos
    
    def backbox(self):
        im=pygame.image.load('back.jpg')
        bbox=im.get_rect()
        bbox=pygame.Rect(self.box.left-71,self.box.top,71,50)
        self.background.blit(im,bbox)
        return bbox
    
    def advanced(self):
        l=[]
        self.background.fill((236,248,241))
        t1=pygame.image.load('Amrita_logo.jpg')
        t1=self.background.blit(t1,(50,350))
        l.append(t1)
        
        t2=pygame.image.load('logosport1.png')
        t2=self.background.blit(t2,(t1.right+10,200))
        l.append(t2)
        
        t3=pygame.image.load('artya.png')
        t3=self.background.blit(t3,(t2.right+30,300))
        l.append(t3)
        
        t4=pygame.image.load('tech_logo1.png')
        t4=self.background.blit(t4,(t3.right+30,200))
        l.append(t4)

        t3=pygame.image.load('food.png')
        t3=self.background.blit(t3,(t4.right+30,250))
        l.append(t3)

        t4=pygame.image.load('yoyo.png')
        t4=self.background.blit(t4,(t3.centerx-130,t3.bottom+100))
        l.append(t4)

        #t4=pygame.image.load('social-media-logos1.png')
        #t4=background.blit(t4,(50,300))
        #l.append(t4)

        t3=pygame.image.load('social-media-logos1.png')
        t3=self.background.blit(t3,(70,t1.bottom+60))
        l.append(t3)
        
        t4=pygame.image.load('entertainment1.png')
        t4=self.background.blit(t4,(t3.right+100,t3.top-50))
        l.append(t4)

        self.bo()
        self.search()
        return l

        
    def web(self,q,s,bot,se):
        self.background.fill((236,248,241))
        pygame.draw.rect(self.background,(255,255,255),q.move(0,-350))
        pygame.draw.rect(self.background,(0,0,0),bot.move(0,-350),2)
        self.background.blit(s,se.move(0,-350))
        return self.adv()


    def firstpage(self):
        self.screen=pygame.display.set_mode((1366,768),FULLSCREEN)
        pygame.display.set_caption("Search Engine")

        self.background=pygame.Surface(self.screen.get_size())
        self.background=self.background.convert()
        self.logo()
        self.box=self.bo()
        self.spos=self.search()
        self.apos=self.adv()


    def main(self):
        self.firstpage()
        while 1:
            if self.back==1:
                bbox=self.backbox()
            for event in pygame.event.get():
                if event.type==KEYDOWN  and event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.type==KEYDOWN and event.key==K_HOME:
                    d=ds()
                    self=d
                    self.firstpage()
                
                elif event.type==MOUSEBUTTONDOWN:
                    (x,y)=pygame.mouse.get_pos()
                    if self.abit==0:
                        if self.box.collidepoint((x,y)) and self.i==1:
                            self.b=''
                            self.i=2
                    #advanced
                        if self.apos.collidepoint((x,y)) and self.frame==0:
                            self.b=''
                            self.i=1
                            self.frame=1
                            self.about=1
                            self.abit=1
                            if self.searc>0:
                                self.textpos=self.textpos.move(0,350)
                                self.box=self.box.move(0,350)
                                self.spos=self.spos.move(0,350)
                                self.apos=self.adv()
                                self.back=0
                                self.searc=0
                                
                            #searc=0
                            l=self.advanced()
                        
                    #about
                        elif self.textpos.collidepoint((x,y)) and self.frame==0 and self.about==0 and (self.i==1 or self.i==2):
                            self.background.fill((236,248,241))
                            
                            self.frame=1
                            self.i=3

                    if self.abit==1:
                        for z in range(len(l)):
                            if l[z].collidepoint((x,y)):
                                self.categ=self.lstring[z]
                                print self.categ
                                self.abit=0
                                break
                    if self.back==1:
                        if bbox.collidepoint((x,y)):
                            if self.stacking.isempty():
                                self.back=0
                                self.background.fill((255,255,255))
                                self.logo()
                                font=pygame.font.SysFont('Times New Roman',25)
                                ret=font.render("Press 'Home' to return",1,(0,0,0))
                                retpos=ret.get_rect()
                                retpos.centerx=self.background.get_rect().centerx
                                retpos.centery=self.background.get_rect().centery+50
                                self.background.blit(ret,retpos)
                            else:
                                self.b=self.stacking.pop()
                                print self.b
                                webl=searchprint(self)
                    if self.searc>0:
                        for z in range(4):
                            if webl[z].collidepoint(pygame.mouse.get_pos()):
                                webbrowser.open('www.facebook.com')
                elif event.type==KEYDOWN and self.i==2:
                    self.count+=1
                    if event.key==K_RETURN:
                        self.stacking.push(self.b)
                        print self.b
                        self.frame=1
                        self.count=0
                        self.back=1
                        self.about=1
                        self.searc+=1
                        self.i=1
                        self.ent=1
                        
                    elif event.key==K_BACKSPACE:
                        self.b=self.b[0:-1]
                        self.count-=2
                    elif event.key==K_SPACE:
                        self.b=self.b+' '
                    elif event.key==K_TAB:
                        self.b=self.b+'   '
                    elif event.key==K_CAPSLOCK:
                        if self.cap==0:
                            self.cap=1
                        elif self.cap==1:
                            self.cap=0
                        
                    elif (event.key in range(97,123)) or (event.key in range(48,58)):
                        a=pygame.key.name(event.key)
                        if self.cap==1:
                            a=a.upper()
                        self.b=self.b+a
                    else:
                        continue
                    
                    #if i==2:
                    q=pygame.draw.rect(self.background,(255,255,255),self.box)
                    self.bo()
                    font=pygame.font.SysFont('Times New Roman',40)
                    s=font.render(self.b,1,(0,0,0))
                    if s.get_rect().width>self.box.width:
                        k=s.get_rect().width-self.box.width
                        bprint=self.b[self.count-30:-1]
                        
                    else:
                        bprint=self.b
                    s=font.render(bprint,1,(0,0,0))
                    se=self.background.blit(s,self.spos)
                    if self.b=='':
                        self.search()
                    if self.ent==1:
                        if self.searc==1:
                            self.textpos=self.textpos.move(0,-350)
                            self.box=self.box.move(0,-350)
                            self.spos=self.spos.move(0,-350)
                            self.apos=self.web(q,s,self.box,se)
                    
                        self.frame=0
                        self.ent=0
                        webl=searchprint(self)

            self.screen.blit(self.background,(0,0))
            pygame.display.flip()



def searchprint(s):
    font=pygame.font.SysFont('Times New Roman',25)
    data=font.render("Facebook",1,(0,0,0))
    datapos=data.get_rect()
    website=font.render("www.facebook.com",1,(0,0,0))
    webpos=website.get_rect()
    datapos=datapos.move(100,300)
    alpha=pygame.Rect(datapos.left,datapos.top,600,30)
    for w in range(4):
        pygame.draw.rect(s.background,(255,255,255),alpha)
        data=font.render(s.b,1,(0,0,0))
        website=font.render("www.facebook.com",1,(0,0,0))
        webpos.left=alpha.right+30
        webpos.top=alpha.top
        s.background.blit(website,webpos)
        s.background.blit(data,datapos)
        datapos=datapos.move(0,50)
        alpha=alpha.move(0,50)
    webl=[webpos,webpos.move(0,-27),webpos.move(0,-54),webpos.move(0,-81)]
    return webl
