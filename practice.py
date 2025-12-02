
#  find the maximam number 

max_list = [12,2,3,33,13,32]
min_number = max_list[0]
for item in max_list :
    if item < min_number :
        min_number = item
        print("print minimam number" ,min_number)

print("maximam number is = ",max(max_list))


# WAP to input user's first name & print its length

# my_name = input("Enter your first name")
# print(len(my_name),my_name)
# print(my_name.find["s"])
str = "sharda khapra"
str = str.find("k")
# print(str.find("s"))
 
print(str)

z = "Hi i am Afzal Soomro from pakistan sindh"
z = z.count("a")
print("Count of a :",z)

Num = 10
if Num % 2 == 0 :
    print("even")
else:
    print("odd")

number_number = 10
if number_number % 4 == 2 :
    print("number greatest is = ")
else:
    print("not divisable")


# a = int(input("enter your first number :"))
# b = int(input("enter your second number :"))
# c = int(input("enter your third number :"))
# d = int(input("enter your Fourth number :"))

# if (a >= b and a >= c):
#     print("first number is largest number",a)
# elif b >= a and b >= c :
#     print("second number is largest number",b)
# elif c >= a and c >= b :
#     print("Fourth number is largest number",c)

# else:
#     print("Fourth number is largest number",c)

x = int(input("enter number :")) 
if x % 7 == 0 :
    print("Multiple of seven 7 = ",x)
else:
    print(" not Multiple of seven 7 = ",x)



# Movies = input(["wanted","dilwale","jaan"])
# # print(Movies)
# movies = []
# mov1 = input("enter ist movie")
# mov2 = input("enter 2nd movie")
# mov3 = input("enter thrid movie")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print("enter your fav movies",movies)


race_car_list = ["r","a","c","e","c","a","r",]
result_car_list = race_car_list.copy()
result_car_list.reverse()
if  result_car_list == race_car_list :
    print("palindrome")
else:
    print("not palindrome")


grade = ("C","B","C","C","E","A",)
grade = grade.count("C")
print(grade)

sort_value = ["D","B","F","C","E","A",]
sort_value.sort()
print(sort_value)


marks = 91

if marks <= 100 and marks >= 90:
    grade = "A+"
elif  marks <= 89 and marks >= 75:
    grade = "A"
elif  marks <= 74 and marks >= 60 :
    grade = "B"
elif  marks <= 59 and marks >= 45:
    grade = "C"
elif  marks <= 44 and marks >= 35:
    grade = "D"
else:
    print("Fail")

print("grade is here ",grade,"and marks obtained",marks)



age = 21

if age <= 4 :
    ticket_price = "Free"
elif age <= 12 and age >= 4:
    ticket_price = "Rs. 500"

elif age <= 17 and age >= 13:
    ticket_price = "Rs. 800"

elif age <=59  and age >= 18:
    ticket_price = "Rs. 1200"

elif age >= 60 :
    ticket_price = "Rs. 700"
else :
    ticket_price = "without ticket not allowed"


print("your age is = ",age," and your ticket price is = ",ticket_price)


