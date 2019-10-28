class stack:
    def __init__(self):
        self.s=[]
    def isempty(self):
        return len(self.s)==0
    def push(self,a):
        self.s.append(a)
    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            return self.s.pop()
    def top(self):
        if self.isempty():
            print("Stack is empty")
        else:
            return self.s[-1]


#Main


a=stack()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
