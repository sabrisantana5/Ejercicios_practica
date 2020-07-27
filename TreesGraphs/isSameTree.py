# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q and (p.val == q.val):
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False
        return True
        
''' 
#With stacks and preorder
def preorderPrint(p: TreeNode, s):
    if p:
        s.append(p.val)
        print(s)
        preorderPrint(p.left,s)
        preorderPrint(p.right,s)

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        sp = []
        sq = []
        preorderPrint(p,sp)
        preorderPrint(q,sq)
        return sp == sq
        
'''