#Program that determines if a number is a palindrome
class Solution:
    def isPalindrome(self, x: int) -> bool:
        stack = []
        x = str(x)
        
        for c in x:
            stack.append(c)
        for c in x:
            if(c != stack.pop()):
                return False
        return True
    
''' #Another simpler way
def isPalindrome(self, x: int) -> bool:
    return str(x) == str(x)[::-1]'''