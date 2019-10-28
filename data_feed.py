fp1=open('data.txt','r+')


fp2=open('final_data.txt','w+')

#array of a dictionary of a dictionary


class arrdict:
    def __init__(self):
        self.main=[dict() for x in range(26)]  
        self.available=[]

    def goal(self):
        for lines in fp1.readlines():
            splitlines=lines.rstrip('\n')
            temp=splitlines.split('^')
            new=self.trim(temp[0]).lower()
            for words in new.split():          
                if words not in self.available:
                    if words[0].lower()=='a':
                        self.main[0][words]={}
                        self.main[0][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='b':
                        self.main[1][words]={}
                        self.main[1][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='c':
                        self.main[2][words]={}
                        self.main[2][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='d':
                        self.main[3][words]={}
                        self.main[3][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='e':
                        self.main[4][words]={}
                        self.main[4][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='f':
                        self.main[5][words]={}
                        self.main[5][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='g':
                        self.main[6][words]={}
                        self.main[6][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='h':
                        self.main[7][words]={}
                        self.main[7][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='i':
                        self.main[8][words]={}
                        self.main[8][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='j':
                        self.main[9][words]={}
                        self.main[9][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='k':
                        self.main[10][words]={}
                        self.main[10][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='l':
                        self.main[11][words]={}
                        self.main[11][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='m':
                        self.main[12][words]={}
                        self.main[12][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='n':
                        self.main[13][words]={}
                        self.main[13][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='o':
                        self.main[14][words]={}
                        self.main[14][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='p':
                        self.main[15][words]={}
                        self.main[15][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='q':
                        self.main[16][words]={}
                        self.main[16][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='r':
                        self.main[17][words]={}
                        self.main[17][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='s':
                        self.main[18][words]={}
                        self.main[18][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='t':
                        self.main[19][words]={}
                        self.main[19][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='u':
                        self.main[20][words]={}
                        self.main[20][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='v':
                        self.main[21][words]={}
                        self.main[21][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='w':
                        self.main[22][words]={}
                        self.main[22][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='x':
                        self.main[23][words]={}
                        self.main[23][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='y':
                        self.main[24][words]={}
                        self.main[24][words][temp[0]]=temp[1]
                        self.available.append(words)
                    elif words[0].lower()=='z':
                        self.main[25][words]={}
                        self.main[25][words][temp[0]]=temp[1]
                        self.available.append(words)
                else:
                    if words[0].lower()=='a':
                        self.main[0][words][temp[0]]=temp[1]
                    elif words[0].lower()=='b':
                        self.main[1][words][temp[0]]=temp[1]
                    elif words[0].lower()=='c':
                        self.main[2][words][temp[0]]=temp[1]
                    elif words[0].lower()=='d':
                        self.main[3][words][temp[0]]=temp[1]
                    elif words[0].lower()=='e':
                        self.main[4][words][temp[0]]=temp[1]
                    elif words[0].lower()=='f':
                        self.main[5][words][temp[0]]=temp[1]
                    elif words[0].lower()=='g':
                        self.main[6][words][temp[0]]=temp[1]
                    elif words[0].lower()=='h':
                        self.main[7][words][temp[0]]=temp[1]
                    elif words[0].lower()=='i':
                        self.main[8][words][temp[0]]=temp[1]
                    elif words[0].lower()=='j':
                        self.main[9][words][temp[0]]=temp[1]
                    elif words[0].lower()=='k':
                        self.main[10][words][temp[0]]=temp[1]
                    elif words[0].lower()=='l':
                        self.main[11][words][temp[0]]=temp[1]
                    elif words[0].lower()=='m':
                        self.main[12][words][temp[0]]=temp[1]
                    elif words[0].lower()=='n':
                        self.main[13][words][temp[0]]=temp[1]
                    elif words[0].lower()=='o':
                        self.main[14][words][temp[0]]=temp[1]
                    elif words[0].lower()=='p':
                        self.main[15][words][temp[0]]=temp[1]
                    elif words[0].lower()=='q':
                        self.main[16][words][temp[0]]=temp[1]
                    elif words[0].lower()=='r':
                        self.main[17][words][temp[0]]=temp[1]
                    elif words[0].lower()=='s':
                        self.main[18][words][temp[0]]=temp[1]
                    elif words[0].lower()=='t':
                        self.main[19][words][temp[0]]=temp[1]
                    elif words[0].lower()=='u':
                        self.main[20][words][temp[0]]=temp[1]
                    elif words[0].lower()=='v':
                        self.main[21][words][temp[0]]=temp[1]
                    elif words[0].lower()=='w':
                        self.main[22][words][temp[0]]=temp[1]
                    elif words[0].lower()=='x':
                        self.main[23][words][temp[0]]=temp[1]
                    elif words[0].lower()=='y':
                        self.main[24][words][temp[0]]=temp[1]
                    elif words[0].lower()=='z':
                        self.main[25][words][temp[0]]=temp[1]


        
    def trim(self,a):
        str=''
        for x in a.split():
            y = x.lower()
            if y=='i' or y=='a' or y=='an' or y=='is' or y=='of' or y=='am' or y=='the' or y=='hi' or y=='hello' or y=='why' or y=='when' or y=='where' or y=='whose' or y=='he' or y=='she' or y=='not' or y=='was' or y=='and':
                del x
            else:
                if str:
                    str=str +' ' + x
                else:
                    str = x
        return str

    def save_data(self):
        fp2.write('#\n')
        for x in range(26):
            if self.main[x]:
                for vals in self.main[x]:
                    fp2.write(vals)
                    fp2.write('\n')
                    for subs in self.main[x][vals]:
                        fp2.write(subs+'^'+self.main[x][vals][subs])
                        fp2.write('\n')
                    fp2.write('#\n')
        fp2.close()
                
A=arrdict()
A.goal()
A.save_data()
