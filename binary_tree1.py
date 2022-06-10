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
