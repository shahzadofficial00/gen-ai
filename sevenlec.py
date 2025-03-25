# add code to repositery
# git status
# git add .
# git commit -m "assignments"
# git push



# 17  for loop while loop

ls = [ "Karachi", "Jaranwala", "Faisalabad"]
i = 0
while i < len(ls):
 print(ls[i])
 i = i+1



# 18 range 

# for x in range(2,21,2):
#     print(x)

# 19 list comprensions 

# ls = [x for x in range(2,10,2)]
# print(ls)

# ls = ["Karachi","Jaranwala","Faisalabad","kivi","test"]
# [print(x) for x in ls if "i" in x ]

# for x in ls:
#     if "a" in x:
#         ls2.append(x)

# ls = ["karachi","jaranwala","faisalabad","kivi","test"]

# ls2 = [x for x in ls if x != "Karachi"]
# ls2 = [x.capitalize() for x in ls ]
# ls2 = [x[0].upper()+x[1:-1].lower()+x[-1:].upper() for x in ls]
# ls2 = [x[0].upper() for x in ls if "F" in x]
# print(ls2)



# assignment table of 2

# for x in range(2,21,2):
#     print(x)


# Assignment: take a input from user and print in list

# a = input("input your name :")
# b = input("input your father name :")
# c = [a,b]
# print(c)

# Assignment fictorial

# num = int(input("Enter a number: "))  
# factorial = 1  

# for i in range(1, num + 1):  
#     factorial *= i  

# print("Factorial of", num, "is", factorial)


# Assignment : how many 3 in 100

# count = 0

# for i in range(1, 101):
#     count += str(i).count('3')

# print("Total occurrences of digit 3:", count)

    