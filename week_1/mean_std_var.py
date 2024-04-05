import numpy
N, M=list(map(int, input().split()))
A=[]
for _ in range(N):
    row=list(map(int, input().split()))
    A.append(row)
mean1=numpy.mean(A, axis=1)
var1=numpy.var(A, axis=0)
std1=round(numpy.std(A, axis = None),11)      
print(mean1)
print(var1)
print(std1)
