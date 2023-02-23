
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        

class solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        # if there is no root node, return null
        if not root:
            return None

        
        # swap the child nodes
        temp = root.left
        root.left = root.right
        root.right = temp
            

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root




# test 
tree = solution([4,2,7,1,3,6,9])
print(tree.invertTree())