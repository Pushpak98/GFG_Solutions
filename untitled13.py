
i=1
b=[]
for _ in range(int(input())):
    a=int(input())
    n=int(input())
    
    while(i<a):
        if a%i==0:
           b=i      
        i+=1
    print(b)

    while(i<n):
        if n%i==0:
           c=i      
        i+=1
    print(c)
         
            
    