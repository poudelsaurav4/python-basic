# class Fruits:
#     f_name = "Apple"

# obj1 = Fruits()
# print(obj1.f_name)



# def fibo(number):
#     n1,n2 = 0,1
#     count = 0
#     num = 0
    
#     if number <1:
#         print("please enter valid positive integer")
#     elif number ==1:
#         print(f"Fibonacci of {number} is {n1}")
#     else:
#         while count < number:
#             print(num, end = ' ')
#             num = n1+n2
#             n1= n2
#             n2=num

#             count += 1

# fibo(9)

# x = [1,2,3,4,5]
# # # y = [i for i in x if i > 3]

# # # print(y)
# def new_func(a):
#     if a >3:
#         return True

# # y = lambda a : a > 3
# # # print(y(4))

# z = filter(new_func,x)
# print(list(z))

# # # a = lambda a, b: a+b
# # print(a(2,3))


# class Person:
#     name = "Ram"
#     occupation = "intern"
#     age =20
#     def info(self):
#         print(f"{self.name} is {self.age} years old")

# ob1 = Person()
# # ob1.name = "Hari"
# # print(ob1.name)
# ob1.info()



# class Person2:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f"{self.name} is {self.age} years old")

#     # def __init__(self):
#     #     self.info = info
#     #     print(f"")

# a = Person2("hari", 26)
# a.info()



# class AayuLogic:
    # def __init__(self,name,location,employeeId,workHours):
    #     self.name = name
    #     self.location = location
    #     self.employeeId = employeeId
    #     self.workHours = workHours
    
    # def Employee(self):
    #     print(self.name,self.location,self.employeeId,self.workHours)
    

# a = AayuLogic("hari","patan",2,8)
# a.name = "ram"
# a.location = "Kathmandu"
# a.employeeId = 1
# a.workHours = 9


# class Vehicals:
#     def __init__(self,name,brand,Cc):
#         self.name = name
#         self.brand = brand
#         self.Cc = Cc
    
#     def Seating_capacity(self, Seat_cap):
#         print(f"The seating Capacity of a {self.name} is {capacity}")

# obj1 = Vehicals("santrao","hyundai",1100)
# print(obj1.brand,obj1.Cc)
# a.Employee()


# class without any variables and methods

# class Laptop:
#     pass


# class Bus(Vehicals):
#     pass
# obj2 = Bus("Thulobus","Tata",9000)

# print(obj2.name,obj2.brand,obj2.Cc)

# class Car(Bus):
#     pass

# obj3 = Car("Jimny","suzuki",1600)

# print(obj3.name,obj3.brand,obj3.Cc)



# class Vehicals:

#     color= "white"
#     def __init__(self,name,brand,Cc):
#         self.name = name
#         self.brand = brand
#         self.Cc = Cc
    
#     def Seating_capacity(self, capacity):
#         print(f"The seating Capacity of a {self.name} is {capacity}")


# class Bus(Vehicals):
#     def Seating_capacity(self, capacity):
#         return super().Seating_capacity(capacity)

# obj1 = Bus("THulobus","Tata",19000)

# print(obj1.Seating_capacity(50))



# class Car(Vehicals):
#     def Seating_capacity(self, capacity):
#         return super().Seating_capacity(capacity)
# obj2 = Car("sanoCar","hyundai", 1209481)
# print(obj2.Seating_capacity(4))






# class Animal:
#     def __init__(self,animal_class, group, vore, bone, fly):
#         self.animal_class= animal_class
#         self.group = group
#         self.vore = vore
#         self.bone = bone
#         self.fly = fly
    
#     def Animal_c(self):
#         print(f"{name} is  under {animal_class}")
    
#     def flight(self):
#         print(f"{name} can fly")
    
#     def eat(self):
#         print(f"{name} is {vore}")


# class Amphi(Animal):
#     def Bone(self):
#         print("amphi donot have bone")




# Polymorphism / method over riding

# class Animal:

#     def EatMeat(self):
#         print("Many of the animal eats meat")

#     def GiveBirthDirectly(self):
#         print("many of animal give birth directly")

# class Cow(Animal):

#     def EatMeat(self):
#         # return super().EatMeat()
#         print("Cow Donot eat meat")
#     def GiveBirthDirectly(self):
#         print("cow give birth directly")

# class Dinasours(Animal):

#     def EatMeat(self):
#         # return super().EatMeat()
#         print("dinasours eats meat")
    
#     def GiveBirthDirectly(self):
#         # return super().GiveBirthDirectly()
#         print("dinasours lays eggs")


# obj1= Animal()

# obj_cow = Cow()
# obj_dinasours = Dinasours() 

# obj_cow.EatMeat()
# obj_cow.GiveBirthDirectly()

# obj_dinasours.EatMeat()
# obj_dinasours.GiveBirthDirectly()


# Method overLoading

# def MethodOverLoading(datatype, *args):

#     if datatype == 'int':
#         res = 0
    
#     elif datatype =='str':
#         res = ''
#     for i in args:
#         res+=i
#     print(res)
    
# print(MethodOverLoading('int', 4,5))
# print(MethodOverLoading('str', "hello", "world"))


# class Parents():
#     def __init__(self,name, depart):
#         self.name = name
#         self.depart = depart
    
#     def EmployeeInfo(self):
#         # print(f"He\she is  {self.name} working on {self.depart}")
#         print(f"hello{self.name}, {self.depart}")

    
# class Childe(Parents):
#     def EmployeeInfo(self):
#         print(f"hello{self.name}, {self.depart}")
#         # pass
    
# obj2 = Childe("Saurav","Development")
# # obj1 = Parents("sp","dep")
# print(obj2.EmployeeInfo())


# class BaseClass():
#     def __init__(self,name) -> None:
#         self.name = name

# class BaseClassNext():
#     def __init__(self,lastname) -> None:
#         self.lastname = lastname
    

# class DerrivedClass(BaseClass, BaseClassNext):
#     def __init__(self,name,lastname) -> None:
#         BaseClass.__init__(self,name)
#         BaseClassNext.__init__(self,lastname) 
        
    
#     def printStrings(self):
#         print(f"hello,{self.name} {self.lastname} ")



# obj1 = DerrivedClass("saurav", "poudel")
# print(obj1.printStrings())



# class MainParent():
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
    
# class SecondParent(MainParent):
#     def __init__(self, num1, num2):
#         MainParent.__init__(self,2,3)
#         self.num1 = num1
#         self.num2 = num2
    

# class Child(SecondParent):
#     def __init__(self):
#         SecondParent.__init__(self,9,11)
    
#     def printResult(self):
#         print(self.num1+self.num2)


# ob1 = Child()
# print(ob1.printResult())


# def add(typ, a,b):
    
#     if typ== str:
#         x =''
#     elif typ== int:
#         x = 0
#     x= a+b
#     print(x)

# print(add("str","hello","world"))
# print(add("int",2,5))



class Bird():
    def fly(self):
        print("Birds do fly")
    

class Ostrich(Bird):
    def fly(self):
        print("Ostrich, They run")

class Penguin(Bird):
    def fly(self):
        print("penguin, They Swim")

class Parrot(Bird):
    def fly(self):
        print("parrot, They fly")


birds = [Ostrich(), Penguin(), Parrot()]

for bird in birds:
    print(bird.fly())