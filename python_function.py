# def new_func():
#     print("this is my first function")

# new_func()

# def fun(arg_return):
#     print(arg_return)

# fun("hello argument")

# def train(fname, lname):
#     print(fname + " " + lname)

# train('ram', 'bahadur')

# def arb_fun(*name):
#     print( name)
# arb_fun(1, 'name is ram', 'ktm')

# list1 = [1,2,3,4,5]

# list2 = [lis for lis in list1 if lis %2 == 1]
# print(list2)

# names =["Ram", "shyam", "hari" , "gita"]
# namess = [name for name in names if 'R' in name]
# print(namess)


# def function_example(parameter_1, Parameter_2):
#     print("hi" + parameter_1, Parameter_2)

# function_example("Argument1", "arguement2")


# passing multiple argument in a single parameter
# def productFunction(*numbers):
#     total =1 
#     for number in numbers:
#         total*=number
#     return total

# print(productFunction(2,3,4,5))

# # passing key variable in a parameter as

# def multipleParameter(**country):
#     print(country)

# multipleParameter(name = "nepal", area = 8848,landmark = "everest")

# scope of a function


# Out_fun = "hi this is outside functio scope"
# def scope(name):
    # lName= "chau"
    # print(Out_fun)out function acts as global variable


    # print(lName) but it is under the scope of the function scope

# print(lname)  this is not under the scope of the function scope



# def FizzBuzz(input):
#     if (input % 5 == 0) and (input % 3 ==0):
#         return "FizzBuzz"
#     elif input %3 == 0:
#         return "Fizz"
#     elif input %5 == 0:
#         return "Buzz"

#     else:
#         return input

# print(FizzBuzz(15))


# def tarun(*, lname):
#     print(lname)

# tarun(lname= "shrestha")


# creating Split FUnction

# def SplitFunc():
#     splitValue = []
#     a = input("enter words to split:")
#     b = " "
#     temp = ""
#     for items in a:
#         if items == b:
#             splitValue.append(temp)
#             temp=""
#         else:
#             temp+=items
#     splitValue.append(temp)

#     return splitValue

# print(SplitFunc())



# def GreaterNumber():
#     aList = [32,55,7,6242,535,1,3,6]
#     aList.sort(reverse=True)
#     print(aList[:2])
    
# GreaterNumber()


# function for sorting items in list
# def SortList():
#     marks = [22,34,12,67,43]
#     for items in range(len(marks)):
#         for item in range(items+1, len(marks)):
#             if marks[items] > marks[item]:
#                 temp = marks[items]
#                 marks[items]=marks[item]
#                 marks[item]=temp

#     return marks
    

# print(SortList())

# def outer_function(a,b):

#     def inner_function(a,b):
#         return a+b
    
#     add = inner_function(a,b)
#     return add+5

# print(outer_function(5,5))


# def show_employee(name, salary=9000):
#     print(f"Name: {name} Salary: {salary}")

# show_employee("Saurav")


# def fNameLname(fname, middlename, lname=""):
#     print(f"My name is {fname} {middlename} {lname}")
#     # print(f"My name is {fname} {lname}")

# fNameLname("saurav", "pd", "poudel")
# fNameLname("saurav", "poudel")

# def numbers(a):
#     if a==50:
#         return 100
#     else:
#         return 50
    
# print(numbers(51))

# def numbers(a):
#     if a==50:
#         a+=50
#         print(a)
#     elif a==100:
#         a-=50
#         print(a)

# numbers(100)
# list2= [1,2,3,4,5]
# list3 = [3,5]
# list1 = [x for x in list2 if x%2==0  ]
# print(list1)


# recursive function 

# def factorial(n):
#     if n ==0:
#         return 1
#     return n* factorial(n-1)


# print(factorial(5))

# def fib(n):
#     if n < 1:
#         return "enter valid number"
    
#

# x = int(input("enter number of shoe that raghu has: "))
# y = []
# while len(y) < x:
#     numbers = int(input("enter number of shoe size: "))
#     y.append(numbers)

# for i in range(len(y)):
#     z = int(input("enter the number of size customer wants: "))
#     if z in y:
#         a = z * 25
#         print(f"the price of size {z} is {a}")
#     elif z not in y:
#         print(f"size {z} is not available in sotre")


# lambda Function 

# X= lambda x: x**2
# print(X(9))

# even_list = [lambda i: i for i in range(5)]
# for items in even_list:
#     print(items())

# list1 = ['2','b,' 3, 5 ,6,7]



# def check_palindrome(palindrome_c):
#     if len(palindrome_c)<1:
#         return True
#     else:
#         if palindrome_c[0]==palindrome_c[-1]:
#             return check_palindrome(palindrome_c[1:-1])
#         else:
#             return False
# palindrome = input("enter the input to check palindrome: ")
# if check_palindrome(palindrome):
#     print(f"{palindrome} is a palindrome")
# else:
#     print(f"{palindrome} is not a palindrome")

# a= "asaaaaaas"

# print(a[1:-1])


# fibonacci series

# n1,n2 = 0 ,1
# count = 0
# num = int(input("Enter Number to check fibonacci series upto: "))

# if num < 1:
#     print("enter valid positivie integer")
# elif num == 1:
#     print(f"fibonacci series of {num} is {n1}")

# else:
#     while count < num:
#         print(n1, end=' ')
#         n = n1+n2
#         n1 = n2
#         n2 = n
#         count+=1

# i = 0 


# while i < 10:
#     print(i, end=' ')
#     i+=1



# list_num = [4,6,7,3,5,7,8]

# def sort(list_num):
#     mul_list =[]
#     for i in list_num: 
#         mul_list.append()
#     return mul_list

# print(sort(list_num))


# # a = [lambda x: x for x in list_num]

# # print(list(a(list_num)))



# def filter_fun(list1:list, *num):
#     list2 = []
#     for items in list1:
#         list2.append(items)
#     for item in num:
#         list2.append(item)

#     return list2
# print(filter_fun([1,2,3,4,5],7,8,9,10))




# def new_function(a):
#     if a%2==0:
#         return True

# def old_function(b):
#     if b**2:
#         return True
    
# x = lambda x,y: x+y
# z=[1,2,3,4,5]

# c = [lambda d: i for i in z if i%2==0]
# print(new_function(z),z)



# z=[1,2,3,4,5]

# def even_checker(a):
#     x = []
#     for i in z:
#         if i%2==1:
#             x.append(True)

#         else:
#             x.append(False)

#     return x

# print(even_checker(z))

# x = list(filter(lambda x: x*2, z))

# y = list(map(lambda x: x%2 == 0, z))


# print(y)



    



rows= 5

# for i in range(x):
#     for j in range(i + 1):
#         print('*', end= ' ')
#     print('')
# j=0   

# for i in range(1, rows):
#     for s in range((rows-i)):
#         print(end = ' ')
#     j=0
#     while j < ((2*i)-1):
        
#         print("*", end='')
#         j+=1

#     print()



# x = {
#     "a":1,
#     "b":5,
#     "c":4
# }
# z= list(x)
# print(sorted(z, reverse=True) )

# # for i in range(len(x)):
    
dicto1 ={
    'a':1,
    'b':2,
    'c':3
}
dicto3 = {
    'a':2,
    'd':3,
    'c':4
}
list1 = ['l','m','n','j']
# for k,v in dicto1(key, value):
#     dicto1[v] = list(v)
# print(value)

# z=list(zip(x,list1))
# print(z)
# dict2 = [i for i in dicto1 zip(dicto1[i],list1)]
# dict2 = list(zip(dicto1, list1))

# dict3= dict(zip(dicto1, dicto3))
# print(dict3)
# keys = []
# for i in dicto1:
#     for j in i:
#         keys.append(j)

# print(keys)
# li2= []
# list3=[]
# for i,j in dicto1.items():
#     li2.append(j)
#     list3.append(i)

# li3 = list(zip(li2, list1))


# dict3 = dict(zip(list3,li3))

# print(dict3)


# main_dict= dicto1  dicto3
# print(main_dict)

# def CombineDict(*dicr):
#     result ={}
#     for i in dicr:
#         for key in (result.keys() | i.keys()):
#             if key in i:
#                 result.setdefault(key, []).append(i[key])
#     return result
# print(CombineDict(dicto1, dicto3))
# keys = []
# Result= {}
# for i in dicto1,dicto3:
#     for key in i:
#         if key not in keys:
#             keys.append(key)

# print(**dicto1, **dicto3)