def compare_array(a, b):
    a1=0
    b1=0
    for i in range(3):
        if a[i] > b[i]:
            a1 += 1
        elif a[i]< b[i]:
            b1 += 1
    return [a1, b1] 
if __name__ and '__main__':
    n=int(input())
arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))
print(compare_array(arr1, arr2)) 
             