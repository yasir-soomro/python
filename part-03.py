# loops in python 
#  Loops are used to reapet in instructions

print ("Hi... Hello!")
print ("Hi... Hello!")
print ("Hi... Hello!")
print ("Hi... Hello!")
a = 0
while a <= 4 :
    a += 1
    print("Hello...!")
    # a += 1
    print(a)

i = 1
while i <= 4 :
    print(i,"Yasir Afzal")
    i += 1
print("Loop Ended")
x = 4
while x >= 1 :
    print(x,"Muhammad Afzal")
    x -= 1
# prints numbers from 1 to 100
num = 1
while num <= 100 :
    print(num,"print numbers ")
    num += 1
# prints numbers from 100 to 1


nums = 100
while nums >= 1 :
    print(nums,"print numbers ")
    nums -= 1
table = 1
while table <= 10 :
    # print(table,f"x {2} = { table *2}")
    print(f"{2} x {table} = {2 * table}")
    table += 1

number = int( input("Enter a Table of number"))

y = 1
while y <= 10 :
    print(f"{number} x {y} = {number * y}")
    y += 1

num1 = [1,4,9,16,25,36,49,64,81,100]
idx = 0

while idx < len(num1) :
    print(idx ,"indixing wise printing number",num1[idx])
    idx += 1
num2 = (1,4,9,16,25,36,49,64,81,100,49)
n = 49
index = 0
while index < len(num2):
    if num2 [index] == n :
        print(n,"Found at",index)
        break
    else:
        print("Founing...",index)
    index += 1
print("End of Loop")

# Break and Continue 
ii = 1 
while ii <= 7:
    if(ii == 3):
     ii += 1
     continue
    print (ii)
    ii += 1
print("End of loop")


jj = 1 
while jj <= 17:
    if(jj % 2 ==0 ):
     jj += 1
     continue
    print (jj)
    jj += 1
print("End of loop")


jj = 1 
while jj <= 17:
    if(jj % 2 !=0 ):
     jj += 1
     continue
    print (jj)
    jj += 1
print("End of loop")

# FOR LOOP 
# loops are used sequential traversal, for traversing list,string, tupple etc.

List = [1,2,3]
for el in List:
   print(el)
#    el += 2   
