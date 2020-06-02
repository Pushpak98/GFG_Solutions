
for _ in range(int(input())):
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    if (b[3]>a[1] or a[3]>b[1] or b[0]>a[2] or a[0]>b[2]):
        print(0)
    else:
        print(1)        


  