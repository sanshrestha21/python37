count=0.0
Sum=0.0
average=0.0
numbers=0.0
xnum=0.0
#mul=0.0
data=float(input("Enter a number or just ENTER to quit:") or 0)
Min=data
Max=data

while data!=0:
    
    count+=1
    number=float(data)
    mul=number*number
    Sum+=number
    average=Sum/count
    
    

    if data<Min:
        Min=data
    if data>Max:
        Max=data
    sub=Max-Min
    pow=(number**data)
    
    data=float(input("Enter a number or just ENTER to quit:") or 0)
#for x in range(data):
 #       numbers=(numbers*xnum)
  #      #return numbers
   #     print(numbers)


print(count,("numbers entered."))
print("Sum:",Sum)
print("Average:",average)
print("Min:",Min)
print("Max:",Max)
print("subtraction:",sub)
print("multiplication:",mul)
print("power:",pow)