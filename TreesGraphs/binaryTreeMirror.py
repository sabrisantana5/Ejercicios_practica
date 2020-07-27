# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def isMirror(p,q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val) and isMirror(p.left,q.right) and isMirror(p.right,q.left)
    
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return isMirror(root,root)


''' Realmente no sirve en varios casos pero así lo pensé
def inorder(root,s):
    if root:
        inorder(root.left,s)
        s.append(root.val)
        inorder(root.right,s)

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        result = []
        inorder(root,result)
        return result == result[::-1]
'''