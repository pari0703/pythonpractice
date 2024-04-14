def birthdayCakeCandles(candles):
    # Write your code here
    max=candles[0]
    count=0
    for i in range(len(candles)):
        if candles[i]>max:
            max=candles[i]
    for i in range(len(candles)):
        if max == candles[i]:
           count += 1
        else:
            count == 1
    return count

if __name__ == '__main__':

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print(str(result) + '\n')
