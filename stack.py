"""
Stack
Follows LIFO, Last-in First-out
https://www.youtube.com/watch?v=zwb3GmNAtFk&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=7

Using collections.deque
"""

from collections import deque


# stack = deque()
# stack.append("A")
# stack.append("B")
# print(stack)


class Stack:
    def __init__(self):
        self.container = deque()

    def size(self):
        return len(self.container)

    def is_empty(self):
        return self.size() == 0

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]


if __name__ == "__main__":
    s1 = Stack()
    # --- Is Stack empty ---
    print(s1.is_empty())  # True
    # --- Stack size ---
    print(s1.size())  # 0
    # --- Add elements to Stack ---
    s1.push("A")
    s1.push("B")
    s1.push("C")
    print(s1.container)  # deque(['A', 'B', 'C'])
    # --- Remove elements from Stack ---
    print(s1.pop())  # C
    print(s1.container)  # deque(['A', 'B'])
    # --- Check element on top of Stack ---
    print(s1.peek())  # B
