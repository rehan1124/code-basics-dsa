"""
Stack
Follows LIFO, Last-in First-out
https://www.youtube.com/watch?v=zwb3GmNAtFk&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=7

Using collections.deque
"""

from collections import deque

stack = deque()
stack.append("A")
stack.append("B")
print(stack)
