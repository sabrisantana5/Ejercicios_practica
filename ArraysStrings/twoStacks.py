#How many things you can get out of the stack before it
#is greater than 10
def twoStacks(x, a, b):
    counter = 0
    suma = 0
    a.reverse()
    b.reverse()
    while(suma < x):
        if(a[-1] + suma < x):
            suma += a.pop()
            counter += 1
        elif(b[-1] + suma < x):
            suma += b.pop()
            counter += 1
        else:
            return counter
a = [4,2,4,6,1]
b = [2,1,8,5]
x = 10
print(twoStacks(x,a,b))