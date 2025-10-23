marks = int(input("Enter your marks: "))

if marks >= 90:
    Grade = "A"

elif marks >= 80:
    Grade = "B"

elif marks >= 70:
    Grade = "C"

elif marks >=60:
    Grade = "D"

elif marks >= 50:
    Grade = "E"

else:
    Grade = "F"

print("Your grade is: ", Grade)