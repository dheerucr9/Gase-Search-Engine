
import pickle





# -*- coding: cp1252 -*-
import pygame
import sys
from pygame.locals import *
from stack import stack
import webbrowser



 


#with open('Dict_data.pkl','rb') as input:
#    dictlist=pickle.load(input)



class stack:
    
    def __init__(self):
        self.a=[]

    def isEmpty(self):
        return len(self.a)==0

    def size(self):
        return len(self.a)

    def push(self,ob):
        self.a.append(ob)

    def pop(self):
        if self.isEmpty():
            print "STACK EMPTY"
        else:
            temp=self.a[-1]
            del self.a[-1]
            return temp


class TreeNode:
    
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def rootret(self):
        return self.root

    def __len__(self):
        return self.size

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def __setitem__(self,k,v):
       self.put(k,v)

    def get(self,key):
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.payload
           else:
                  return None
       else:
           return None

    def _get(self,key,currentNode):
       if not currentNode:
           return None
       elif currentNode.key == key:
           return currentNode
       elif key < currentNode.key:
           return self._get(key,currentNode.leftChild)
       else:
           return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
       return self.get(key)

    def __contains__(self,key):
        #print key
        if self._get(key,self.root):
            return True
        else:
            return False

    def delete(self,key):
      if self.size > 1:
         nodeToRemove = self._get(key,self.root)
         if nodeToRemove:
             self.remove(nodeToRemove)
             self.size = self.size-1
         else:
             raise KeyError('Error, key not in tree')
      elif self.size == 1 and self.root.key == key:
         self.root = None
         self.size = self.size - 1
      else:
         raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
       self.delete(key)

    def findSuccessor(self):
      succ = None
      if self.hasRightChild():
          succ = self.rightChild.findMin()
      else:
          if self.parent:
                 if self.isLeftChild():
                     succ = self.parent
                 else:
                     self.parent.rightChild = None
                     succ = self.parent.findSuccessor()
                     self.parent.rightChild = self
      return succ

    def findMin(self):
      current = self
      while current.hasLeftChild():
          current = current.leftChild
      return current
    def inord(self):
        self.inorder(self.root)
        
    def inorder(self,node):   #implement inorder and check the order
        if node==None:
            return None
        else:
            self.inorder(node.hasLeftChild())
            print(node.key,node.payload)
            self.inorder(node.hasRightChild())
        
    def remove(self,currentNode):
         if currentNode.isLeaf(): #leaf
           if currentNode == currentNode.parent.leftChild:
               currentNode.parent.leftChild = None
           else:
               currentNode.parent.rightChild = None
         elif currentNode.hasBothChildren(): #interior
           succ = currentNode.findSuccessor()
           succ.spliceOut()
           currentNode.key = succ.key
           currentNode.payload = succ.payload

         else: # this node has one child
           if currentNode.hasLeftChild():
             if currentNode.isLeftChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.leftChild
             elif currentNode.isRightChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.leftChild
             else:
                 currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
           else:
             if currentNode.isLeftChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.rightChild
             elif currentNode.isRightChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.rightChild
             else:
                 currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)


#with open('Data_Tree.pkl','rb') as input:
 #   mytree=pickle.load(input)

class PriorityQueue:
    
    def __init__(self):
        self.a=[]
        self.size=0
        self.temp_array=[]

    def enqueue(self,ob):
        self.a.append(ob)
        self.size+=1

    def isEmpty(self):
        return self.size==0

    def size(self):
        return self.size
    
    def getip(self,ip):
        self.ip=ip
        
    def ranksall(self):
        self.ranks=[]
        for vals in self.a:
            temp=0
            for ipvals in self.ip.split():
                if ipvals.lower() in vals.lower():
                    temp+=1
            self.ranks.append(vals)
            self.temp_array.append(temp)
            
    def sortall(self):
        for i in range((len(self.temp_array))):
            for j in range((len(self.temp_array)-2)):
                if self.temp_array[j]<self.temp_array[j+1]:
                    temp1=self.temp_array[j]
                    temp2=self.ranks[j]
                    self.temp_array[j]=self.temp_array[j+1]
                    self.ranks[j]=self.ranks[j+1]
                    self.temp_array[j+1]=temp1
                    self.ranks[j+1]=temp2
        
        
                    
    def dequeue(self):
        self.size-=1
        return self.ranks.pop(0)


class encode:
        
    def enc(self,ip):
        temp = 0
        self.val=0
        for l in ip:
            if l=='a' or l=='A':
                temp=10
            elif l=='b' or l=='B':
                temp=11
            elif l=='c' or l=='C':
                temp=12
            elif l=='d' or l=='D':
                temp=13
            elif l=='e' or l=='E':
                temp=14
            elif l=='f' or l=='F':
                temp=15
            elif l=='g' or l=='G':
                temp=16
            elif l=='h' or l=='H':
                temp=17
            elif l=='i' or l=='I':
                temp=18
            elif l=='j' or l=='J':
                temp=19
            elif l=='k' or l=='K':
                temp=20
            elif l=='l' or l=='L':
                temp=21
            elif l=='m' or l=='M':
                temp=22
            elif l=='n' or l=='N':
                temp=23
            elif l=='o' or l=='O':
                temp=24
            elif l=='p' or l=='P':
                temp=25
            elif l=='q' or l=='Q':
                temp=26
            elif l=='r' or l=='R':
                temp=27
            elif l=='s' or l=='S':
                temp=28
            elif l=='t' or l=='T':
                temp=29
            elif l=='u' or l=='U':
                temp=30
            elif l=='v' or l=='V':
                temp=31
            elif l=='w' or l=='W':
                temp=32
            elif l=='x' or l=='Z':
                temp=33
            elif l=='y' or l=='Y':
                temp=34
            elif l=='z' or l=='Z':
                temp=35
            '''else :
                temp=36'''
            self.val=self.val*100+temp
        return self.val


class evaluate:
    
    def __init__(self):
        self.flag1=0
        self.ans=0
        self.a=0
        self.flag=0
        self.S=stack()

    def check(self,eval_eqn):
        for val in eval_eqn:
            if val.isdigit():
                self.a=self.a*10+int(val)
                self.flag=1
            elif val=='+':
                self.S.push(self.a)
                if self.flag1==1:
                    self.mulordiv()
                    self.flag1=0
                if self.flag==1:
                    self.flag=0
                    self.S.push('+')
                self.a=0
            elif val=='-':
                self.S.push(self.a)
                if self.flag1==1:
                    self.mulordiv()
                    self.flag1=0
                if self.flag==1:
                    self.flag=0
                    self.S.push('-')
                self.a=0
            elif val=='*':
                self.S.push(self.a)
                if self.flag1==1:
                    self.mulordiv()
                    self.flag1=0
                if self.flag==1:
                    self.flag1+=1
                    self.S.push(val)
                self.flag=0
                self.a=0
            elif val=='/':
                self.S.push(self.a)
                if self.flag1==1:
                    self.mulordiv()
                    self.flag1=0
                if self.flag==1:
                    self.flag1+=1
                    self.S.push(val)
                self.flag=0
                self.a=0
        self.S.push(self.a)
        if self.flag1==1:
            self.mulordiv()

        self.ans=self.S.pop()
        while not self.S.isEmpty():
            sym=self.S.pop()
            if sym=='+':
                self.ans=self.ans+self.S.pop()
            elif sym=='-':
                self.ans=self.S.pop()-self.ans

        return self.ans
    
    def mulordiv(self):
        num=self.S.pop()
        val=self.S.pop()
        if val=='*':
            self.S.push(num*self.S.pop())
        elif val=='/':
            self.S.push((float(self.S.pop()))/num)


class read_dict:
    
    def finddict(dict_ip):
        for i in range(26):
            for vals in dictlist[i]:
                if vals==dict_ip.lower():
                    return (vals+'-'+dictlist[i][vals])


class finalop:
    
    def __init__(self,ip,f):
        self.final={}
        self.ip=ip
        self.flag=0

        self.searchfile=f
        
        self.ar_ans=0
        self.Q=PriorityQueue()
        self.yes=''
        with open(f,'rb') as input:
            self.mytree=pickle.load(input)

        
    def callfilterkey(self):
        ar_or_find=1
        wanted=['1','2','3','4','5','6','7','8','9','0',"+","-","*","/"]
        for val in self.ip:
            if not val in wanted:
                ar_or_find=0
                break
        if ar_or_find:
            print 'evaluate'
            Eval=evaluate()
            self.ar_ans=Eval.check(self.ip)
            return self.ar_ans
        else:
            if 'define' in self.ip:
                print 'dictionary'
                Read_Dict=read_dict()
                dictvaltrim=self.ip('define ')
                meaning=Read_Dict.finddict(dictvaltrim)
                if meaning:
                    print meaning
                else:
                    print 'sorry no meaning!!'
            else:
                self.yes=''
                temp=self.ip
                check=self.filterkey(temp)
                if check:
                    print 'check'
                    self.yes='yes'
                else:
                    print 'checking check1'
                    ans=''
                    for val in temp.split():
                        t=''
                        t=val+'s '
                        ans=ans+t
                    ans=ans.strip()
                    check1=self.filterkey(ans)
                    if check1:
                        print 'check1'
                        self.yes='yes'
                    else:
                        print 'checking check2'
                        temp=self.ip
                        for val in temp.split():
                            c=''
                            temp1=''
                            if val[-1]=='s':
                                for i in range(len(val)-1):
                                    c=c+val[i]
                            temp1=temp1+c
                            ans1=temp1+' '
                        ans1=ans1.strip()
                        check2=self.filterkey(ans1)
                        if check2:
                            print 'check2'
                            self.yes='yes'
                        else:
                            print "search not found"

        return self.yes

        
    def filterkey(self,changed_ip):
        iptrim=self.trim(changed_ip)            #trim off the useless words in the keywords
        ipsplit=iptrim.split()
        print 1
        print ipsplit
        
        E=encode()
        for ipsplitvals in ipsplit:
            temp = E.enc(ipsplitvals)           #encoding the trimmed input values
            if self.mytree.__contains__(temp):       #check in the binary tree for this encoded value
                finerfilter=self.mytree.get(temp)    #returns the payload
                for obs in finerfilter.keys():  #entering all values in BST under the keyword
                    if self.Q.size==0:               
                        self.Q.enqueue(obs)          
                        self.final[obs]=finerfilter[obs]
                    else:
                        if not obs in self.Q.a:
                            self.Q.enqueue(obs)
                            self.final[obs]=finerfilter[obs]

        if self.Q.isEmpty():
            return 0
        else:
            return 1
            
    def trim(self,a):
        str=''
        for x in a.split():
            x = x.lower()
            if x=='i' or x=='a' or x=='an' or x=='of' or x=='and':
                del x
            else:
                if str:
                    str=str +' ' + x
                else:
                    str = x
        return str
    
    def op(self):
        self.Q.getip(self.ip)
        self.Q.ranksall()
        self.Q.sortall()
        if self.flag:
            print('Did you mean'+'\n\n')
        output=[]
        for deq in range(self.Q.size):
            ans_key=self.Q.dequeue()
            ans_val=self.final[ans_key]
            #here check for match and print in color or bold
            output.append(ans_key + '-' + ans_val)
        return output
        


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
        self.lstring=['amrita','sports','arts','technology','food','music','socialmedia','entertainment']

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
                                
                            l=self.advanced()
                        
                    #about
                        elif self.textpos.collidepoint((x,y)) and self.frame==0 and self.about==0 and (self.i==1 or self.i==2):
                            self.background.fill((245,235,245))
                            font=pygame.font.SysFont('High Tower Text',48)
                            abt=font.render("Designed By,",1,(0,0,0))
                            abtpos=abt.get_rect()
                            abtpos.left=100
                            abtpos.top=100
                            i1=pygame.image.load('murthy.png')
                            font=pygame.font.SysFont('Times New Roman',40)
                            font.set_underline(1)
                            i1=self.background.blit(i1,(abtpos.left+100,abtpos.bottom+100))
                            n1=font.render("K S Murthy",1,(133,133,133))
                            n1pos=n1.get_rect()
                            n1pos.centerx=i1.centerx
                            n1pos.top=i1.bottom+10
                            self.background.blit(n1,n1pos)
                            i2=pygame.image.load('dheeraj.jpg')
                            i2=self.background.blit(i2,(i1.left+350,i1.top))
                            n2=font.render("|)H££®@J",1,(163,73,164))
                            n2pos=n2.get_rect()
                            n2pos.centerx=i2.centerx
                            n2pos.top=i2.bottom+10
                            self.background.blit(n2,n2pos)
                            i3=pygame.image.load('tarun.jpg')
                            i3=self.background.blit(i3,(i2.left+350,i1.top))
                            n3=font.render("M N S S Tarun",1,(255,64,69))
                            n3pos=n3.get_rect()
                            n3pos.centerx=i3.centerx
                            n3pos.top=i3.bottom+10
                            self.background.blit(n3,n3pos)
                            self.background.blit(abt,abtpos)
                            self.frame=1
                            self.i=3
                            font.set_underline(0)
                                                   
                            lp=1
                            font=pygame.font.SysFont('High Tower Text',30)
                            n1=font.render("UI Designer",1,(133,133,133))
                            n2=font.render("Architect & Coder",1,(163,73,164))
                            n3=font.render("Data Organiser",1,(255,64,69))
                            self.background.blit(n1,n1pos.move(20,45))
                            self.background.blit(n2,n1pos.move(330,45))
                            self.background.blit(n3,n1pos.move(715,45))
                            abt=font.render("03-05-2015",1,(0,0,0))
                            abtpos=abt.get_rect()
                            abtpos.bottom=768
                            abtpos.right=1366
                            self.background.blit(abt,abtpos)
                            self.screen.blit(self.background,(0,0))
                            pygame.display.flip()
                                    
                            while lp==1:
                                for event in pygame.event.get():
                                    if event.type==MOUSEBUTTONDOWN:
                                        (x,y)=pygame.mouse.get_pos()
                                        if n1pos.collidepoint((x,y)) or i1.collidepoint((x,y)):
                                            webbrowser.open('https://www.facebook.com/murthy.kuppa.5')
                                        elif n2pos.collidepoint((x,y)) or i2.collidepoint((x,y)):
                                            webbrowser.open('https://www.facebook.com/dheeraj.ronaldo.7?fref=ts')
                                        elif n3pos.collidepoint((x,y)) or i3.collidepoint((x,y)):
                                            webbrowser.open('https://www.facebook.com/saitarun.malladi?fref=ts')

                                    elif event.type==KEYDOWN and event.key==K_HOME:
                                        lp=0

                                    elif event.type==KEYDOWN and event.key==K_ESCAPE:
                                        pygame.quit()
                                        sys.exit()

                            e=ds()
                            self=e
                            self.firstpage()

                            

                    if self.abit==1:
                        for z in range(len(l)):
                            if l[z].collidepoint((x,y)):
                                self.categ=self.lstring[z]
                                pygame.draw.rect(self.background,(0,0,0),l[z],2)
                                self.abit=0
                                break
                    if self.back==1:
                        if bbox.collidepoint((x,y)):
                            if self.stacking.isEmpty():
                                d=ds()
                                self=d
                                self.firstpage()
                            else:
                                self.b=self.stacking.pop()
                                font=pygame.font.SysFont('Times New Roman',40)
                                pygame.draw.rect(self.background,(255,255,255),self.box)
                                s=font.render(self.b,1,(0,0,0))
                                self.background.blit(s,self.spos)
                                #print self.b
                                webl=searchprint(self)
                    if self.searc>0:
                        for z in range(len(webl[0])):
                            if webl[0][z].collidepoint(pygame.mouse.get_pos()):
                                webbrowser.open(webl[1][z])
                elif event.type==KEYDOWN and self.i==2:
                    self.count+=1
                    if event.key==K_RETURN and self.b!='':
                        self.stacking.push(self.b)
                        #print self.b
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
                    elif event.key==K_KP_DIVIDE:
                        self.b=self.b+'/'
                    elif event.key==K_KP_MULTIPLY:
                        self.b=self.b+'*'
                    elif event.key==K_KP_MINUS:
                        self.b=self.b+'-'
                    elif event.key==K_KP_PLUS:
                        self.b=self.b+'+'
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
    print s.b
    webl=[[],[]]
    alpha=pygame.Rect(100,200,600,25)
    font=pygame.font.SysFont('Times New Roman',20)
    pos=pygame.Rect(s.box.right+5,s.box.top,500,50)
    pygame.draw.rect(s.background,(236,248,241),pos)
    if s.categ:
        print s.categ
        f=s.categ+'_Tree.pkl'
        s.categ=''
        #advanced search
        print f
        F=finalop(s.b,f)
    else:
        F=finalop(s.b,'Data_Tree.pkl')

    opflag=F.callfilterkey()
    if opflag:
        if isinstance(opflag,int) or isinstance(opflag,float):
                font=pygame.font.SysFont('Times New Roman',40)
                data=font.render(str(opflag),1,(0,0,0))
                pygame.draw.rect(s.background,(236,248,241),pos)
                s.background.blit(data,pos)
        else:
            output=F.op()
            if output:
                for vals in output:
                    valsplit=vals.split('-')
                    #print (valsplit[0]+'^'+valsplit[1])
                    pygame.draw.rect(s.background,(236,248,241),alpha)
                    data=font.render(valsplit[0],1,(0,0,0))
                    pygame.draw.rect(s.background,(236,248,241),pygame.Rect(alpha.left,alpha.top,1200,600))
                    font.set_underline(1)
                    website=font.render(valsplit[1],1,(14,28,201))
                    font.set_underline(0)
                    webpos=website.get_rect()
                    webpos.left=alpha.right+10
                    webpos.top=alpha.top
                    s.background.blit(website,webpos)
                    s.background.blit(data,alpha)
                    pygame.draw.rect(s.background,(236,248,241),pos)
                    alpha=alpha.move(0,27)
                    webl[0].append(webpos)
                    webl[1].append(valsplit[1])
                
            #webl=[webpos,webpos.move(0,-27),webpos.move(0,-54),webpos.move(0,-81)]
            
    else:
        print 'value not found'
        pygame.draw.rect(s.background,(236,248,241),pygame.Rect(alpha.left,alpha.top,1200,500))
        data=font.render("Search not found",1,(0,0,0))
        s.background.blit(data,alpha)

    return webl
    #font=pygame.font.SysFont('Times New Roman',20)
    #data=font.render("Facebook",1,(0,0,0))
    #datapos=data.get_rect()
    #website=font.render("www.facebook.com",1,(0,0,0))
    #webpos=website.get_rect()
    #datapos=datapos.move(100,300)
    #alpha=pygame.Rect(datapos.left,datapos.top,600,20)
    #for w in range(4):
        #pygame.draw.rect(s.background,(255,255,255),alpha)
        #data=font.render("Facebook",1,(0,0,0))
        #website=font.render("www.facebook.com",1,(0,0,0))
        #webpos.left=alpha.right+10
        #webpos.top=alpha.top
        #s.background.blit(website,webpos)
        #s.background.blit(data,datapos)
        #datapos=datapos.move(0,27)
        #alpha=alpha.move(0,27)

    
    




S=ds()
S.main()

        



'''Q=PriorityQueue()
Enc=encode()
F=finalop()
F.callfilterkey(F.ip)
F.op()'''
