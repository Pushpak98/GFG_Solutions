for _ in range(int(input())):
    h,m=map(int,input().split())
    
    for j in range(1,m+1):
        j*=6
    print(j)
    for i in range(1,h+1):
        i*=30
    print(i)

print(j-i)

    