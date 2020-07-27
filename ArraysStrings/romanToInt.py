#Transform roman number to integer
#number from 1 to 3999
def romanToInt(s: str) -> int:
        dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        salida = 0
        i = 0
        if(len(s)==1):
            salida = dict[s[len(s)-1]]
        while(i < len(s)-1):
            temp = ""
            temp = s[i]+s[i+1]
            if(temp in dict):
                salida += dict[temp]
                i+= 2
                if(i==len(s)-1):
                    salida += dict[s[i]]
            else:
                if(i+1==len(s)-1):
                    salida += dict[s[i]]
                    salida += dict[s[len(s)-1]]
                    i+= 1
                else:
                    salida += dict[s[i]]
                    i+= 1
        
        return salida
str2 = "MCMXCIV"
print(romanToInt(str2))