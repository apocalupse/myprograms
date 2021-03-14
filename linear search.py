#execution time for linear search
import time
import random
def linear_search(arr,key):

    n=len(arr)
    for i in range(n):
        if(arr[i]==key):
            return i
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
    x=myarr[0]


    start= time.time()
    ans=linear_search(myarr,x)
    end= time.time()
    execution_time=end-start
    best_time.append(execution_time)
    output.append(ans)
for ans in output:
    print(ans)
for e in best_time:
    print(e)


