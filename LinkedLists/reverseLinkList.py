#Program that reverses a link list
class ListNode:
    def __init__(self,x):
        self.value = x
        self.next = None
def reverseLinkList(ll):
    anterior = None
    local = ll
    while(local != None):
        siguiente = local.next
        local.next = anterior
        anterior = local
        local = siguiente
    return ll.value
        
Node1 = ListNode("Octa")
Node2 = ListNode("Cris")
Node3 = ListNode("Ruben")
Node4 = ListNode("Martin")
Node5 = ListNode("Sabri")

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
reverseLinkList(Node1)
print(Node5.value)
print(Node5.next.value)
print(Node4.next.value)
print(Node3.next.value)
print(Node2.next.value)
print(Node1.next)

