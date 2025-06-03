####  1.Abstraction 2.Encapsulation 


### Abstraction - Hiding implementation details of a class and only showing essential features  to the user's.

### Encapsulation - Wrapping data and functions into a single unit(Object).

class car:
    
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clk = False
        
    
    def start(self):
        self.acc = True
        self.clk = True
        print("Car Started")
        
c1 = car()
c1.start()






        