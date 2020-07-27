#Check valid anagram (string)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        
        if len(s) != len(t):
            return False
        
        for x in s:
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] += 1
                
        for x in t:
            if x not in dict or dict[x]<1:
                return False
            else:
                dict[x] -= 1
        return True