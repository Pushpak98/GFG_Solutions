

for _ in range(int(input())):
    m = int(input())
    List = []
    #for m in range(int(input())):
    arr = list(map(int, input().split()))
    for i in range(m):
        for j in range(1,max(arr)+1):
            if arr[i]%j == 0:
                List.append(j)
    print(List)

   
#def most_frequent(List): 
    k= max(set(List), key = List.count) 
    print(k)
  
#print(most_frequent(List)) 

'''    

#def most_frequent(k): 
counter = 0
num = 0 
  
for i in k: 
    curr_frequency = k.count(i) 
    if(curr_frequency> counter): 
        counter = curr_frequency 
        num = i 
        print(i)
        
 #   return num
  

#List = [2, 1, 2, 2, 1, 3] 
#print(most_frequent(k)) 


   

    
import statistics 
from statistics import mode 
  
def most_common(List): 
    return(mode(List)) 
    
List = [2, 1, 2, 2, 1, 3] 
print(most_common(List)) 

    

    arr = []
    if len(arr)<=m: 
        arr = list(map(int, input().split()))
    
    k=[]
    for i in range(1,arr[0]+1):
        if (arr[0] % i == 0):
            if (arr[1] % i == 0):
                k.append(i)
    print(max(k))    
'''