"""Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.
If there exist multiple answers, you can return any of them.
Example 1:
Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    preIdx=0
    postIdx=0
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        root=TreeNode(preorder[self.preIdx])
        self.preIdx+=1
        if root.val!=postorder[self.postIdx]:
            root.left=self.constructFromPrePost(preorder, postorder)
        if root.val!=postorder[self.postIdx]:
            root.right=self.constructFromPrePost(preorder, postorder)
        self.postIdx+=1
        return root
        
        

        
        