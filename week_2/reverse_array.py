def reverse_array(arr):
    return arr[::-1]
n=int(input())
arr=[]
for i in range(n):
    arr.append(input())
rev_array=reverse_array(arr)
print(' '.join(rev_array))
