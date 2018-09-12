#统计每个方向上的棋子数量　和　阻塞情况
def shang(l,i,j,sign):
    s = []
    count = 0
    x = 3
    while 1:
        if i - 1 >= 0:
            i -= 1
            if l[i][j] = sign:
                count += 1
            else:
                x = l[i][j]
                break
        else:
            break
    s = [count,x]
    return s 
def xia(l,i,j,sign):
    s = []
    count = 0
    x = 3 
    while 1:
        if i + 1 <= 14:
            i += 1
            if l[i][j] = sign:
                count += 1
            else:
                x = l[i][j]
                break
        else:
            break
    s = [count,x]
    return s 
def zuo(l,i,j,sign):
    s = []
    count = 0
    x = 3
    while 1:
        if j - 1 >= 0:
            j -= 1
            if l[i][j] == sign:
                count += 1
            else:
                x = l[i][j]
                break
        else:
            break 
    s = [count,x]
    return s 
def you(l,i,j,sign):
    s = []
    count = 0
    x = 3
    while 1:
        if j + 1 <= 14:
            j += 1
            if l[i][j] == sign:
                count += 1
            else:
                x = l[i][j] 
                break
        else:
            break
    s = [count,x]
    return s 
def zuoshang(l,i,j,sign):
    s = []
    count = 0
    x = 3
    while 1:
        if i - 1 >= 0 and j + 1 <= 14:
            i -= 1
            j += 1
            if l[i][j] == sign:
                count += 1
            else:
                x = l[i][j]
        else:
            break
    s = [count,x]
    return s 
def zuoxia(l,i,j,sign):
    s = []
    count = 0
    x = 3
    while 1:
        if i + 1 <= 14 and j - 1 >= 0:
            i += 1
            j -= 1
            if l[i][j] == sign:
                count += 1
            else:
                x = l[i][j]
        else:
            break
    s = [count,x]
    return s 
def youshang(l,i,j,sign):
    s = []
    count = 0
    x = 3
    while 1:
        if i - 1 >= 0 and j - 1 >= 0:
            i -= 1
            j -= 1
            if l[i][j] == sign:
                count += 1
            else:
                x = l[i][j]
        else:
            break
    s = [count,x]
    return s 
def youxia(l,i,j,sign):
    s = []
    count = 0
    x = 3
    while 1:
        if i + 1 <= 14 and j + 1 <= 14:
            i += 1
            j += 1
            if l[i][j] == sign:
                count += 1
            else:
                x = l[i][j]
                break
        else:
            break
    s = [count,x]
    return s 
#求出　横　shu zuoxie  youxie  的　棋子数量
def scount(l,sign):
    L = {}
    for i in range(15):
        for j in range(15):
            if l[i][j] == 0:
                cshu = shang(l,i,j,sign) + xia(l,i,j,sign)
                crow = zuo(l,i,j,sign) + you(l,i,j,sign)
                zxie = zuoshang(l,i,j,sign) + zuoxia(l,i,j,sign)
                yxie = youshang(l,i,j,sign) + youxia(l,i,j,sign)
                L[(i,j)] = [crow,cshu,zxie,yxie]
    return L
def position(l):
    S = {}
    s1 = scount(l,1)
    s2 = scount(l,2)
    for i in range(15):
        for i in range(15):
            if l[i][j] == 0:
                score = 0
                n1 = 0
                n2 = 0
                #白
                c1 = 1
                c2 = 1
                for k in s2[(i,j)]:
                    #五个棋子以上
                    if k[0]+k[2]+1>=5:
                        score+=1000000
                    #四个棋子
                    if k[0]+k[2]+1==4:
                        #活四
                        if k[1]==0 and k[3]==0:
                            score+=500000
                        if k[1]==0 and k[3]!=0:
                            n2 += 1
                        if k[1]!=0 and k[3]==0:
                            n2+=1
                    #三个棋子
                    if k[0]+k[2]+1==3:
                        #或三
                        if k[1]==0 and k[3]==0:
                            score+=50000
                    #两个棋子
                    if k[0]+k[2]+1==2:
                        #活儿
                        if k[1]==0 and k[3]==0:
                            score+=500
                            if c2==1:
                                if k[0]==1:
                                    if j-4>=0 and l[i][j-4]==0 and l[i][j-3]==2 :
                                        score+=60000
                                        n2+=1
                                    if j+3<=14 and l[i][j+3]==0 and l[i][j+2]==2:
                                        score+=60000
                                        n2+=1
                                if k[2]==1:
                                    if j+4<=14 and l[i][j+4]==0 and l[i][j+3]==2:
                                        score+=60000
                                        n2+=1
                                    if j-3>=0 and l[i][j-3]==0 and l[i][j-2]==2:
                                        score+=60000
                                        n2+=1
                            if c2==2:
                                if k[0]==1:
                                    if i-4>=0 and l[i-4][j]==0 and l[i-3][j]==2:
                                        score+=60000
                                        n2+=1
                                    if i+3<=14 and l[i+3][j]==0 and l[i+2][j]==2:
                                        score+=60000
                                        n2+=1
                                if k[2]==1:
                                    if i+4<=14 and l[i+4][j]==0 and l[i+3][j]==2:
                                        score+=60000
                                        n2+=1
                                    if i-3>=0 and l[i-3][j]==0 and l[i-2][j]==2:
                                        score++60000
                                        n2+=1
                            if c2==3:
                                if k[0]==1:
                                    if i-4>=0 and j+4<=14 and l[i-4][j+4]==0 and l[i-3][j+3]==2:
                                        score+=60000
                                        n2+=1
                                    if i+3<=14 and j-3>=0 and l[i+3][j-3]==0 and l[i+2][j-2]==2:
                                        score+=60000
                                        n2+=1

                                if k[2]==1:
                                    if i+4<=14 and j-4>=0 and l[i+4][j-4]==0 and l[i+3][j-3]==2:
                                        score+=60000
                                        n2+=1
                            if c2==4: 
                                if k[0]==1:
                                    if i-4>=0 and j-4>=0 and l[i-4][j-4]==0 and l[i-3][j-3]==2:
                                        score+=60000
                                        n2+=1
                                    if i+3<=14 and j+3<=14 and l[i+3][j+3]==0 and l[i+2][j+2]==2:
                                        score+=60000
                                        n2+=1
                                if k[2]==1:
                                    if i+4<=14 and j+4<=14 and l[i+4][j+4]==0 and l[i+3][j+3]==2:
                                        socre+=60000
                                        n2+=1

                                    if i-3>=0 and j-3>=0 and l[i-3][j-3]==0 and l[i-2][j-2]==2:
                                        score+=60000
                                        n2+=1
                    if k[0]+k[2]==0 and k[1]==0 and k[3]==0:
                        # if l[7][7]==0:

                        if c2==1:
                            if j+4<=14 and l[i][j+4]==0 and l[i][j+3]==2 and l[i][j+2]==2:
                                score+=60000
                                n2+=1
                            if j-4>=0 and l[i][j-4]==0 and l[i][j-3]==2 and l[i][j-2]==2:
                                score+=60000
                                n2+=1
                        if c2==2:
                            if i-4>=0 and l[i-4][j]==0 and l[i-3][j]==2 and l[i-2][j]==2:
                                score+=60000
                                n2+=1
                            if i+4<=14 and l[i+4][j]==0 and l[i+3][j]==2 and l[i+2][j]==2:
                                score+=60000
                                n2+=1
                        if c2==3:
                            if i-4>=0 and j+4<=14 and l[i-4][j+4]==0 and l[i-3][j+3]==2 and l[i-2][j+2]==2:
                                score+=60000
                                n2+=1
                            if i+4<=14 and j-4>=0 and l[i+4][j-4]==0 and l[i+3][j-3]==2 and l[i+2][j-2]==2:
                                score+=60000
                                n2+=1
                        if c2==4:
                            if i+4<=14 and j+4<=14 and l[i+4][j+4]==0 and l[i+3][j+3]==2 and l[i+2][j+2]==2:
                                score+=60000
                                n2+=1
                            if i-4>=0 and j-4>=0 and l[i-4][j-4]==0 and l[i-3][j-3]==2 and l[i-2][j-2]==2:
                                score+=60000
                                n2+=1
                    c2+=1
                for k in s1[(i,j)]:
                    #五个棋子以上
                    if k[0]+k[2]+1>=5:
                        score+=800000
                    #四个棋子
                    if k[0]+k[2]+1==4:
                        #活四
                        if k[1]==0 and k[3]==0:
                            score+=400000
                        if k[1]==0 and k[3]!=0:
                            n1 += 1
                        if k[1]!=0 and k[3]==0:
                            n1+=1
                    #三个棋子
                    if k[0]+k[2]+1==3:
                        #或三
                        if k[1]==0 and k[3]==0:
                            n1+=1
                    #两个棋子
                    if k[0]+k[2]+1==2:
                        #活儿
                        if k[1]==0 and k[3]==0:
                            score+=400
                            if c1==1:
                                if k[0]==1:
                                    if j-4>=0 and l[i][j-4]==0 and l[i][j-3]==1 :
                                      
                                        n1+=1
                                    if j+3<=14 and l[i][j+3]==0 and l[i][j+2]==1:
                                    
                                        n1+=1
                                if k[2]==1:
                                    if j+4<=14 and l[i][j+4]==0 and l[i][j+3]==1:
                                    
                                        n1+=1
                                    if j-3>=0 and l[i][j-3]==0 and l[i][j-2]==1:
                                  
                                        n1+=1
                            if c1==2:
                                if k[0]==1:
                                    if i-4>=0 and l[i-4][j]==0 and l[i-3][j]==1:
                                    
                                        n1+=1
                                    if i+3<=14 and l[i+3][j]==0 and l[i+2][j]==1:
                                     
                                        n1+=1
                                if k[2]==1:
                                    if i+4<=14 and l[i+4][j]==0 and l[i+3][j]==1:
                                     
                                        n1+=1
                                    if i-3>=0 and l[i-3][j]==0 and l[i-2][j]==1:
                                     
                                        n1+=1
                            if c1==3:
                                if k[0]==1:
                                    if i-4>=0 and j+4<=14 and l[i-4][j+4]==0 and l[i-3][j+3]==1:
                                   
                                        n2+=1
                                    if i+3<=14 and j-3>=0 and l[i+3][j-3]==0 and l[i+2][j-2]==1:
                                    
                                        n1+=1

                                if k[2]==1:
                                    if i+4<=14 and j-4>=0 and l[i+4][j-4]==0 and l[i+3][j-3]==1:
                                     
                                        n1+=1
                            if c1==4: 
                                if k[0]==1:
                                    if i-4>=0 and j-4>=0 and l[i-4][j-4]==0 and l[i-3][j-3]==1:
                                    
                                        n1+=1
                                    if i+3<=14 and j+3<=14 and l[i+3][j+3]==0 and l[i+2][j+2]==1:
                                      
                                        n1+=1
                                if k[2]==1:
                                    if i+4<=14 and j+4<=14 and l[i+4][j+4]==0 and l[i+3][j+3]==1:
                                      
                                        n1+=1

                                    if i-3>=0 and j-3>=0 and l[i-3][j-3]==0 and l[i-2][j-2]==1:
                                    
                                        n1+=1
                    if k[0]+k[2]==0 and k[1]==0 and k[3]==0:
                        # if l[7][7]==0:

                        if c1==1:
                            if j+4<=14 and l[i][j+4]==0 and l[i][j+3]==1 and l[i][j+2]==1:
                              
                                n1+=1
                            if j-4>=0 and l[i][j-4]==0 and l[i][j-3]==1 and l[i][j-2]==1:
                            
                                n1+=1
                        if c1==2:
                            if i-4>=0 and l[i-4][j]==0 and l[i-3][j]==1 and l[i-2][j]==1:
                            
                                n1+=1
                            if i+4<=14 and l[i+4][j]==0 and l[i+3][j]==1 and l[i+2][j]==1:
                            
                                n1+=1
                        if c2==3:
                            if i-4>=0 and j+4<=14 and l[i-4][j+4]==0 and l[i-3][j+3]==1 and l[i-2][j+2]==1:

                                n1+=1
                            if i+4<=14 and j-4>=0 and l[i+4][j-4]==0 and l[i+3][j-3]==1 and l[i+2][j-2]==1:

                                n1+=1
                        if c2==4:
                            if i+4<=14 and j+4<=14 and l[i+4][j+4]==0 and l[i+3][j+3]==1 and l[i+2][j+2]==1:

                                n1+=1
                            if i-4>=0 and j-4>=0 and l[i-4][j-4]==0 and l[i-3][j-3]==1 and l[i-2][j-2]==1:

                                n1+=1
                

                    if w>=2:
                        score2+=8000

                
                S[(i,j)] = score1+score2
    s = sorted(S.items(),key = lambda x:x[1],reverse = True)
    print(s)
    score1 = S[s[0][0]]
    

    

    position1 = s[0][0]
    return position1
