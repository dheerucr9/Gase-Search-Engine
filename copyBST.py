import pickle

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


Tree = BinarySearchTree()

class encode:
        
    def enc(self,ip):
        self.val=0
        temp = 0
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


E=encode()

fp=open('final_data.txt','r+')

def initializer():
    temp_flag = 0
    temp_en_val = None
    temp_count = 0
    temp_array = [None]*100
    temp_data = None
    temp_website = None
    temp_op = []
    for line in fp.readlines():                 #reading line by line
        line=line.rstrip('\n')                  #removing the newline
        if line == '#' :
            if temp_count == 0 :                #to check for a new start
                temp_flag = 1
            else :
                temp_dict = {}                  #create a new dictionary
                for i in range(temp_count):     #at the start of new keyword make the dictinary for the keyword
                    temp_op = temp_array[i].split('^')
                    temp_data = temp_op[0]
                    temp_website = temp_op[1]
                    temp_dict[temp_data] = temp_website
                Tree.put(temp_en_val,temp_dict)     #enter the data and encoded keyword into the BST
                temp_count = 0
                temp_flag = 1
                del temp_dict                   #delete the temporary dictionary
                
        else:
            if temp_flag == 1 :                 #encoding the keyword
                temp_en_val = E.enc(line)
                temp_flag = 0
            elif temp_flag == 0:
                temp_array[temp_count] = line   #values for the keyword stored in a temporary array
                temp_count+=1
    with open('Data_Tree.pkl','wb') as output:          #write the BST object created into a file
        pickle.dump(Tree,output,pickle.HIGHEST_PROTOCOL)


initializer()
