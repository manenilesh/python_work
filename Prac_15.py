num_1 = int(input("Enter First No:- "))
num_2 = int(input("Enter Second No:- "))
num_3 = int(input("Enter Third No:- "))

if num_1 > num_2 and num_1 > num_3 :
    print("First Number is Greatest")
elif num_2 > num_1 and num_2 > num_3:
    print("Second Number is Greatest")
else:
    print("Third Number is Greatest")