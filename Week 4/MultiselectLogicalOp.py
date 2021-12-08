#!/usr/bin/python3
# and/or
grade = eval(input("Enter grade: "))

if (grade < 0) or (grade > 100):
    print("Awnser is Invalid")
elif (grade >= 90) and (grade <= 100):
    print("Grade is 'A'")
elif (grade >= 80) and (grade < 90):
    print("grade is 'B'")
elif (grade >= 70) and (grade < 90):
    print("grade is 'C'")
else:
    print("grade is 'F'")
