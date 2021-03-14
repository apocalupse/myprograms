#execution time for binary search
import time
import random
def binary_search(arr,m,key):
    first=0
    last=m-1
    while(first<=last):
        mid=(first+last)//2
        if(arr[mid]==key):
            return mid
        elif(arr[mid]<key):
            first=mid+1
        if(arr[mid]>key):
            last=mid-1
    return -1
output=[]
best_time=[]
# number of array we want to execute
t=int(input("enter t \n"))
for i in range(t):
    size=int(input("enter size \n"))
    myarr=[]
    for i in range(size):
        num=random.randrange(1,1000)
        myarr.append(num)
    #input best case
    x=myarr[(size-1)//2]


    start= time.time()
    ans=binary_search(myarr,size,x)
    end= time.time()
    execution_time=end-start
    best_time.append(execution_time)
    output.append(ans)
for ans in output:
    print(ans)
for e in best_time:
    print(e)


