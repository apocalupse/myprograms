def partition(arr,p,r):
    x=arr[r]
    i=p-1
    for j in range(p,r):
        if arr[j]<=x:
            i=i+1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    temp=arr[i+1]
    arr[i+1]=arr[r]
    arr[r]=temp
    return (i+1)
def quick_sort(arr,p,r):
    if(p<=r):
        q=partition(arr,p,r)
        quick_sort(arr,p,q-1)
        quick_sort(arr,q+1,r)
        return a
a=[2,8,7,1,3,5,6,4]
b=len(a)
b = quick_sort(a,0,b-1)
print(b)
