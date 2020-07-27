#Program that merges two sorted lists
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        salida = ListNode (0)
        res = salida

        if(l1 == None and l2 == None):
            return l1
        
        while(l1 != None or l2 != None):
            if(l1 == None):
                salida.val = l2.val
                l2 = l2.next
                if(l2 == None):
                    return res
            elif(l2 == None):
                salida.val = l1.val
                l1 = l1.next
                if(l1 == None):
                    return res
            else:   
                if(l1.val < l2.val):
                    salida.val = l1.val
                    l1 = l1.next
                else:
                    salida.val = l2.val
                    l2 = l2.next
            salida.next = ListNode(0)
            salida = salida.next           
        return res
    