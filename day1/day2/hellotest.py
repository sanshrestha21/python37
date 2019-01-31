"""def main():
    salesList = []
    salesvalue = float(input())
    while salesvalue < 0:
        salesvalue = float(input())
        if salesvalue == -1:
            break
    for i in range (5):
        salesList.append(salesvalue)
        salesvalue = float(input("yourmessage"))
    print (salesList)

main()"""
"""def function1():
    global a,b
    a=int(input("Enter any number\t"))
    b=int(input("Enter any number\t"))

def add(a,b):
    #s=0
    s=int(a+b)
    print ("this is the added number - ",s)
def sub(a,b):
    minus=int(a-b)
    print("this is subtracted value- ",minus)

function1()
add(a,b)
sub(a,b)"""
#main()
"""def makeList():
        salesList = []
        while True:
            salesValue = float(input('Please enter total sales in your department: '))
            if salesValue == -1:
                break        
            salesList.append(salesValue)
        #return salesList
        print(salesList)

print(makeList)"""
import numpy as np
list =[]
number = int(input("how many value you want in a list: "))
for i in range(0,number):    
    numbers = int(input("enter your choice number:"))
    list.append(numbers)
 
print(list)
def add():
    addition=np.sum(list)
    print(addition)
def mul():
    multiplication=np.prod(list)
    print(multiplication)
def sub():
    subtraction=np.diff(list)
    print(subtraction)
def maximum():
    maximum=np.max(list)
    print(maximum)
def minimum():
    minimum=np.min(list)  
    print(minimum)
add()
mul()
sub()
maximum()
minimum()
