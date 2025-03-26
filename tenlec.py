# Today topic is DICTIONARIES
# CRUD : C: CREATE R: READ U:UPDATE  D: DELETE              MIT

# dic = {"name":"shahzad"}
# dic = dict(({"name":"shahzad","age":22}))               # CONSTRUCTOR :-we se curly braces for dictionary
# print(type(dic),dic,len(dic))
# print(dic["name"])
# print(dic.get("name"))                               
# dic["name"] = "hassan"                                  # value cahnged method
# dic["color"] = "blue"                                   # add new things and update method ADD ONE VALUE
# dic.update({"color":"green","alpha":"1.09"})            #  ADD MULTIPLE VALUES : new update method and direCt method 
# dic.pop("alpha")                                        # remove method
# dic.popitem()                                           # remov last key 
# print(dic.keys())                                       # find keys and find  how many keys
# print(dic.values())                                     # find values
# print(dic.items())                                      # find items
# del dic["name"]                                         # delete any key and value
# dic.clear()                                             # clear all values and keys

# print(dic)


                                                            # new topic
                                        # pass by reference / pass by value : mit of interview

# pass by value
# primitive data types

# a = 10
# b = a
# a = 20
# print(a, b)

# pass by refernce
# non primitive data types

# dic1 = {"name":"shahzad","age":"22"}
# dic2 = dic1

# dic1["name"]= "adil"
# print(dic1, dic2)

                                                                   # Copy DICTIONARY

dic1 = {"name":"shahazad", "age":22}
# dic2 = dic1.copy()
# dic2 = {"name":"hassan", "age":22}
dic2 = dict(dic1)                                                 # constructor 
dic1["name"] ="adil"
print(dic1,dic2)