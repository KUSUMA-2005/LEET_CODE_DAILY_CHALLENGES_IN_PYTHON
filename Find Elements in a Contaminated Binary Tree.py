'''Given a binary tree with the following rules:
root.val == 0
For any treeNode:
If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.
Implement the FindElements class:
FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
bool find(int target) Returns true if the target value exists in the recovered binary tree.

Example 1:
Input
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
Output
[null,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True '''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.values=set()
        self.root=root
        if root:
            self.recover_Tree(root,0)
    def recover_Tree(self,node,val):
        if node:
            node.val=val
            self.values.add(val)
            self.recover_Tree(node.left,2*val+1)
            self.recover_Tree(node.right,2*val+2)
    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return True if target in self.values else False

        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)