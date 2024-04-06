import numpy
N, M, P=list(map(int, input().split()))
A=[]
for _ in range(N):
    row=list(map(int, input().split()))
    A.append(row)
   
B=[]
for _ in range(M):
    row1=list(map(int, input().split()))
    B.append(row1)
 
print(numpy.concatenate((A, B), axis = 0))
   


