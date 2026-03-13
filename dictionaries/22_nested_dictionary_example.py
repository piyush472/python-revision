# Question 22: Nested dictionary example
# Write a Python program demonstrating a nested dictionary (e.g., student data with subjects).
students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    student_name = input("Enter student name: ")
    
    subjects = {}
    m = int(input("Enter number of subjects: "))
    
    for j in range(m):
        subject = input("Enter subject name: ")
        marks = int(input("Enter marks: "))
        
        subjects[subject] = marks
    
    students[student_name] = subjects

print(students)