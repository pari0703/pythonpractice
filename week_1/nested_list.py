n = int(input("Enter the number of students: "))
students = []
   
for _ in range(n):
    name = input("Enter the student's name: ")
    score = float(input("Enter the student's score: "))
    students.append([name, score])
     
students.sort(key=lambda x: x[1])
    
unique_grades = sorted(set(score for name, score in students))
second_lowest_grade = unique_grades[1]
    
second_lowest_students = []
for name, score in students:
    if score == second_lowest_grade:
        second_lowest_students.append(name)
for name in sorted(second_lowest_students):
        print(name)
