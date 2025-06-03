class Student:

    def __init__(self, name, subject_marks):
        self.name = name
        self.subject_marks = subject_marks

    def get_avg(self):
        sum = 0
        for val in self.subject_marks:
            sum += val
        print("Hi", self.name , "Your Average Score is:- ", sum / 3)


s1 = Student("Shree", [99,98,96])

s1.get_avg()

