class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        children = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
        
        if len(children) == 0:
            if root.val == None:
                return []
            return [str(root.val)]
        
        # for each kid, append current node's val to it
        for i in range(len(children)):
            children[i] = str(root.val) + "->" + children[i]
            
        return children