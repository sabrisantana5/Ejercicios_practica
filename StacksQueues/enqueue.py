#Program that implements queues using stacks
def enqueue(element): #of a string
    stack.append(element)
def dequeue():
    stack2 = []
    while(len(stack)!=0):
        stack2.append(stack.pop())
    x = stack2.pop()
    while(len(stack2)!=0):
        stack.append(stack2.pop())
    return x
stack = []
print("1 in")
enqueue(1)
print("2 in")
enqueue(2)
print("3 in")
enqueue(3)
print("first out (1)")    
dequeue()
print("first out (2)")   
dequeue()
print("Elments remaining")
for i in stack:
    print(i)

    
