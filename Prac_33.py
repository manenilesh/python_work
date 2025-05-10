## Recurssion
## Recursive Fucntion
# def show(n):
#     if (n==0):              ##Base Case is important in Rescursion  
#         return
#     print(n)
#     show(n-1)
# #    print("END")
# show(5)



##Recurrence relation

def fact(n):
    if (n == 0 or n ==1):
        return 1
    else:
        return n * fact(n-1)

print(fact(5))
    