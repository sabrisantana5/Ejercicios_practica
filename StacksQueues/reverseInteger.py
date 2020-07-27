#Reverses integers: 120 --> 12 , -38 --> -83
def reverse(x: int) -> int:
        stack = []
        negative = False
        if(x < (-2)**31 or x > (2**31 - 1)):
            return 0
        
        if(x<0):
            x = abs(x)
            negative = True
        x = str(x)
        
        s = ""
        for c in x:
            stack.append(c)
            
        if(negative):
            s += "-"
            
        while(len(stack)!=0):
            s += stack.pop()
            
        s = int(s)
        
        if(s < (-2)**31 or s > (2**31 - 1)):
            return 0
        return s

number = 210
res = reverse(number)
print(res)