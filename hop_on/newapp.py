import math
# item = ['momo','chowmen','choila','chatamari','friedrice','thukpa']
# price = [100,120,80,150,120,120]
# sold = [20,15,5,8,10,15]
# expected = [30,20,10,15,15,10]
# outstock = [0,0,0,0,0,5]

dataset = [
    ['momo',100,20,30,0],
    ['chowmen',120,15,20,0],
    ['choila',80,5,10,0],
    ['chatamari',150,8,15,0],
    ['friedrice',120,10,15,0],
    ['thukpa',120,10,10,0]
]


total=0
sales_report=[]
prep_next_day=[]
for i,data in enumerate(dataset):
    name,price,sold,expected=data[:4]
    coll=price*sold
    expected_coll=price*expected
    diff=expected_coll-coll
    sales_report.append((name,price,sold,coll,expected_coll,diff))
    qty=math.ceil(sold + ((expected * 15)/100))
    mid=expected/2
    if(sold<=mid):
        qty=mid + math.ceil(expected * .25)
    prep_next_day.append((name,expected,sold,sold-expected,qty))

print(prep_next_day)


