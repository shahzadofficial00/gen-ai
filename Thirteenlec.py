                                                                        # OOPS IN PYTHON

                                                     # there are two main things in OOP: class or object

                                          # SETTER OR GETTER METHOD

# class Employee:
#     # pass
#     def steEmp(self, name,age):
#         self.name = name
#         self.age = age
#     def getEmp(self):
#         print(f"{self.name}:{self.clsage}") 

# ab = Employee()
# ab.steEmp("akash",23) 
# ab.getEmp()   

                                                          # CONSTRUCTOR METHOD

# class Employee:
#     # pass
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#     def getEmp(self):
#         print(f"{self.name}:{self.age}") 

# ab = Employee("SHEZI",22) 
# ab.getEmp()  
# 
#                                                         POLYIMORPHISIM    

# class Car:

#     def __init__(self, name):
#         self.name = name

#     def func(self):
#         print(f"hello sky man {self.name}")    

        
# class Bus:

#     def __init__(self, name):
#         self.name = name

#     def func(self):
#         print(f"hello drown man {self.name}") 

# ab = Car("kia")
# ac =Bus("Daewo") 

# ab.func()
# ac.func()

  
# assignment 1

# class Sum:
#     # pass
#     def steEmp(self,a,b):
#         self.a = a
#         self.b = b
#     def getEmp(self):
#         print(f"{self.a + self.b}") 

# ab = Sum()
# ab.steEmp(15,20) 
# ab.getEmp()  


# assignment 2

# class Employee:
#     # pass
#     def __init__(self, name, age):
#         self.name = name
#         self.age = str(age)
#     def getEmp(self):
#         print(f"{self.name}: {self.age}") 
#         print(type(self.age))

# ab = Employee("SHEZI",22) 
# db = Employee("Hassan",23)
# cd =Employee("Zubair",33)
# ff= Employee("Ahmad",11)
# fd = Employee("Shahzaib",23)


# ab.getEmp()  
# db.getEmp()
# cd.getEmp()
# ff.getEmp()
# fd.getEmp()


# assignment 3


class Employee:
    # pass
    def __init__(self, *name):
        self.name = name
    def getEmp(self):
        print(f"{self.name[1] + self.name[1]}") 

ab = Employee(21,22,23,24) 
ab.getEmp() 

