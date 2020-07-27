#Program that validates brackets without other characters
def brackets(s):
    stack = []
    dict = {"{":"}","(":")","[":"]"}
    count = 0
    if(len(s)<=1):
        return False
    for c in s:
        if c in dict:
            stack.append(c)
        else:
            if (c == dict[stack[-1]]): #ver si el que cierra corresponde al ultimo en stack
                stack.pop()
            else:
                return False
            
    if(len(stack)>0):
        return False
    return True
    
print(brackets("[{({})}]"))
print(brackets("[{(})}]"))
print(brackets("[]{}"))