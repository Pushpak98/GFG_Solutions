import math
for _ in range(int(input())):
    n, m = map(int, input().split())
    rt = m ** (1/n)
    fl = math.floor(rt)
    ce = math.ceil(rt)
    if m == fl**n:
        print(fl)
    elif m == ce**n:
        print(ce)
    else:
        print(-1)