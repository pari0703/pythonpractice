# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n=int(input())
student=namedtuple('student', 'Id Marks Class Name')
sum=0
for _ in range(n):
    data=input()
    x= student(Id=int(data.split()[0]), Marks=int(data.split()[1]), Class=int(data.split()[2]), Name=data.split()[3])
    sum +=x.Marks
average=sum/n
print(format(average, '.2f'))
