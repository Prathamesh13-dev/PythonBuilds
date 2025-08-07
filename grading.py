"""📅 Day 1 Project: Student Grading System (CLI)
🎯 Goal:
Create a program where:
User enters student name and marks in English , Hindi , Maths.
Program calculates:
Total marks
Average
Grade (A/B/C/D/Fail)
Prints a result summary"""
name = input("Enter your name  :")
sub = ["English","Hindi","Maths"]
marks = []
for subject in sub:
    while True:
        try :
            mark = int(input(f"Enter marks in {subject} out of 100:"))
            if mark <=100 and mark >=0:
                marks.append(mark)
                break
            else:
                print("Please enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

summ = sum(marks)
avg = summ/len(marks)
print(f"Your name is {name}")
print("..................Result summary .........................")
print(f"Sum :{summ}")
print(f"Average : {avg}")
if avg>=90 and avg<=100:
    print("Grade : A")
elif avg >=80 and avg <90:
    print("Grade : B")
elif avg >=70 and avg <80:
    print("Grade : C")
elif avg >=60 and avg <70:
    print("Grade : D")
elif avg<60:
    print("Fail")