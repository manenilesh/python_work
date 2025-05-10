# Nested If

Age = int(input("Enter Your Age:- "))

if Age >= 18:
    if Age >= 80:
        print("Can not drive due to Upper Age")
    else:
        print("Can drive")
else:
    print("You does not have rights for driving")