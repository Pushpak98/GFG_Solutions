for _ in range(int(input())):
    k=[]
    m=int(input())
    while(m>2):
        for i in range(2,m):        
            if m%i==0:
                break
        else:
            k.append(m)
        m-=1
    k.append(2) 
    k.sort()
    print(sum(k))
    
    
    