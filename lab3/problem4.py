grade = int(input("Please enter your grade: "))

if grade > 100:
    print("Invalid grade")
elif grade >= 90:
    print("Your grade is an A")
elif grade >= 80:
    print("Your grade is a B")
elif grade >= 70:
    print("Your grade is a C")
elif grade >= 60:
    print("Your grade is a D")
else:
    print("Your grade is an F")


