# Two words can be chained if the last character of the first word
#  the same as the first char of the second word
#Check if all words can be chained in a circle
def chainedArray(words):
    dict = {}
    for c in words:
        dict[c[0]] = c[-1]
    for c in dict.values():
        if c not in dict:
            return False
    return True
        

words = ["eggs","karat","apple","snack","tuna"]
print(chainedArray(words))
