Age = int(input("Enter Your Age :- "))
if Age >= 18:
    print("You are eligible for voting")
elif Age < 18 and Age >= 1:
    print("You are not eligible for voting")
elif Age == 0:
    print("YOU ARE NOT BORN")
else:
    print("Wrong Value")