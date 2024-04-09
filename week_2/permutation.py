# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
k=input()
s, n=k.split()[0], int(k.split()[1])
for i in sorted(list(permutations(s, n))):
    print(''.join(i))
