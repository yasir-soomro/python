
# print("welcome to mini calculator in python ")
# #  users input 
# number_one = float(input("Enter your First Number"))
# operator_signs = input("Enter your operator sign( +,-,*,/ )")
# number_two = float(input("Enter your Second Number"))


# if operator_signs == "+":
#     result = number_one + number_two
#     print("Sum of the Numbers",result)
# elif  operator_signs == "-":
#     result = number_one - number_two
#     print("subtract of the Numbers",result)
# elif  operator_signs == "*":
#     result = number_one * number_two
#     print("Multiplication of the Numbers",result)
# elif  operator_signs == "/":
#     if number_two  != 0: 
#      result = number_one / number_two
#     print("division of the Numbers",result)
# else:
#         print("🚫 Error: Division by zero is not allowed.")


# # print("✅ Thank you for using the calculator!")

# numbers = [12, 3, 5, 8, 9, 10, 21, 30]
# if numbers  == 0 :
#     print(f"even ={numbers.count()} ")
# # # Your logic here


# # Input: "afzal"
# # Output: "lazfa"
# Name = input("reverse your name :")
# Name.reverse()
# print("reverse the name",Name.rev)

# # Input: 123
# # Output: 6  (1 + 2 + 3)
# user = input("enter number")

# ✅ Q2: Multiply All Numbers in List


nums = [1, 2, 3, 4]
num = 1
for val in nums :
    num *= val 
    
    
    
    print(num)
# Your logic here:
# Start with result = 1
# Multiply each number with result using a loop


# Your logic here:

# Convert num to string
# Reverse the string
# Compare with original
# num = 121
# num [::-1] 

# if res == num :
#     print("plandrome",res)
# else :
#     print("not plandrome",res)

# Q3: Find the Largest Element Without max()
# max_list_Number
max_list  = [10, 23, 5, 78, 99, 32]
max_list_Number = max_list[0]
for Value in max_list:
    if Value > max_list_Number :
        max_list_Number = Value

print("maximum number is :",max_list_Number)

# Output: 99
# ✅ Q4: Reverse a List Without [::-1]
reverse_list = [1, 2, 3, 4, 5]
reverse_list.reverse()
print(reverse_list)
# Output: [5, 4, 3, 2, 1]


original_list = [1, 2, 3, 4, 5]
reversed_list = []

for item in original_list:
    reversed_list.insert(0, item)
 
 
print(reversed_list)

# "Every expert was once a beginner." 🚀
# "Your dedication is your superpower." 💪


# higher order functions 
# List comprehenshion 
list_numbers = [2,1,4,3,7,8]
square_list_number = []
for num in list_numbers :
    square_list_number = num * num
    # square_list_number = num
    print(square_list_number)

student_record ={
    "student_id_one"  : {"name"  : "Bilal", "age"  : 18, "grade" : "D"},
    "student_id_two"  : { "name"  : "Nasir", "age"  : 14, "grade" : "A" },
    "student_id_three" : { "name"  : "Afzal", "age"  : 22, "grade" : "A+" },
    "student_id_four"  : { "name"  : "Aftab", "age"  : 28, "grade" : "C" },
}

for student in student_record.values() :

    print(student["name"])
  
student_data ={}
  
def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    grade = input("Enter Grade: ")

    student_data[student_id] = {
        "name": name,
        "age": age,
        "grade": grade
    }
    print("✅ Student added successfully!\n" )