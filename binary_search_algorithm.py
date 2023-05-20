pos=0
def binary_search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid = (l+u)//2
        if list[mid] ==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False

list = [2,4,5,6,78,22,1,9,55]
n=int(input("Enter the number to be found in the list:  "))
if binary_search(list,n):
    print("Found at: ",pos+1)
else:
    print("Not found")