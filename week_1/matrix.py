import numpy

N, M = list(map(int, input().split())) 

A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

s = numpy.sum(A, axis=0)
print(numpy.prod(s))
