import math
for _ in range(int(input())):
    h,m=input().split()
    k=float(m)/60
    h=float(h)+k
    a=float(m)*6-(h)*30
    a=abs(a)
    if a>180: 
       a=360-a
       print(math.floor(a))
    else:
        print(math.floor(a))
        
        
    