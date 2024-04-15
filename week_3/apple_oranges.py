def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    count1 =0
    count2=0
    for i in range(len(apples)):
        if a+apples[i] in range(s, t+1):
            count1 += 1
    for i in range(len(oranges)):
        if b+oranges[i] in range(s, t+1):
            count2 += 1
    print(count1)
    print(count2)
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
