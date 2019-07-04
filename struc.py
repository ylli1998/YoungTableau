from ytmath import *
from visual import print_tex
from words import *

class youngtableau():
    def __init__(self,word):
        self.lists=parse_word(word)


    def visual(self,boxlength,filename):
        print_tex(self.lists  ,boxlength, filename)
        with open(filename,"r+") as Datei:
            f=Datei.readlines()
            Datei.close()

    def word(self):
        L=[]
        for i in range(len(self.lists)):
            for j in range(len(self.lists[i])):
                L.append(str(self.lists[i][j]))
        L=" ".join(L)
        return word(L)

    def row_insert(self, x):
        return row_insert(self,x)

class word():
    def __init__(self,v):
        self.list=strtoint(v)

    def youngtableau(self):
        YT=youngtableau(str(self.list[0]))
        L=[]
        for i in range(1,len(self.list)):
            YT = YT.row_insert(self.list[i])
        return YT

def mult_classes(word1,word2):
    W=word1 +" "+word2
    return word(W)

def are_equiv(word1,word2):
    W=word1.youngtableau()
    V=word2.youngtableau()
    if V.lists==W.lists :
        return True
    if V.lists !=W.lists:
        return False



def create_from(row, file):
    with open(file,'r+') as Datei:
        mylist=Datei.read().splitlines()
        S=mylist[row].replace('"', "")
        return youngtableau(str(S))
""" from the file struc.py you can call any function you would like be it in ytmath , visual or words .
create from creates a young tableau from a row of a .txt file .
visual , creates a .tex file with a youngtableau in in , are equiv tests if two given words are equivalent to each other and everything 
else is very self explainatory."""
