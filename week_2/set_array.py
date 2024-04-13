def average(array):
    # your code goes here
    a=set(array)
    length=len(a)
    return sum(a)/length
        
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)