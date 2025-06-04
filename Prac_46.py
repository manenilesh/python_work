## Inheritance

##Types  1- Single inheritance,    2- Multilevel inheritance,    3- Multiple inheristance


##1- Single inheritance


class College:

    name = "SGM College Karad"
    
    def __init__(self, art, com, sce):
        self.art = art
        self.com = com
        self.sce = sce


branch = College("Art Dept", "Commerce Dept", "Science Dept")
print(branch.art)

class Dep_Fees(College):

   
    def __init__(self, A, C, S):
        self.A = A
        self.C = C
        self.S = S

fees = Dep_Fees("Art Fees - 1800", "Commerce Fees- 5500", "Science - 14000")

print(College.name)
print(branch.art)
print(fees.A)




