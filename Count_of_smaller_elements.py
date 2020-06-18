
for _ in range(int(input())):
    count=0
    x=int(input())
    a=list(map(int,input().split()))
    y=int(input())
    for i in range(len(a)):
        if a[i]<=y:
            count+=1
    print(count)
        