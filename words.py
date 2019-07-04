from visual import print_tex

def strtoint(v):
        x=v.split(' ')
        for i in range(len(x)):
                x[i]=int(x[i])
        return x




def parse_word(v):
        List=strtoint(v)
        Z=[]
        M=[]
        for j in List:
                Z.append(list())
        k = 0
        Z[0].append(List[0])
        for i in range(len(List)-1):
                if List[i]<=List[i+1]:
                        Z[k].append(List[i+1])
                else:
                        k += 1
                        Z[k].append(List[i+1])
        for i in range(len(Z)):
                if  len(Z[i])!=0:
                        M.append(Z[i])        
        for i in range(len(M)-1):
                for j in range(len(M[i])-1):
                        if M[i][j]<=M[i][j+1] and  M[i][j]>M[i+1][j]:
                                        return M
                        elif M[i][j]>M[i][j+1]:
                                raise  Exception('no young tableau')
                        elif M[i][j] not in P:
                                raise  Exception('no young tableau')
                        else:
                                raise  Exception('no young tableau')
        return M

