

for _ in range(int(input())):
     m=int(input())
     for i in range(m):
         if m%i==0:
             break
     if 
     print()












    a=[]
    m=int(input())
    while(m>=4):
        b=[]
        for i in range(1,m+1):
            if m%i==0:
                b.append(i)
        #print(b)
        if len(b)==3:
           a.append(m)    
           #print(a)
        m-=1
    print(len(a))                        
