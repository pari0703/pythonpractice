def sum_array(ar):
    sum=0
    for i in  range(len(ar)):
        sum += ar[i]
    return sum
if __name__ and '__main__':
    n=int(input())
arr=list(map(int, input().split()))
print(sum_array(arr))