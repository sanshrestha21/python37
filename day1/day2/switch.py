number=0.0
count=0.0
numbers=0.0
xnum=0.0


data=float(input("Enter a number or just ENTER to quit:") or 0)
while data!=0:
    
    count+=1
    number=float(data)
    data=float(input("Enter a number or just ENTER to quit:") or 0)
    numbers=(number ** data)
    print(numbers)