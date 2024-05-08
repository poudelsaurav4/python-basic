# def hello_decorator(func):
# 	def inner1(*args, **kwargs):
		
# 		print("before Execution")
		
# 		returned_value = func(*args, **kwargs)
# 		print("after Execution")
		
# 		return returned_value
		
# 	return inner1

# @hello_decorator
# def sum_two_numbers(a, b):
# 	print("Inside the function")
# 	return a + b

# a, b = 1, 2
# print("Sum =", sum_two_numbers(a, b))

def dec_fun(func):
    def min_max(x, y):
        if x > y:
            return x
        else:
            return y

    def pass_val(a, b):
        # res = func(a, b)
        return min_max(a, b)

    return pass_val

@dec_fun
def minmax(a, b):
    return (a, b)

result = minmax(5, 10)
print(f"Result: {result}")

# def vals(c,d):
#     return (c,d)

# print(vals(34,32))



def dec1(func):
    def retName(name,lname):
        return name+ lname
    
    def passname(a,b):
        return retName(a,b)
    
    return passname

@dec1

def myname(a,b):
    return a,b

print(myname("saurav","difygdsifus"))
    