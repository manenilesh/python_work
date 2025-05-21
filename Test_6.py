####   Methods 


class College:

    clg_name = "SGM College Karad"

    def __init__(self, name, HSC_marks):
        self.name = name
        self.HSC_marks = HSC_marks

    def welcome(self):                                                  ####   Methods
        print("Welcome Student,", self.name)

    def get_HSC_marks(self):                                            ####   Methods
        return self.HSC_marks

s1 = College("Shree", 97)
s1.welcome()
print(s1.get_HSC_marks())

