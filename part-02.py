
# # #  <----------- Dictionary and Set ---------->
# # info = {
# #     "key" : "value",
# #     "name" : "afzal",
# #     "learn" : "coding",
# #     "isPass" : True,
# #     "age" : 23
# # }
# # infos = info.copy() 
# # infos         
# # for item in info :
# #     item = info
# #     print(item)
# # # print(info["key"])
# # # info.copy()
# # # print(info.values())
# # # print(len(info["learn"]))
# # student_marks_dictionary = {
# #     "Name"  : "Yasir Afzal Soomro",
# #     "Age"   : 22,
# # "every_class_nested_dictionary" : {
# #     "class vi"  : ["English  = 77","Sindhi  = 80","social study  = 71","science  = 49","islamiat  = 72","urdu  = 84","arabic  = 38"],
# #     "class vii" : ("English  = 62","Sindhi  = 69","social study  = 73","science  = 58","islamiat  = 89","urdu  = 80","arabic  = 42"),
# #     "isPass?"  : True,
# #     12 : 2.44
# #     }
# # }
# # print (len(student_marks_dictionary))
# # print (len(student_marks_dictionary ["every_class_nested_dictionary"]["class vii"] ))

# # print (len(student_marks_dictionary ["every_class_nested_dictionary"]["class vi"] ))

# my_dic = {
#     "name" : "Nasir Ali",
#     "age" : 12,
#     "subjects" : {
#         "topics" : ["dict","sets","list"],
#         "makrs": (44,49,89,90,78,71),
#        "is_pass"  : True,
#        12.99 : 94.1
#     } 
# }

# my_dic ["name"] = "Yasir Afzal"
# my_dic ["age"] = "13"
# my_dic ["type"] = "dictionary"
# # my_dic ["subjects"] = ["ff","dd"]
# my_dic ["subjects"]["topics"] = ["dict","sets","list","tupple"]
# print(type(my_dic))


# student = {
#     "name"  : "Bilal Ahmed",
#     "subject" : {
#       "phy"    :  44,
#       "eng"    :  72,
#       "math"    : 49,
#     }
# }
# print(student["subject"] ["eng"])
# student["name"]  = ["Afzal soomro"]
# student["name"]  = ["Bilal Ahmed "]
# # student.get("name")  = ["Afzal soomro"]
# print (student.get("name"))
# print (list(student.values()))
# print(student["subject"] ["eng"])
# student["name"]  = ["Afzal soomro"]
# student["name"]  = ["Bilal Ahmed "]
# # student.get("name")  = ["Afzal soomro"]
# print (student.get("name"))   # type safe  get method
# print (list(student.values()))   # value method 
  
# print (list(student.items()))   # items method
# # print (list(student.update()))   # update method
# pairs = list(student.items())
# print(pairs[0])

# print (list(student.keys()))  # keys method

# # numbers = [1, 2, 2, 3]
# # unique = set(numbers)  # {1, 2, 3}
# # my_set = {1, 2, 3, 4}
# # for item in my_set:
# #     num = item / item
    
# #     print(num)

# # my_list = list(my_set)
# # print (my_list)

# # print([student]["name2"]) # error
# print ("Before")
# print(student.get("name2")) # None
# print("hi...Hello")
# print("hi...Yasir")
# print("hi...Afzal")
# print("hi...Asifa")
# student.update({"City":"karachi"})
# print(student)
# print ("After")
# roll_no = student.get("roll_number", "Not Found")
# print(f"Student Roll Number: {roll_no}")
collections = {}   # empty sytntax of dictionary
collectionss = set()  # empty syntax of set
collectionss.add(1)
collectionss.add(2)
collectionss.add(3)
# collectionss.pop(2) why he give error
collectionss.add((1,2,7,8))
# collectionss((1,2,7,8))
# collectionss.add([1,2,7,8])# TypeError: unhashable type: 'list'

print(type(collections))  # class dictionary 
print(type(collectionss))  # class set 
# print(collectionss.clear("set is empty"))  # here is output 
print(collectionss.pop())
print(collectionss)
# # sets in python 
collection = {1,2,2,2,3,4,"Hello","world","Hello"} # unordered list set
print(collection)
print(type(collection))
print(len(collection))


# important methods of set union & intersection
set1 = {1,2,3,4}
set2 = {4,7,8,9,7}

print (set1.union(set2))
print (set1.intersection(set2)) # 4 is common value 

res = set1 , set2
print (res)


# you are given a list of subjects  for  students. assume one classroom is required for 1 subject.how many classrooms are needed by all students

"python","java","C++","python","javascript","java","python","java","C++","C",

total_subject =   {
    "python","java","C++","python","javascript","java","python","java","C++","C",}
print  (len( total_subject))

x = 5
while x >= 1:
    x -= 1
