def miniMaxSum(arr):
    # Write your code here
    min=arr[0]
    max=arr[0]
    sum=0
    for i in range(len(arr)):
        sum += arr[i]
        if min>arr[i]:
            min=arr[i]
        if max<arr[i]:
            max = arr[i]
    sum1 = sum - max
    sum2 = sum - min
    print(str(sum1)+' '+str(sum2))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
