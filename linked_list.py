"""
Linked list
[YouTube]
https://www.youtube.com/watch?v=qp8u-frRAnU&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=4
"""


class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """
        Adds given "data" at the beginning of "Linked List"
        :param data:
        :return:
        """
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        """
        Adds given "data" at the end of "Linked List"
        :param data:
        :return:
        """

        if self.head is None:
            self.insert_at_beginning(data)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def print(self):
        """
        Method to print contents of "Linked List" object
        :return:
        """
        if self.head is None:
            print("--- Empty linked list ---")
            return

        ll_str = ""
        itr = self.head
        while itr:
            ll_str += str(itr.data) + "-->"
            itr = itr.next

        print(ll_str)


if __name__ == "__main__":
    # Initializing "Linked List"
    ll = LinkedList()
    ll.print()  # --- Empty linked list ---
    # Add elements to the beginning of list
    ll.insert_at_beginning(11)
    ll.print()  # 11-->
    ll.insert_at_beginning("Rehan")
    ll.insert_at_beginning("Shareka")
    ll.print()  # Shareka-->Rehan-->11-->
    ll.insert_at_end("Rizwan")
    ll.insert_at_end("Afsha")
    ll.print()  # Shareka-->Rehan-->11-->Rizwan-->Afsha-->
