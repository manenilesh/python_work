######### Private Attribute and Objects             ---- Private Attribute and Objects used within a class and it can not accessible from Outside the class

class Person:

    __name = "Anonymous"

    def __hello(self):
        print("Hello Guys!!!!")

    def welcome(self):
        self.__hello()
        print("Welcome in Pune")


p1 = Person()
p1.welcome()        