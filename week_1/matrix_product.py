import numpy
N=int(input())
A=[]
B=[]
for _ in range(N):
    row=list(map(int, input().split()))
    A.append(row)
for _ in range(N):
    row1=list(map(int, input().split()))
    B.append(row1) 
print(numpy.dot(A, B))