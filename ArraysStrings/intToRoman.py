def intToRoman(num: int) -> str:
        roman = ""
        dict = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L", 40:"XL", 10:"X",9:"IX",5:"V",4:"IV",1:"I"}
        while(num>0):
            noencontrado = True
            if num in dict:
                return roman + dict[num]
            else:
                for element in dict:
                    if(element<num and noencontrado):
                        num -= element
                        roman += dict[element]
                        noencontrado = False
        return roman
print(intToRoman(1999))