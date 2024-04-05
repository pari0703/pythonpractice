print("Enter the elements into array:")
arr=list(map(int, input().split()))
n=len(arr)
print("Enter the element to be searched:")
key=int(input())
pos=-1
start=0
end=n-1
while start <= end:
    mid = (start + end) // 2
    if arr[mid] == key:
       pos=mid
       break
    elif arr[mid] < key:
       start = mid + 1  
    else:
       end = mid - 1   
if pos != -1:    
   print("the element",key," is present at index:",pos)
else:
   print("the element",key," is not present in the array.")        
