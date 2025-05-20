### OOPs Concept

# 1. Class 2. Object 3.Abstraction 4.Encapsulation 5.Inheritance 6. Polymorphism




class Company:
    
    def __init__(self, name, employee, location):
        self.name = name
        self.employee = employee
        self.location = location
        
    @staticmethod
    def welcome():
        print("Welcome in", p1.name)
        
    
    
    def  avg_emp(self):
        avg = 0
        for val in self.employee:
            avg += val
        print("Average emp of Both Branch is ", avg/ 2)
        
    
        
    

p1 = Company("PCGI", [200 ,130], "Pune and Thrissur")

p1.welcome()

print(p1.name, p1.employee, p1.location)

p1.avg_emp()



