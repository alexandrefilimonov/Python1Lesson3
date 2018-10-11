from random import *
# pass sort_to_max([2,10,-12,2,5,20,-11,4,4,0]
n = int(input("Enter qty of elements of array:"))
i = 0
list = []
print("Array before sorting:")
while  (i<n) :
    list.append(randint(-100,100))
    print("Element ",(i+1),":",list[i])
    i+=1
def sort_to_max(arr) :
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Array after sorting:")
    i=0
    while  (i<n) :
        print("Element ",(i+1),":",arr[i])
        i+=1
sort_to_max(list) 

