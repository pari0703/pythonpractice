import numpy
N, M = list(map(int, input().split())) 
A = []
for _ in range(N):
   row=list(map(int, input().split()))
   A.append(row)
minimum = numpy.min(A, axis=1)
print(numpy.max(minimum))   



