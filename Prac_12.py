marks = int(input("Enter Your Marks:- "))
if marks >= 90:
    Grade = "A"
elif marks >= 80 and marks < 90:
    Grade = "B"
elif marks >= 70 and marks < 80:
    Grade = "C"
else:
    Grade = "D"

print("Grade of the Student -->", Grade)