##########     Class and object(instance) attributes
#####    instance attr > class attr


class Laptop:

    name = "Anonymous"                              ###Class Attribute

    def __init__(self, name, price):
        self.name = name                            ####instance (Object) Attribute
        self.price = price

        print("New Laptop Information")

l1 = Laptop("HP", 50000)
print(l1.name)


l2 = Laptop("Asus", 45000)
print(Laptop.name)