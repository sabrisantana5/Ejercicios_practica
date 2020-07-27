#Program that transforms a string in zig zag and returns
#the result
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        dict = {} #de strings
        contador = 0
        booleana = False
        res=""
        if(numRows==1):
            return s
        
        for i in range(numRows):
            dict[i] = ""
        for letra in s:
            dict[contador] += letra
            if(contador == numRows-1):
                booleana = True
            if(contador == 0):
                booleana = False
            if(booleana):
                contador -= 1
            else:
                contador += 1
        for i in range(numRows):
            res+=dict[i]
        return res
sol = Solution()
s= "paypalishiring"
print(sol.convert(s,3))