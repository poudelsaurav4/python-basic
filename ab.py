# l1 = [1,2,3,4,5,2,1,2,4,5,4,5,1,2,3,2,4,2]


# d1={}
# for item in l1:
#     if item in d1:
#         d1[item] += 1
#     else:
#         d1[item] = 1

# print(d1)


# l1=[]
# l2=[]

# l2=[1,2,9,4,5]
# a = {item: len([x for x in l1 if x == item]) for item in set(l1)}
# print(a)
# res = {}
# for key in set(l1):
#     for value in l2:
#         res[key] = value
#         l2.remove(value)
#         break
        

# print(res)


def names(x,y):
    x_dict = {}
    y_dict = {}

    for char in x:
        if char in x_dict:
            x_dict[char] += 1
        else:
            x_dict[char] = 1

    for char in y:
        if char in y_dict:
            y_dict[char] += 1
        else:
            y_dict[char] = 1

    if x_dict == y_dict:
        print("same.")
    else:
        print("not same.")
    

names('ass','sss')

