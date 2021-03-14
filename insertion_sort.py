import random
import time
def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while arr[j]>key and j>-1:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key

def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i,n):
            if(arr[i]>arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp

def random_c(arr):
    start=time.time()
    bubble_sort(arr)
    end=time.time()
    execution_time=end-start
    arr1.append(execution_time)

    start=time.time()
    insertion_sort(arr)
    end=time.time()
    execution_time=end-start
    arr2.append(execution_time)

    start=time.time()
    selection_sort(arr)
    end=time.time()
    execution_time=end-start
    arr3.append(execution_time)

def sorted_c(arr):
    start=time.time()
    bubble_sort(arr)
    end=time.time()
    execution_time=end-start
    arr4.append(execution_time)

    start=time.time()
    insertion_sort(arr)
    end=time.time()
    execution_time=end-start
    arr5.append(execution_time)

    start=time.time()
    selection_sort(arr)
    end=time.time()
    execution_time=end-start
    arr6.append(execution_time)

def reverse_c(arr):
    start=time.time()
    bubble_sort(arr)
    end=time.time()
    execution_time=end-start
    arr7.append(execution_time)

    start=time.time()
    insertion_sort(arr)
    end=time.time()
    execution_time=end-start
    arr8.append(execution_time)

    start=time.time()
    selection_sort(arr)
    end=time.time()
    execution_time=end-start
    arr9.append(execution_time)




t=int(input())
arr1=[]
arr2=[]
arr3=[]
arr4=[]
arr5=[]
arr6=[]
arr7=[]
arr8=[]
arr9=[]
for i in range(t):
    rajesh=[]
    size=int(input())
    for i in range(size):
        b=random.randrange(1,1000)
        rajesh.append(b)
    random_c(rajesh)
    rajesh.sort()
    sorted_c(rajesh)
    rajesh.reverse()
    reverse_c(rajesh)
print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)
print(arr6)
print(arr7)
print(arr8)
print(arr9)
        
