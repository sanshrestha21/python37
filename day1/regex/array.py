#array=[2,15,18,19,21,30]
'''def min():
    minimum=sum(array)
    print (minimum) 

def max():
    maximum=max(array)
    print(maximum)

min()
max()'''
lst=[2,15,18,19,21,30]
def minmaxsum(lst):
    i = 1
    min = max = sum = lst[0]
    while i < len(lst):
        if lst[i] > max:
            max = lst[i]
        if lst[i] < min:
            min = lst[i]
        sum += lst[i]
        #if lst[i] / sum
         #   avg = lst[i]
        #i += 1
        avg=sum/len(lst)
        if lst[i]==15:
            print("match found")
        elif lst[i]==3:
            print("not matched")
        
        i +=1
        
    #return min, max, sum
    print(max)
    print(min)
    print(sum)
    print(avg)
    
#min, max, sum = minmaxsum(scores)
minmaxsum(lst)