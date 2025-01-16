class TreeNode:

    def __init__(self, key, value=None, left=None, right=None):
        if not value:
            value = key
        self.key = key
        self.val = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode {self.val}"


class Tree:

    def __init__(self):
        self.root = None

    # recursive helper
    def preorder_helper(self, current_node, values):
        # if the tree is empty
        if not current_node:
            # return the list of values
            return values

        # Append current node to list of values
        values.append(current_node.val)
        # call helper function on the left child
        self.preorder_helper(current_node.left, values)     
        # call helper function on the right child   
        self.preorder_helper(current_node.right, values)

        return values

    def preorder(self):
        # create an empty list to hold the node's values
        values = []
        # call helper function on root
        return self.preorder_helper(self.root, values)
    
    # recursive helper
    def inorder_helper(self, current_node, values):
        # if the tree is empty
        if not current_node:
            # return the list of values
            return values

        # call helper function on the left child
        self.inorder_helper(current_node.left, values)
        # Append current node to list of values
        values.append(current_node.val)     
        # call helper function on the right child   
        self.inorder_helper(current_node.right, values)

        return values

    def inorder(self):
        # create an empty list to hold the node's values
        values = []
        # call helper function on root
        return self.inorder_helper(self.root, values)
    
     # recursive helper
    def postorder_helper(self, current_node, values):
        # if the tree is empty
        if not current_node:
            # return the list of values
            return values

        # call helper function on the left child
        self.postorder_helper(current_node.left, values)     
        # call helper function on the right child   
        self.postorder_helper(current_node.right, values)
        # Append current node to list of values
        values.append(current_node.val)

        return values

    def postorder(self):
        # create an empty list to hold the node's values
        values = []
        # call helper function on root
        return self.postorder_helper(self.root, values)