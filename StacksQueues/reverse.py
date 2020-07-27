#Program that reverses strings through stacks
def reverse(s):
    stack = []
    answer = ""
    for c in s:
        stack.append(c)
    for c in s:
        answer += stack.pop()
    return answer
s = "sabrina"
print(reverse(s))

#Program that reverses sentences
def reverseSentence(s):
    stack = []
    answer = ""
    s2 = s.split() #O(n)
    for c in s2: #O(n)
        stack.append(c)
    for c in s2: #O(n)
        answer += stack.pop() + " "
    return answer
s = "sabrina is happy"
print(reverseSentence(s))
#Complexity o(3n)

        