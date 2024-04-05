print("Enter elements into array:")
arr=list(map(int, input().split()))
n=len(arr)
for i in range(0,n-1):
   for j in range(0,n-i-1):
      if arr[j] > arr[j+1]:
         arr[j], arr[j + 1] = arr[j + 1], arr[j]
print("The Sorted Array is:")
for i in range(n):
 print(arr[i],end='  ')         