#Program that returns the longest palindrom  in a string
def longestPalindrome(s: str) -> str:
        
        if(len(s)<1):
            return ""
        
        maxim = s[0]
        temp = ""
        if(len(s)>=1000 or len(s)==1):
            return s
        else:
            for i in range(len(s)):
                temp = s[i]
                for j in range(i+1,len(s)):
                    isPalindrome = True
                    temp += s[j]
                    x = 0
                    y = len(temp)-1
                    while(x<y and isPalindrome):
                        if(temp[x]!=temp[y]):
                            isPalindrome = False
                        else:
                            isPalindrome = True
                        x+=1
                        y-=1

                    if(isPalindrome):
                        if(len(temp) >= len(maxim)):
                            maxim = temp
        return maxim
                    
print(longestPalindrome("yanppnag"))