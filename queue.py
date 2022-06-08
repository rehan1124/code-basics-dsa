"""
Queue
Works on FIFO. First-in First-out concept

Reference: https://www.youtube.com/watch?v=rUUrmGKYwHw&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=8

Using collections.deque
"""

from collections import deque


class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, data):
        self.container.appendleft(data)

    def dequeue(self):
        return self.container.pop()

    def size(self):
        return len(self.container)

    def is_empty(self):
        return self.size() == 0


if __name__ == "__main__":
    d1 = {
        "customer_name": "Zara",
        "traffic": 120,
        "timestamp": "2022-06-08 10:30:00"
    }
    d2 = {
        "customer_name": "Zara",
        "traffic": 100,
        "timestamp": "2022-06-08 11:00:00"
    }
    d3 = {
        "customer_name": "Zara",
        "traffic": 50,
        "timestamp": "2022-06-08 11:30:00"
    }
    q1 = Queue()
    # --- Insert data in Queue ---
    q1.enqueue(d1)
    q1.enqueue(d2)
    q1.enqueue(d3)
    print(
        q1.container)  # deque([{'customer_name': 'Zara', 'traffic': 50, 'timestamp': '2022-06-08 11:30:00'},
    # {'customer_name': 'Zara', 'traffic': 100, 'timestamp': '2022-06-08 11:00:00'}, {'customer_name': 'Zara',
    # 'traffic': 120, 'timestamp': '2022-06-08 10:30:00'}])
    # --- Get size of Queue ---
    print(q1.size())  # 3
    # -- Check if Queue is empty ---
    print(q1.is_empty())  # False
    # --- Remove elements from Queue (FIFO)
    print(q1.dequeue())  # {'customer_name': 'Zara', 'traffic': 120, 'timestamp': '2022-06-08 10:30:00'}
    print(q1.dequeue())  # {'customer_name': 'Zara', 'traffic': 100, 'timestamp': '2022-06-08 11:00:00'}
    print(q1.container)  # deque([{'customer_name': 'Zara', 'traffic': 50, 'timestamp': '2022-06-08 11:30:00'}])
    print(q1.size())  # 1
