#Program that adds two linked lists that represent 2 numbers
#Lists must have same size
class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None
    
class SumLists:
    def problem2(L1,L2) -> ListNode:
        carry = 0
        while(L1 != None and L2 != None):
            L1.value += L2.value + carry
            # // is floor division
            carry = L1.value // 10 #para saber si la suma es mayor a 9
            if(carry >= 1):
                L1.value -= 10
            L1 = L1.next
            L2 = L2.next
        return L1

LN = ListNode(2)
LN.next = ListNode(4)
LN.next.next = ListNode(3)
LN2 = ListNode(5)
LN2.next = ListNode(6)
LN2.next.next = ListNode(4)
Answer = SumLists()
SumLists.problem2(LN,LN2)
print(LN.value)
print(LN.next.value)
print(LN.next.next.value)



'''
Same problem for different sized lists
def problem2solution(L1,L2):
    while(L1 != None or L2 != None):
        carry = 0
        if(L1 != None):
            val1 = L1.value
        else
            val1 = 0
            
        if(L2 != None):
            val2 = L2.value
        else
            val2 = 0
        
        val1 + val2
        #no está terminado, hay que hacer una nueva lista y meter ahi los valores 
            
        carry = L1.value%10 #para saber si la suma es mayor a 9
        if(carry >0):
            L1.value -= 10
    L1 = L1.next
    L2 = L2.next
return L1
'''