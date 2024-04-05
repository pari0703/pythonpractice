print("Enter the elements into array:")
arr=list(map(int, input().split()))
n=len(arr)
print("Enter the element to be searched:")
key=int(input())
pos=-1
for i in range(0,n-1):
    if arr[i] ==key:
        pos=i
        break
if pos != -1:    
   print("the element",key," is present at index:",pos)
else:
   print("the element",key," is not present in the array.")        
