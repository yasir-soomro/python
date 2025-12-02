#  python 

# Sum of the two Numbers 
# Num1 = int(input("Enter your first number"))
# Num2 = int(input("Enter your second number"))

# Sum = Num1 + Num2
# print("Sum of the Numbers :",Sum)




str = "String"
Num = 123
Float = 12.23
Bool = True
print(type(str),"output of str = ",str)
print(type(Num),"output of Num = ",Num)
print(type(Float),"output of Float = ",Float)
print(type(Bool),"output of Bool = ",Bool)

List_Number = [12,11,30,4,17,19,10]
# max_Num = List_Number[0]
# for item in List_Number :
#     if item >=  max_Num :
#         max_Num = item
        # print("Maximam number is ",max_Num)
print("Maximum number is", max(List_Number))
print("Maximum number is", min(List_Number))
   # <----- Concatenation -----> 
str1 = "apna"
str2 = "college"
Concatenation_string = str1 + " " + str2
print(Concatenation_string)
print(len( Concatenation_string))

Str1 = "I am learning from apna college. \n my teacher name is sharda khapra"
print(Str1)

str4 = "Yasir afzal"
# str4[0] = "-"  # he give error because str object does not support item assignment 
print(str4)
# slicing in python 
y = "Yasir afzal"
x = "Yasir afzal"
print(x[1:4])  #   "asi"

Fruit = "pomegranates"
print(Fruit[-4:-1]) # "eta"

print(Fruit.endswith("es"))  #  "True"
print(Fruit.capitalize())  #  capitalize
print(Fruit.replace("s",""))  #  replace 
print(Fruit.find("g"))  #   find index 4
print(Fruit.count("e"))  #   count "e" index  2
age = 18
# if age >= 18 :
if True :
    print("can vote")
    print("can drive")

# student_marks = int (input("Enter Student Marks :"))
student_marks = 40
if (student_marks >= 90   and student_marks <= 100) :
    Grade = "A+"
elif student_marks >= 74 and student_marks < 90 :
    Grade = "A"
elif student_marks >= 60 and student_marks < 74 :
    Grade = "B"
elif student_marks >= 45 and student_marks < 60 :
    Grade = "C"
elif student_marks >= 35 and student_marks < 45 :
    Grade = "D"
else : 
    Grade = "Fail try next year"
print( "Your Grade according to Marks =",Grade )
print( f"Your Grade according to Marks the Grade is = {Grade} \n and Student Marks : {student_marks}" )
 
marks = ["Afzal","Asifa",22,17,2.13]
marks[1] = "Misbah"
print(marks)

strr = "afzal"
# strr[0] = "y"
print (strr)
# list slicing in python 
student_Score = [90,77,87,73,40,39]
student_Score[1:4] = -23,33,-38
print(student_Score)

List = [2,1,3]
List.append(4)  # adds one element at the end 
List.sort()     # sorts in ascending order
List.sort(reverse=True) # sorts in descending order
List.reverse()  # reverse List
List.insert(2,4)  # insert element at index 
List.remove(4)  # removes first occurrence of element  
List.pop(3)   # removes element at idx

print(List)

#   Tupples in Python 
# A built in data type that lets us create immutable sequences of values.

tup = (12,13,14,11,17)
print(type(tup))
print(tup.count(12))
print(tup.index(14))
