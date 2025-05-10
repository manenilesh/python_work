print("List in Python")

student = ["Nilesh","Yogesh","Shubham","Sid"]
print(student)
print(student[0:3])

print("\n")
print("\n")
print("\n")



print("\nNormal List")
Number = [2,1,10,5,4,9,6,8,7]
print(Number)

print("\nChanging Value of List (Mutable)")
Number[2] = 3
print(Number)

print("\nappend value in List")
Number.append(10)
print(Number)

print("\nReverse the List")
Number.reverse()
print(Number)

print("\nSort the List Descending Order Like [3,4,1,2] ---> [4,3,2,1]")
Number.sort(reverse=True)
print(Number)

print("\nSort the List Ascending Order Like [3,4,1,2] ---> [1,2,3,4]")
Number.sort()
print(Number)

print("\nInsert New value with the help of Indexing Like Replacing old value with New value")
Number.insert(9,11)
print(Number)

print("\nRemove a Value in List")
Number.remove(11)
print(Number)

print("\nDelete a specific value using it's index number")
Number.pop(9)
print(Number)

print("\nCount total count of single value in List")
print(Number.count(7))