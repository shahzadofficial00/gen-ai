# Tuple

# 20 tuples 
 
 # tup = ("hello",)
 
 # tp = tuple(("hello",))
 
 # ls = list((tp))
 
 # ls.append("guru99")
 # print(ls)
 # tup = tuple((ls))
 # print(tup)
 
 
 
 
 # print(type(tp))
 
 # del tup
 
 # print(tup)
 
 # print(type(tup))
 # print(type(tup))
 # print(tup[1])
 # print(tup[0:-1])
 
 # tup1 = ("tup 1",)
 # tup2 = ("tup 2",)
 
 # tup3 = tup1 + tup2
 # print(tup3)
 
#  tup1 = ("faisalabad","Jaranwala","Lahore")
#  tup2 = (1,2,3,4,5,6,7)
#  tup3 = tup2 + tup1
 
 # print(tup3[7:] + tup3[:7])
 # ls = list(tup3)
 # ls2 =[]
 # for i in  ls:
 #     ls2.insert(0, i)
 # tup4 = tuple(ls2)
 # print(tup4)
 # print(ls)
 
 
 





# tup = ("lahore","jaranwala","faisalabad")
# ls = list ((tup))
# lp = []
# for x in ls:
#     y = x[0:1].upper() + x[1:].lower()
#     lp.append(y)
# print(lp)


# unpacking

# tup = ("semester", "annual","master")
# (tup1,tup2,tup3)=tup
# print(tup2)

# # destructure

# tup = ("semester", "annual","master","m phill")
# (tup1,tup2,*tup3)=tup
# print(tup3)



#  15 Tuple assignment

# tup1 = ("faisalabad","Jaranwala","Lahore")
# tup2 = (1,2,3,4,5,6,7)
# tup3 = tup2 + tup1
# print(tup3[7:] + tup3[:7])


# Method 1: Using List Conversion and Extended Slicing

# tup1 = ("faisalabad","Jaranwala","Lahore")
# tup2 = (1,2,3,4,5,6,7)
# tup3 = tup2 + tup1
# list_tup3 = list(tup3)
# result_list = list_tup3[7:] + list_tup3[:7]
# result_tuple = tuple(result_list)
# print(result_tuple)

# Method 2: Using a Loop and Tuple Construction

# tup1 = ("faisalabad","Jaranwala","Lahore")
# tup2 = (1,2,3,4,5,6,7)
# tup3 = tup2 + tup1
# new_tup = ()
# for i in range(7,len(tup3)):
#     new_tup += (tup3[i],)
# for i in range(7):
#     new_tup += (tup3[i],)
# print(new_tup)

# method 3 Using Tuple Unpacking and Re-packing

# tup1 = ("faisalabad","Jaranwala","Lahore")
# tup2 = (1,2,3,4,5,6,7)
# tup3 = tup2 + tup1
# a,b,c,d,e,f,g,h,i,j = tup3
# new_tup = (h,i,j,a,b,c,d,e,f,g)
# print(new_tup)

# Method 4: Using Indexing and Tuple Creation

# tup1 = ("faisalabad","Jaranwala","Lahore")
# tup2 = (1,2,3,4,5,6,7)
# tup3 = tup2 + tup1
# new_tup = (tup3[7],tup3[8],tup3[9],tup3[0],tup3[1],tup3[2],tup3[3],tup3[4],tup3[5],tup3[6])
# print(new_tup)

# Method 5: Using List Comprehensions and Tuple Conversion

# tup1 = ("faisalabad","Jaranwala","Lahore")
# tup2 = (1,2,3,4,5,6,7)
# tup3 = tup2 + tup1
# result_list = [tup3[i] for i in range(7, len(tup3))] + [tup3[i] for i in range(7)]
# result_tuple = tuple(result_list)
# print(result_tuple)

