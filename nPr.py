import math

for _ in range(int(input())):
    a=list(map(int, input().split()))
    k=math.factorial(a[0])/(math.factorial(abs(a[1]-a[0])))
    #l=k/math.factorial(a[1])
    l=k/math.factorial(a[1])
    print(int(l))
    