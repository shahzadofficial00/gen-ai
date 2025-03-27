                                                                # FUNCTIONS

# def c():
#     print("This is a function")                             # simple function
# c()


# def func(name, age):                                        # parameter
#     print("hello world " + name + str(age))
# func("Shahzad", 22)



# def func(name, *age):                                        # * arg arbitrary :
#     print(name + " " +  str(age[1]))
# func("Shahzad", 22,23)


# def func(**krgs):                                              # ** keyargument
#    print(krgs["name"]+ str(krgs["age"]))
# func(name= "shahzad", age=22)


# def fun():
#     pass                                                        # pass:- for clear the eror and start the next function

# fun()

                                                          # EXCEPTION HANDLING

# x =22
# try:
#     print(x)                                               # try and except 
# except:
#     print("error: varialble is not defined")
# finally:
#         print("this is always excuted")


                                                           # ANONYMOUS FUNCTION

# x = lambda a,b : a**b
# print(x(5,2))

# x = lambda a : a*4
# print(x(3))


# x = lambda a : a**4
# print(x(3))

# x = lambda a,b,c : a*(b/c)
# print(x(5,2,2))
 

# 1 ASSIGNMENT :  

# def fun():
#     city=["Lahore","Karachi","Islamabad","Multan","Sarghoda"]
#     user=input("Enter your city")
#     if user in city:
#         print("your city is clean: ")
#     else:
#         print("your city is not clean")
# fun()



# 1 ASSIGNMENT : part 2 : FLAG

# def fun(c):
#     alp = False
#     ls = ["Lahore","Faisalabad","Karachi","Multan","jaranwala"]
#     for city in ls:
#         if city == c:
#             alp=True
#     if (alp):
#         print("your city is clean: ")
#     else:
#         print("your city is not clean")
# c = input("Please enter your city")
# fun(c)



