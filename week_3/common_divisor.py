def gcd(a, b):
    # Find the greatest common divisor using Euclid's algorithm
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    # Calculate the least common multiple using the formula: lcm(a, b) = (a * b) / gcd(a, b)
    return (a * b) // gcd(a, b)

def getTotalX(a, b):
    # Find the LCM of all elements in array a
    lcm_a = a[0]
    for i in range(1, len(a)):
        lcm_a = lcm(lcm_a, a[i])
    
    # Find the GCD of all elements in array b
    gcd_b = b[0]
    for i in range(1, len(b)):
        gcd_b = gcd(gcd_b, b[i])
    
    count = 0
    # Count the number of multiples of lcm_a that evenly divide gcd_b
    for i in range(lcm_a, gcd_b + 1, lcm_a):
        if gcd_b % i == 0:
            count += 1
    return count
    

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(str(total) + '\n')

