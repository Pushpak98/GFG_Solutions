for _ in range(int(input())):
    a=int(input())
    i=1
    b=[]
    while(i<a):
        if a%i==0:
            b.append(i)
        i+=1
    if sum(b)==a:
        print(1)
    else:
        print(0)

            