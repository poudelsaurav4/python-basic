import openpyxl

from openpyxl import Workbook



path_excel = 'git.xlsx'

wb = Workbook()

ws = wb.active
# ws_write = wb.create_sheet(0)
# res={}
x=  [1,2,3,4,5]
y = [2,3,4,5,6]


# for i in x:
#     ws_write.append(i)
# res = {x[i]: y[i] for i in range(len(x))}

# print(res)
# ws.append(res)


# a = {
#     1:"a",
#     "b":2
# }
# z= []
# for i in a:
#     z.append(i)

# ws.append(z)

# ws.append(a)

for row in x:
    ws.append(row)


wb.save('git.xlsx')
