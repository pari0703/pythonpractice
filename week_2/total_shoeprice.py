# Enter your code here. Read input from STDIN. Print output to STDOUT
X=int(input())
lst=list(map(int, input().split()))
n=int(input())
sum = 0
for _ in range(n):
    k=input()
    shoe_size, price =int(k.split()[0]), int(k.split()[1])
    if shoe_size in lst:
       sum += price
       lst.remove(shoe_size)
print(sum)
    