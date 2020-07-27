def checksIfRotated(s1,s2):
    if(len(s1) == len(s2)):
        s1 += s1
        if s2 in s1:
            return True
       
    return False
    
        
    
s1 = "string"
s2 = "ingstr"
s3 = "gnirts"
s4 = "strin"
print(checksIfRotated(s1,s2))
print(checksIfRotated(s1,s3))
print(checksIfRotated(s1,s4))