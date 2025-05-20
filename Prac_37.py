
class Account:
    
    def __init__(self, acc_no, bal):
        self.acc_no = acc_no
        self.bal = bal
    
    def debit(self, amount):
        self.bal -= amount
        print("Rs.", amount , "was Debited")
        print("Total Balance is ", self.get_bal())
        
    def  credit(self, amount):
        self.bal += amount
        print("Rs.", amount ,"was Credited")
        print("Total Balance is", self.get_bal())
    
    def get_bal(self):
        return self.bal

acc1 = Account(1001, 78.50)
print("Account No: ", acc1.acc_no, "Total Balance: ",acc1.bal)

acc1.debit(10)
acc1.credit(7)
