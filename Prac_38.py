
#### Use of del Keyword

class Student:

    def __init__(self, name, Age):
        self.name = name


s1 = Student("Shree", "2")

print(s1.name)
del s1.name
print(s1.name)

