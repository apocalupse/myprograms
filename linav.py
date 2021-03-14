import time
import random
def linear_search(arr,key):
    n=len(arr)
    for i in range(n):
        if(arr[i]==key):
            print(i)
def sum_arr(arr):
    sum=0
    n=len(arr)
    for i in range(n):
        sum=sum+arr[i]
    print(sum)
myarr=[]
size=int(input("enter size of an array \n"))
for i in range(size):
    b=random.randrange(1,100)
    myarr.append(b)
print(myarr)
exe_time=[]
t=int(input("enter t \n"))
if(t<size):
    for i in range(t):
        myarr[i]
        start=time.time()
        linear_search(myarr,myarr[i])
        end=time.time()
        execution_time=end-start
        exe_time.append(execution_time)
    print(exe_time)
sum_arr(exe_time)



