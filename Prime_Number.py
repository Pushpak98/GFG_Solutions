

for _ in range(int(input())):
    m=int(input())
    count=0
    for i in range(2,range(3,m)):
        if m%i==0: 
            count+=1
    if count>0:
        print('No')
    else:
        print('Yes')
        
        
        
        