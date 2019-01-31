n=2
m=3
multiply=0
def exponent(a, b):

    num = 1
    for i in range(b):
        num = multiply(num, a)
    return num

print(exponent(n, m))