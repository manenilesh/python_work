######### Private Attribute and Objects             ---- Private Attribute and Objects used within a class and it can not accessible from Outside the class


class Student:

    __name = "Nilesh"

    def __init__(self, last_name):

        self.last_name = last_name
    
    def city(self):
        print("Karad")



s1 = Student("Mane")

print(s1.name, s1.last_name)