## Inheritance


class Car:

    Color = "White"


    @staticmethod 
    def start():
        print("Car Started........")

    
    @staticmethod
    def stop():
        print("Car Stopped.........")



class ToyotaCar(Car):

    def __init__(self, name):
        self.name = name


car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

print(car1.start())
print(car1.Color)
        