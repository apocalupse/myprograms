
'''import random
def merge_sort(n):
    myarr=[]
    x=len(myarr)
    for i in range(x):
        b=random.randrange(1,1000)
        myarr.append(b)
    print(myarr)

merge_sort(13)
'''

import random
def merge_sort(arr):
    if(len(arr)>1):
        mid=int((len(arr)//2))
        L=arr[:mid]
        R=arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i=0
        j=0
        k=0
        while i<len(L) and j<len(R):
            if(L[i]<R[j]):
                arr[k]=L[i]
                i +=1
            else:
                arr[k]=R[j]
                j +=1
            k+=1
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1

            
myarr=[]
n=int(input("enter n \n"))
for i in range(n):
    b=random.randrange(1,100)
    myarr.append(b)
merge_sort(myarr)
print(myarr)

'''myarr = [54,26,93,17,77,31,44,55,20]
merge_sort(myarr)
print(myarr)'''

            





