# Palindrome Number 

list1 = [1,2,3,4,3,2,1]
copy_list_1 = list1.copy()
copy_list_1.reverse()

if list1 == copy_list_1:
    print("Palindrome")
else:
    print("Not Palindrome")