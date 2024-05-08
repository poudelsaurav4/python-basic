# from openpyxl import Workbook

name = input("enter a name to add contact and enter contact number of the same person separate with comma: ")
a = name.split(',')
b = iter(a)
res = dict(zip(b,b))
print(res)

def add_to_contacts():
    pass

def update_to_contacts():
    pass

def del_from_contacts():
    pass