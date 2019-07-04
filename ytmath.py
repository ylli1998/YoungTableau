from words import strtoint
import struc

def K1(v,index):
	word=strtoint(v)
	b=len(word)
	if index+3>b:
		raise ValueError("K2 Operation impossible")
	if word[index+2]<word[index]<=word[index+1]:
		word[index],word[index+1],word[index+2]=word[index],word[index+2],word[index+1]
		return word
	else :
		raise ValueError("K1 Operation impossible")
def K1_inv(v,index):
	word=strtoint(v)
	b=len(word)
	if index+3>b:
		raise ValueError("K1_inv Operation impossible")
	if word[index+1]<word[index]<=word[index+2]:
		word[index],word[index+1],word[index+2]=word[index],word[index+2],word[index+1]
		return word
	else :
		raise ValueError("K1_inv Operation impossible")

def K2(v,index):
	word=strtoint(v)
	b=len(word)
	if index+3>b:
		raise ValueError("K2 Operation impossible")
	if word[index]<=word[index+2]<word[index+1]:
		word[index],word[index+1],word[index+2]=word[index+1],word[index],word[index+2]
		return word
	else :
		raise ValueError("K2 Operation impossible")
def K2_inv(v,index):
	word=strtoint(v)
	b=len(word)
	if index+3>b:
		raise ValueError("K2_inv Operation impossible")
	if word[index+1]<=word[index+2]<word[index]:
		word[index],word[index+1],word[index+2]=word[index+1],word[index],word[index+2]
		return word
	else :
		raise ValueError("K2_inv Operation impossible")


def multiply(S,T):
    w = T.word()
    w.list.reverse()
    
    for i in range(len(w.list)):
        S.row_insert(w.list[i])
    return S


def row_insert(S,x):
    C=[[0]]
    for lists in S.lists:
        C.append(lists)
    C.reverse()
    A=row_insert2(C[0],x)
    if x>=C[0][-1]:
        C.pop(-1)
        return struc.youngtableau(string_from_list(C))
    else :
        for i in range(1,len(A)):
            if A[i]>x:
                x=A.pop(i)
                break
        for i in range(1,len(C)):
            row_insert2(C[i],x)
            if x==C[i][-1]:
                break
            else :
                for j in range(len(C[i])):
                    if C[i][j]>x:
                        x=C[i].pop(j)
                        break
        C[-1].pop(0)
        for i in range(len(C)):
            if C[i]==[]:
                C.pop(i)
        print(C)
        return struc.youngtableau(string_from_list(C))

def string_from_list(L):
    wort = ""
    L.reverse()
    for i in range(len(L)):
        for j in range(len(L[i])):
            wort += str(L[i][j])+ " "
    return wort[:len(wort)-1]


def row_insert2(L,x):
	if x>=L[-1]:
		L.append(x)
		return L
	for i in range(len(L)):
		if L[i]>x:
			L.insert(i,x)
			return L



