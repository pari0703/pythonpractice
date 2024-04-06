import numpy as np
A=[]
B=[]
N,M=list(map(int, input().split()))
for _ in range(N):
    row=list(map(int, input().split()))
    A.append(row)
for _ in range(N):
    row1=list(map(int, input().split()))
    B.append(row1)
print(np.add(A,B))
print(np.subtract(A,B))
print(np.multiply(A,B))
print(np.floor_divide(A,B))
print(np.mod(A,B))
print(np.power(A,B))
