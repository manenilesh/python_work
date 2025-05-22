######Constructor



class Student:
    
    ##Default Constructor
    def __init__(self):
        pass


    ##Prametrized Constructor
    def __init__(self, name, subject, marks):
        self.name = name
        self.subject = subject
        self.marks = marks
        print("Adding Student Information")

s1 = Student("Nilesh","Python",98)
print(s1.name, s1.subject, s1.marks)

s2 = Student("Tejas", "Maths", 88)
print(s2.name, s2.subject, s2.marks)