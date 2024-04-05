print("Enter number of students:")
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input("Enter name along with scores:\n").split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input("Enter name of the student whose average score is needed:\n")
print("The average score of",query_name,"is:")
print(format(sum(student_marks[query_name]) / 3, '.2f'))