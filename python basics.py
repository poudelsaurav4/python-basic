# print("hello")

# IF else condition 
# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird


# import math
# import os
# import random
# import re
# import sys
# n = int(input().strip())
    
# if n%2 == 1:
#     print("Weird")
# elif n%2 == 0 and n< 5:
#     print("Not Weird")
# elif n%2 == 0 and 6 <= n <= 20 :
#     print("Weird")
# elif n%2 == 0 and  n > 20 :
#     print("Not Weird")


# Calculate angle of triangle




# import math
# a = int(input("enter AB: "))
# b= int(input("enter BC: "))

# c = math.sqrt(a**2 + b**2)


# sine_value = b/c

# degree = math.degrees(math.asin(sine_value))
# print(round(degree))


# n = int(input())

# for i in range(n):
#     i = i**2

#     print(i)


# program to check if the year is leap or not 

# def is_leap(year):
#     leap = False
    
#     # Write your logic here
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#     return leap

# year = int(input())
# print(is_leap(year))


# def myFunc():
#     print("Hello, My name is Saurav")

# myFunc()


# def Func_arg(Lastname):
#     print("Saurav " + Lastname)

# Func_arg("Poudel")

# b = "I don't love football"

# A = a.split()
# B = b.split()

# common = []
# diff = []
# print("football" in A)

# for i in B:
#     if i in A:
#         common.append(i)
#     else:
#         diff.append(i)

# print(common)
# print(diff)

# Creating split 
# a = "I,love,football"

# split_val = []
# temp = '' 
# y = ','
# for items in a:
#     if items == y:
#         split_val.append(temp)
#         temp=''
#     else:
#         temp += items
        

# split_val.append(temp)
# print(split_val)

# Sets 

# new_sets = {"sa", "sasasa", "sasa", "sa"}
# print(new_sets.pop())

# newew_sets = {1,2,3}
# new_li = [9,8,7]
# # print(len(new_sets))

# # for items in new_sets:
# #     print(items)

# # print("sa" in new_sets)
# # new_sets.update(new_li)
# # for items in new_sets:
# #     x = new_sets.pop()

#     # print(x)
# print(new_sets)


# new_set = {'1',2,3}
# neww_set = {5,6,2,3}
# # new_set.remove(3)
# # print((new_set))

# set3 = neww_set - new_set
# print(set3)

# Y = dict()
# print(type(Y))
# dict = {}
# Y = dict()
# print(type(Y))

# new_dict = {
#     "name": "Saurav",
#      "last": "poudel",
#      "address": "Kathmandu",
#      "contact": 12345
# }

# new_dict.update({"name":"noname"})
# new_dict.update({"color":"black"})
# new_dict.pop("address")
# new_dict.popitem()

# for items in new_dict:
#     # print(items)
#     print(new_dict[items])


# nested_dict = {
#     "geography":{
#         "area":"plain",
#         "region":"north",
#         "land":"locked"
#     },

#     "country":{
#         "name":"Mongolia",
#         "area": 123184,
#         "president": "mr mongolia"
#     }
# }

# print(type(nested_dict))

# for items in nested_dict:
#     print(nested_dict[items])

# for i, obj in nested_dict.items():
#     for j in obj:
#         print(j, obj[j])

# nested_dict.update({"country":{"model":"china"}})
# print(nested_dict)

# nested_dict["country"]["model"]= "china"
# nested_dict["geography"]["Highest peak"] = '2000m'

# print(nested_dict)

# convertibg two list into dictonaries

# keyss = ['name', 'location', 'phone']
# valuess = ['sp', 'ktm', 98724987]

# new_dictonary= {}

# for i in range(len(valuess)):
#     new_dictonary[keyss[i]]= valuess[i]

# new_dictonary2 = {i:j for i,j in zip(keyss, valuess)}
#     # print(valuess[i])
# # new_dictonary['lname']='poudel'
# print(new_dictonary)
# print(new_dictonary2)
# list1 = [1,2,3]
# list2 = [3,4,4]
# print(list1+list2)


# name = ['saurav', 'tarun']
# caste = ['poudel','shrestha']
# fname= [name[0]+ ' ' +caste[0] + ', ' + name[1]+ ' ' +caste[1]]
# print(fname)


# x = zip(name, caste)
# # list(x)
# print(set(x))

# x= ['m', 'na', 'i', 'ra']
# y = ['y', 'me', 's', 'm']my n

# x = input("Enter sentence")
# lis = x.split()
# print(lis)

# temp = ""
# for i, j in list(zip(x,y)):
#     temp += ' ' + i+j
#     # print(i+j)
# print(temp)

# for i in range(1,100):
#     if i % 3 == 0:
#         print(i, 'hello')
#     elif i%5 == 0:
#         print(i, 'world')
#     else:
#         print(i, "hello world")

# x = range(5)
# print(x)
# names = "Saurav Poudel"
# print(names[::-1])
# names = "".join(reversed(names))
# print(names)
# print(names[1:-5])

# list1 = list(names)

# list1[0]='g'
# names ="".join(list1)
# print(type(names))

# string / raw string used to use escape sequence

# string1 = r"hello \this is saurav\123\34"

# print(string1)

# keys =['name', 'age']
# values = ['saurav', '20']
# dicto= {}

# for i in range(len(keys)):
#     dicto.update({keys[i]:values[i]})
#     # print(i)

# print(dicto)

# s= zip(keys,values)
# dict1 = dict(s)
# print(dict1)

# print(set(zip(keys,values)))

# dict_1 = {
#     "name": "saurav",
#     "age": 20
#     }
# dict_2={
#     "address":"Sitapaila",
#     "contact":11111
# }

# # dict_3 = dict_1.copy()
# # dict_3.update(dict_2)
# # print(dict_3)
# y = {**dict_1, **dict_2}
# print(y)

# x = 5
# print(complex(x))

# listDuplicate = [1,2,3,2,3,4,5]
# temp = []
# dup = []
# for items in listDuplicate:   
#     if items not in temp:
#         temp.append(items)
#     elif items not in dup:
#         dup.append(items)
# print(dup)

# tupleEx = ("ss", "sa", "sasa")
# tupleEx.append("sssss")
# print(tupleEx)
# (*s,sss) = tupleEx
# print(s)
# print(sss)
# # print(ssss)

# def newFun(x = "x", y=15):
#     print(x,y)
    
# newFun("y", y = 20)

# def positionKeyword(a,b,c,/,*,e,f,g):
#     print(a,b,c,e,f,g)

# positionKeyword(1,2,3,e=1,f=2,g=1)

# exSet = set()
# exsetElem = {1,2,3,4}
# print(list(exsetElem))

# listEx = [1, "sp", 0]
# print(set(listEx))





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




x = {
    "a":1,
    "b":4,
    "c":2,
    "d":7,
    "e":3
}

# res = {k:v for k,v in x.items() if v < max(x.values())}
# res2 = {k:v for k,v in x.items() if v == max(x.values())}
# y = print(res | res2)


res = {}
while x:
    min_key = max(x, key=x.get)
    res[min_key] = x.pop(min_key)
print(res)


# print(x)
# print(res2)
# print(res)
# values = []
# keys= []
# for i in x:
#     # print(x[i])
#     values.append(x[i])
#     keys.append(i)

# for j in range(len(values)):
#     for k in range(j+1, len(values)):
#          if values[j]>values[k]:
#              a= values[j]
#              values[j]=values[k]
#              values[k]=a
# print(dict(zip(keys,values)))
# print(values)
    

# def f1(val):
#     y = x[val]
#     print(y)
#     print(val)
#  x = {'a':1,'c':2}
# print(sorted(x.items(), key = lambda ab: ab[1]))

# sorted_x= {}
# for key in sorted(x, key = x.get):
#     sorted_x[key]= x[key]
# print(sorted_x)


# def filter_function(function1, iterables1):
#     even_numbers=[]

#     for i in iterables1:
#         if function1(i):
#             even_numbers.append(i)
#     return even_numbers
    
# numbers =[1,2,3,4,5,6,7,8,9,10]

# eveNum = filter_function(lambda x: x%2 ==0, numbers)
# print(eveNum)

