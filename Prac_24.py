# # Nested Dictionary  
# student = {
#     "Name" : "Nilesh",
#     "Subject_marks" : {
#         "Python" : 99,
#         "SQL" : 85,
#         "Java" : 67
#     }
# }

# print(student["Name"])
# print(student["Subject_marks"])
# print(student["Subject_marks"]["Python"])




# #Dictionary Methods
    
# info = {
#     "Name" : "ApnaCollege",
#     "Subject" : ["Python","C","Java"],
#     "Topics" : ("Dictionary","Set")
#     }
# print(info["Name"]) 
# print(info.keys())
# print(list(info.keys()))     ## Type casting ## Convert into List 
# print(tuple(info.keys()))    ## Type casting ## Convert into Tuple
# print(len(info)) 



# #Dictionary Methods
    
# info = {
#     "Name" : "ApnaCollege",
#     "Subject" : ["Python","C","Java"],
#     "Topics" : ("Dictionary","Set")
#     }
# print(info["Name"]) 
# print(info.values())
# print(list(info.values()))  




# #Dictionary Methods
    
# info = {
#     "Name" : "ApnaCollege",
#     "Subject" : ["Python","C","Java"],
#     "Topics" : ("Dictionary","Set")
#     }
# pairs = list(info.items())
# print(info["Name"])
# print(pairs[1])




# #Dictionary Methods
    
# info = {
#     "Name" : "ApnaCollege",
#     "Subject" : ["Python","C","Java"],
#     "Topics" : ("Dictionary","Set")
#     }
# print(info["Name"])       ## it return Error    
# print(info.get("Name"))   ## When error occur in Statement then it return None



# #Dictionary Methods
    
# info = {
#     "Name" : "ApnaCollege",
#     "Subject" : ["Python","C","Java"],
#     "Topics" : ("Dictionary","Set")
#     }

# print(info)

# info.update({"Garde" : "Karad"})      ## Update the dictionary 
# print(info) 




