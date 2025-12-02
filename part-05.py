# File  I/O in python 
# python can be used to perform operations on a file.
# (read & write data)  
# types of all files 
# 1. text files : .txt , .docx, .log  etc 
# 2. Binary Files : .mp4 , . .mov, .png, .jpeg etc. 

f = open("document.txt", "r")
data = f.read(4)
line1 = f.readline()
print (line1)
print(data)
print(type(data))
f.close()

s = "hello"
n = int(s)
print(n)





