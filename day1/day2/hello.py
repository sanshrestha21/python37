
import numpy as np
def hello():
    print("Good Morning")
def name():
    print(input("Enter your name: "))
"""def inputstr():
    global data,number
    count=0.0
    number=0.0
    #print(input("Enter a number:"))
    #output_lines = []
    
    data=float(input("Enter a number or just ENTER to quit:") or 0)
    #list=[]
    #list=data.split()

    
    while data!=0:
        count+=1
        number=float(data)
        
        data=float(input("Enter a number or just ENTER to quit:") or 0)
        #list.append(data)
        
        #print(data)
       # print(number)

       # print(data)"""
def value1():
    list =[]
    number = int(input("how many value you want in a list: "))
    for i in range(0,number):    
        numbers = int(input("enter your choice number:"))
        list.append(numbers)
 
    print(list)
def add(list):
    #sum=0.0
    addition=int(np.add(list))
    print(addition)
    

name() 
hello()  
#inputstr()  
add(list) 
print(value1)