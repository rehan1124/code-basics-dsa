"""
Tree (General Tree)
Tree data structure is used to represent hierarchical data such as organization hierachy,
product categories, geographic locations etc.

Root node -> Nodes -> Leaf nodes
Level 0 -> Level 1 -> Level 2

Reference: https://www.youtube.com/watch?v=4r_XR9fUPhQ&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=9
"""


class TreeNode:
    """
    All the nodes will be created first following below patter as per __init__
    """

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, obj):
        """
        Nodes/Objects created from TreeNode will be passed as arguments to add_child
        :param obj:
        :return:
        """
        # The parent of the object (obj) that is added will be the object (self) on which add_child is called
        obj.parent = self
        self.children.append(obj)

    def get_level(self):
        """
        Calculates level of the associated object
        :return:
        """
        level = 0
        p = self.parent
        while p:
            level += 1
            # Go one level up to check if parent exists
            p = p.parent
        return level

    def print_tree(self):
        spaces = " " * self.get_level() * 2
        prefix = spaces + "|__" if self.parent else ""
        # Print "data" of the associated object
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                # Recursively call "print_tree" to check for "children" and print "data"
                child.print_tree()


def separator():
    print("-" * 10)


if __name__ == "__main__":
    # --- Electronics ---
    root = TreeNode("Electronics")
    # print(root)
    # print(root.data)
    # print(root.children)
    # print(root.parent)
    # print(root.get_level())
    # separator()
    # --- Laptop ---
    laptop = TreeNode("Laptop")
    mac_book = TreeNode("MacBook")
    lenovo = TreeNode("Lenovo")
    acer = TreeNode("Acer")

    root.add_child(laptop)
    laptop.add_child(mac_book)
    laptop.add_child(lenovo)
    laptop.add_child(acer)

    # print(root)
    # print(laptop.data)
    # print(root.children)
    # print(laptop.parent)
    # print(laptop.get_level())
    # separator()
    # --- Mobile ---
    mobile = TreeNode("Mobile")
    iphone = TreeNode("Iphone")
    samsung = TreeNode("Samsung")
    one_plus = TreeNode("OnePlus")
    mobile.add_child(iphone)
    mobile.add_child(samsung)
    mobile.add_child(one_plus)
    root.add_child(mobile)

    # --- TV ---
    tv = TreeNode("TV")
    lg = TreeNode("LG")
    akai = TreeNode("Akai")
    root.add_child(tv)
    tv.add_child(lg)
    tv.add_child(akai)

    # --- Print the tree ---
    root.print_tree()
