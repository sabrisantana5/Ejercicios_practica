#Program that rotates an array x times to the left
def rotateArrayLeft(array,x):
    stack = []
    for c in range(x): #i think 1 to 3
        stack.append(array[0])
        for i in range(len(array)-1):
            array[i] = array[i+1]
        array[len(array)-1] = stack.pop()
    return array
        
        
    
   
array = [1,2,3,4,5]
x = 3
print(rotateArrayLeft(array,x))
# [4,5,1,2,3]