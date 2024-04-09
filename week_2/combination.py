# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
n=input()
s, k= n.split()[0], int(n.split()[1])
for i in range(k):
    for char in combinations(sorted(s), i + 1):
        print(''.join(char))
