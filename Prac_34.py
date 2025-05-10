##Practice Question

# with open("Practice.txt","w") as f:
#     f.write("Hi Everone \nWe are learning File I/O \nusing Java \nI like programming in Java")
    
    
with open("Practice.txt","r") as f:
    data = f.read()
new_data = data.replace("Java","Python")
print(new_data)  

with open("Practice.txt","w") as f:
    f.write(new_data)