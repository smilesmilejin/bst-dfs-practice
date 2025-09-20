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

    def inorder(self):
        values = []
        return self.inorder_helper(self.root, values)

    def inorder_helper(self, current_node, values):
        if not current_node:
            return values
        
        # call inorder_helper on left child
        self.inorder_helper(current_node.left, values)

        # add current_node to list of explored_nodes
        values.append(current_node.val)

        # call inorder_helper on right child
        self.inorder_helper(current_node.right, values)

        return values

    def preorder(self):
        # create an empty list to store the explored nodes
        # call preorder helper on root
        explored_nodes = []
        return self.preorder_helper(self.root, explored_nodes)
    
    def preorder_helper(self, current_node, explored_nodes):
        #     if the tree is empty:
        #         return explored_nodes
        if not current_node:
            return explored_nodes
        
        # add current_node to list of explored_nodes
        explored_nodes.append(current_node.val)
        # call preorder_helper on left child
        self.preorder_helper(current_node.left, explored_nodes)
        # call preorder_helper on right child
        self.preorder_helper(current_node.right, explored_nodes)
        # pass

        return explored_nodes
    
    def postorder(self):
        values = []
        return self.postorder_helper(self.root, values)

    def postorder_helper(self, current_node, values):
        #     if the tree is empty:
        #         return explored_nodes
        if not current_node:
            return values
        
        # call postorder_helper on left child
        self.postorder_helper(current_node.left, values)
        # call postorder_helper on right child
        self.postorder_helper(current_node.right, values)
        # add current_node to list of explored_nodes
        values.append(current_node.val)

        return values