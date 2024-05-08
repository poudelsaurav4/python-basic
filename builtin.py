# print(abs(-1.232342341212))

# print(abs(3-3j))


# print(ascii("a"))

# print(bin(24232))

# print(bin(9))
# x = 1
# print(bool(x<0))

# def func():...
# l1 = {}

# print(bytearray(l1))
# print(type(l1))
# print(callable(l1))

# print(callable(func))

# print(chr(95))

# x = compile('print(55+98*5)', 'test', 'eval')
# exec(x)


# delattr() to delete attribute from class

# class Aayu:
#     name = "logic"
#     location = "patan"

# ob1 = Aayu()
# delattr(Aayu, 'location')
# print(ob1.name, ob1.location)


# print(divmod(9,100))
# x = "apple", "ball", "cat"
# print(list(enumerate(x)))

# x= input("enter funtion in term of a ")

# a = int(input("enter the vlaue to pass in expression: "))

# print(eval(x))

# class Calculation:
#     def add(self,a,b):
#         return a+b
    

# calc = Calculation()

# x = getattr(calc, "add")
# print(x(4,5))

# class Name:
#     naf = 'hi'

# x = Name()
# setattr(x, 'name', 'saurav')
# setattr(x, 'location', 'sitapaila')

# print(isinstance(x, Name))
# print(hasattr(Name, 'naf'))
# print(x.name, "lives in ", x.location)


# x = 2

# print(help(x))

# x = 1
# y=x
# print(id(1))
# print(id(x))
# print(id(y))

# print(hex(1793))

# print(ord("H"))


# iter_toools

import itertools
import operator

l1= [1,2,3,4,5]
l2= [2,3,4,5,6]

# a, b, c, d, e = map(operator.mul, l1, l2)

# print(a,b,c,d,e)

# a, b, c, d, e = map(operator.add, l1,l2)

# print(a,b,c,d,e)

# a, b, c, d, e = map(operator.mod, l1,l2)

# print(a,b,c,d,e)

# for numbers in count(start=10, step=2):
#     if numbers>99:
#         break
#     print(numbers)

# for i in itertools.count(2,2):
#     if i==20:
#         break
    
#     else:
#         print(i, end=' ')
# count=0
# for i in itertools.cycle('ABC'):
#     if count > 100:
#         break
#     else:
#         print(i, end = " ")
#         count+=1
# itt = itertools.cycle(l1)
# for i in range(100):
#     print(next(itt), end=' ')


# print(list(itertools.repeat(100,182)))

# from itertools import combinations
# from itertools import permutations
# print(list(combinations([l1,l2],2)))
# print(list(combinations('abc'),2))

# l3= [l1,l2]
# print(list(itertools.chain.from_iterable(l3)))


# from collections import Counter

# l1 = [1,2,3,4,4,2,2,3,1,3,4,1,2,3,2,1,2,2]
# print(Counter(l1))

  
#   assert keyword

# a = 5
# b=8
# assert a>b , "a is smaller than b"

# print(a+b)


# def area_reactangle(x,y):

#     assert x>0 and y>0, "length and width should be positive"
#     area = x*y

#     return area

# print(area_reactangle(-2,-5))


# for i in l1:
#     assert i<=5, "not ok"
#     print(f"{i}, ok")

# generating random without random

# import time

# start_range = 5
# end_range = 15


# a = int(time.time())

# random_number = (a % (end_range - start_range + 1)) + start_range

# print(random_number)

n=3
s = ''
for i in range(1,n):
    s+=i
print(s)