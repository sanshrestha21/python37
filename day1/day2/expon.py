"""def main():
    numbers=[1,2,3,4,5,6,7,8,9]
    numbers3=power(numbers[:])
    print('Original list:', numbers)
    print('Cubic list:', numbers3)
main()"""
numbers=[4,2]
numbers3 = []
for n in numbers:
    numbers3.append(n**n)
print('Original list:', numbers)
print('Cubic list:', numbers3)