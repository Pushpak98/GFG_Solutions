import math

for _ in range(int(input())):
    a=list(map(int, input().split()))
    l=(math.factorial(abs(a[1]-a[0])))*(math.factorial(abs(a[1])))
    k=math.factorial(a[0])/l
    print(int(k))
    