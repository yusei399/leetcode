class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.isSymmetricHelper(root.left, root.right)
    
    def isSymmetricHelper(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        elif left.val != right.val:
            return False
        else:
            return self.isSymmetricHelper(left.left, right.right) and self.isSymmetricHelper(left.right, right.left)
