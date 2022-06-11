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
        print(f"Creating BinaryTree node with data: {data}")

    def add_child(self, data):
        """
        Adds 'data' as 'BinaryTree' node
        :param data:
        :return:
        """
        if data == self.data:
            print(f"data {data}, self.data {self.data} are same")
            # Check if data to be added is same as present node data
            return

        if data < self.data:
            print(f"data {data} < self.data {self.data}")
            # Check if data to be added is smaller than present node data
            if self.left is None:
                print(f"self.left is None. Add BinaryTree node with data {data}.")
                # Add only if left of parent node is None
                self.left = BinaryTree(data)
            else:
                # If left of parent node is not None, make recursive calls
                print(f"self.left is not None. Recursively call add_Child.")
                self.left.add_child(data)
        else:
            print(f"data {data} > self.data {self.data}")
            # Check if data to be added is larger than present node data
            if self.right is None:
                print(f"self.right is None. Add BinaryTree node with data {data}.")
                # Add only if right of parent node is None
                self.right = BinaryTree(data)
            else:
                # If right of parent node is not None, make recursive calls
                print(f"self.right is not None. Recursively call add_Child.")
                self.right.add_child(data)

    def in_order_traversal(self):

        elements = []

        # Visit left binary tree nodes
        if self.left:
            print(f"self.left is present.")
            print(f"elements {elements}.")
            elements += self.left.in_order_traversal()

        # Visit base node
        elements.append(self.data)
        print(f"Parent node elements {elements}.")

        # Visit left binary tree nodes
        if self.right:
            print(f"self.right is present.")
            print(f"elements {elements}.")
            elements += self.right.in_order_traversal()

        return elements

    def is_present(self, data):
        if self.data == data:
            return True

        if data < self.data:
            if self.left:
                return self.left.is_present(data)
            else:
                return False

        if data > self.data:
            if self.right:
                return self.right.is_present(data)
            else:
                return False


def build_tree(l1):
    root = BinaryTree(l1[0])
    print(f"Root element {root.data}.")
    for items in range(1, len(l1)):
        print(f"Adding child {l1[items]}.")
        root.add_child(l1[items])
    return root


if __name__ == "__main__":
    sample_list = [17, 4, 1, 20, 9, 23, 18, 34]
    bt = build_tree(sample_list)
    print(bt)
    print(bt.in_order_traversal())  # [1, 4, 9, 17, 18, 20, 23, 34]
    print(bt.is_present(101))  # False
    print(bt.is_present(9))  # True
    print(bt.is_present(18))  # True
    print(bt.is_present(100))  # False
