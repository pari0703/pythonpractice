
def diagonalDifference(arr):
    # Write your code here
    length=len(arr)
    sum1=0
    sum2=0
    for i in range(length):
        for j in range(length):
            if i == j:
                sum1 += arr[i][j]
            if i+j == length-1:
                sum2 += arr[i][j]
    return abs(sum1 - sum2)
            
if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(str(result) + '\n')
