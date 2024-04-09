# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
n=input()
s, k=n.split()[0], int(n.split()[1])
for i in sorted(list(combinations_with_replacement(sorted(s), k))):
    print(''.join(i))