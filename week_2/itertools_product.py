from itertools import product
# Enter your code here. Read input from STDIN. Print output to STDOUT
A=list(map(int, input().split()))
B=list(map(int, input().split()))
for i in sorted(tuple(product(A, B))):
    print(i, end=' ')
