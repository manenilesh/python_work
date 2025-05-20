##Practice Question

# with open("Practice.txt","w") as f:
#     f.write("Hi Everone \nWe are learning File I/O \nusing Java \nI like programming in Java")
    
    
# with open("Practice.txt", "r") as f:
#     data=f.read()
#     print(data)
    
#     new_data = data.replace("Java", "Python")
#     print(new_data) 

# with open("Practice.txt", "w") as f:
#     f.write(new_data)



# word=input("Enter a Word:- ")
# with open("Practice.txt","r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("Present")
#     else:
#         print("Absent")
        


##Using function
        
# def check_for_word(word):
#     with open("Practice.txt","r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("Present")
#         else:
#             print("Absent")
    
# check_for_word("am") 



def check_for_line(word):
    with open("Practice.txt","r") as f:
        data = f.readline()
        

check_for_line("nii") 