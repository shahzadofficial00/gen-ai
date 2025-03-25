# 15 lists  

 # ls = list(("Lahore","Faisalabad","Jaranwala")) # constructor method

# ls= []
# ls = [ "Lahore","Faisalabad","Jaranwala"]
# print(type(ls), ls)
# print(type(ls), ls)

# ls = ["Lahore","Faisalabad","Jaranwala"]

# print(ls[2:])

# ls[1] = "Multan"
# ls[0:1] = [ "Karachi"]
# ls[2:] = ["Multan"]
# ls[1:2] = ["Peshawar"]
# ls[0:] = ["Lahore","Faislabad","Jaranwala","Peshawar"]
# print(ls)

# ls = ["Lahore","Faisalabad","Jaranwala"]
# ls.append("Peshawar")
# ls.insert(2,"Peshawar")
# ls.pop(0)
# ls.remove("Faisalabad")
# del ls

# ls.clear()
# print(ls)

# 16 for loops 

# ls = ["apple","banana","mango", "orange"]

# print(ls)
# for item in ls:
#     print(item)

# Assignments class 19/ 03/ 2025:______________________

# ls = ["lahore","faisalabad","jaranwala"]
# lp=[]
# for x in ls:
#     p = x[0:1].upper() + x[1:-1].lower() + x[-1:].upper()
#     lp.append(p)
#     print(p)
# print(lp)

# ls = [ "lahore","Faisalabad","jaranwala"]
# lp = []
# for x in ls:
#     lp.insert(0,x)
# print(lp)



# ls1 = ["Faisalabad","jaranwala"]
# ls2 = ["Lahore"]
# ls1.extend(ls2)
# print(ls1)

# for i in range(1,10):
#     print("Pakistan Zindabad: " + str(i))

# ls = [1,2,3,4,5,6,7,8,9,10]
# ls2 = []
# for i in ls:
#     if i % 2 == 0:
#         ls2.append(i)
#         print(i)
# print(ls2)

# i = 0
# while i < len(ls):
#       print(ls[i])
#       i= i + 1

# ls = ["Lahore","Jaranwala"]
# n = input("Enter your city : ")
# city_found = False
# for x in ls:
#     if n == x:
#         city_found = True

# if city_found:
#     print("your city is neat and clean now.")
# else:
#     print("your city is not neat and clean now")

# ls = ["Lahore","Jaranwala"]
# [print(x) for x in ls]

# ls = ["Lahore","Jaranwala"]
# ip = input("Enter your city :")
# ls2 = [x for x in ls if ip==x]
# print(ls2)

# ls1 = [1,2,3,4,5,6,7,8,9,10]
# ls2 = [x for x in ls1 if x %2 == 0]
# print(ls2)

# ls1 = ["Lahore","Jaranwala","Faisalabad","Jaranwala"]
# ls2 = [x if x!= "Jaranwala" else "144GB" for x in ls1 ]
# print(ls2)

