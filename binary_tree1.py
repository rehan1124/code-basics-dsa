"""
Binary Tree -> Has at most 2 nodes

Reference: https://www.youtube.com/watch?v=lFq5mYUWEBk&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=10

* Binary search and insert

--- Binary search tree ---
Special case of Binary Tree. Has 2 nodes but left side will always be smaller value than parent node.
Right side will always be greater value than parent node. Inserted elements are always unique.

Big-O is O(log n) for Searching elements in Binary Search Tree. Each time search is made, we reduce number of elements
to be traversed by 1/2.

* 2 traversal techniques: Breadth first search & Depth first search

--- Depth first search ---
In-order traversal -> Left nodes, parent/root node, right node
Pre order traversal ->  Parent/root node, Left nodes, right node
Post order traversal -> Left nodes, right nodes, Parent/root node

"""


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        """
        Adds 'data' as 'BinaryTree' node
        :param data:
        :return:
        """
        if data == self.data:
            # Check if data to be added is same as present node data
            return

        if data < self.data:
            # Check if data to be added is smaller than present node data
            if self.left is None:
                # Add only if left of parent node is None
                self.left = BinaryTree(data)
            else:
                # If left of parent node is not None, make recursive calls
                self.add_child(data)
        else:
            # Check if data to be added is larger than present node data
            if self.right is None:
                # Add only if right of parent node is None
                self.right = BinaryTree(data)
            else:
                # If right of parent node is not None, make recursive calls
                self.add_child(data)
