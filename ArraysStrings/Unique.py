#Determines if all characters in a string are unique.
#O(n^2)
def problem1(s):
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                return False
    return True

#O(n) 
def problem1dict(s):
    dict={}
    for c in s:
#ves si la letra está en el diccionario
        #buscar y añadir son constantes lineales
        if c in dict:#dict.buscar(c) == True: 
            return False
        dict[c] = 1 #mete el string en el dicc
    return True

str = "SALSA"
str2 = "HOLA"
print(problem1(str))
print(problem1dict(str2))