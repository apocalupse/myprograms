def partition(arr):
    n=len(arr)
    x=arr[n-1]
    j=0
    i=j-1
    for j in range(j,n-2):
        if(arr[j]<=x):
            i=i+1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    temp=arr[i+1]
    arr[i+1]=arr[n-1]
    arr[n-1]=temp
myarr=[2,8,7,1,3,5,6,4]
partition(myarr)
print(myarr)