#Program that returns the N-K Node on a link list
class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None
def nminusKNode(head, k):
    n = 0
    res = head
    while(head != None):
        n += 1
        head = head.next
    if(n-k<1):
        return head
    else:
        n-=k
        for x in range(n-1):
            res = res.next
    return res.value
        
    
    
Node1 = ListNode(3)
Node2 = ListNode(4)
Node3 = ListNode(5)
Node4 = ListNode(6)
Node5 = ListNode(7)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
print(nminusKNode(Node1,1))
