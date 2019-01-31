f= open("employee.txt","w+")
'''name=[sandeep,sohil,sachin]
t=[[salary,increament],[]]
t=[[name,salary,increament],[45000,25000,20000],[5,8,15]]

for r in t:
    for c in r:
        print(c,end = " ")
print()'''
list_of_lists = []
for row in range(rows):
    inner_list = []
    for col in range(cols):
        inner_list.append(None)
    list_of_lists.append(inner_list)
