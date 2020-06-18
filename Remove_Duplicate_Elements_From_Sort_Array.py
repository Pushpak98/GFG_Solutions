def remove_duplicate(n, arr):
    for x in arr:
        if arr.count(x)>1:
            arr.remove(x)
    print(len(arr))
    return 


remove_duplicate(3,[1,1,3])

n=remove_duplicate(3,[1,1,3])

for i in range(2):
    print(arr[i],end=' ')
print()
