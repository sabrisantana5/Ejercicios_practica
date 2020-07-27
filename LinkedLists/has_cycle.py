#Checks if a linked list has a cycle
class LinkList:
    def __init__(self,x):
        self.value = x
        self.next = None
        
class Solution:
    def has_cycle(head):
        dict = {}
        while(head != None):
            if head in dict:
                return True
            else:
                dict[head] = 1
            head = head.next
        return False
    
one = LinkList(1)
two = LinkList(2)
one.next = two
three = LinkList(3)
two.next = three
three.next = two
sol = Solution
print(sol.has_cycle(one))
