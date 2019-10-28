#for dictionary


import pickle


fp=open('ip.txt','r+')

class dictionary:
    def __init__(self):
        self.main=[dict() for x in range(26)]
        self.makedict()

    def makedict(self):
        for lines in fp.readlines():
            splitlines=lines.rstrip('\n')
            temp=splitlines.split('^')
            if temp[0][0].lower()=='a':
                self.main[0][temp[0]]=temp[1]
            elif temp[0][0].lower()=='b':
                self.main[1][temp[0]]=temp[1]
            elif temp[0][0].lower()=='c':
                self.main[2][temp[0]]=temp[1]
            elif temp[0][0].lower()=='d':
                self.main[3][temp[0]]=temp[1]
            elif temp[0][0].lower()=='e':
                self.main[4][temp[0]]=temp[1]
            elif temp[0][0].lower()=='f':
                self.main[5][temp[0]]=temp[1]
            elif temp[0][0].lower()=='g':
                self.main[6][temp[0]]=temp[1]
            elif temp[0][0].lower()=='h':
                self.main[7][temp[0]]=temp[1]
            elif temp[0][0].lower()=='i':
                self.main[8][temp[0]]=temp[1]
            elif temp[0][0].lower()=='j':
                self.main[9][temp[0]]=temp[1]
            elif temp[0][0].lower()=='k':
                self.main[10][temp[0]]=temp[1]
            elif temp[0][0].lower()=='l':
                self.main[11][temp[0]]=temp[1]
            elif temp[0][0].lower()=='n':
                self.main[12][temp[0]]=temp[1]
            elif temp[0][0].lower()=='o':
                self.main[13][temp[0]]=temp[1]
            elif temp[0][0].lower()=='p':
                self.main[14][temp[0]]=temp[1]
            elif temp[0][0].lower()=='q':
                self.main[15][temp[0]]=temp[1]
            elif temp[0][0].lower()=='r':
                self.main[16][temp[0]]=temp[1]
            elif temp[0][0].lower()=='s':
                self.main[17][temp[0]]=temp[1]
            elif temp[0][0].lower()=='t':
                self.main[18][temp[0]]=temp[1]
            elif temp[0][0].lower()=='u':
                self.main[19][temp[0]]=temp[1]
            elif temp[0][0].lower()=='v':
                self.main[20][temp[0]]=temp[1]
            elif temp[0][0].lower()=='w':
                self.main[21][temp[0]]=temp[1]
            elif temp[0][0].lower()=='x':
                self.main[22][temp[0]]=temp[1]
            elif temp[0][0].lower()=='x':
                self.main[23][temp[0]]=temp[1]
            elif temp[0][0].lower()=='y':
                self.main[24][temp[0]]=temp[1]
            elif temp[0][0].lower()=='z':
                self.main[25][temp[0]]=temp[1]
            

        with open('Dict_data','wb') as output:         
            pickle.dump(self.main,output,pickle.HIGHEST_PROTOCOL)

D=dictionary()

            
