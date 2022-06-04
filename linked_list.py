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

    def insert_values_from_list(self, data_list):
        self.head = None
        for items in data_list:
            self.insert_at_end(items)

    def calc_length(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
        return count

    def remove_at_index(self, index):

        if index < 0 or index >= self.calc_length():
            raise "Invalid index"

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

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
    # --- Added elements at the end of LL ---
    ll.insert_at_end("Rizwan")
    ll.insert_at_end("Afsha")
    ll.print()  # Shareka-->Rehan-->11-->Rizwan-->Afsha-->
    # --- Add items from list to LL ---
    fruits = ["Apple", "Mango", "Banana"]
    ll.insert_values_from_list(fruits)
    ll.print()  # Apple-->Mango-->Banana-->
    # --- Calculate lenght of Linked List ---
    print(f"Length of Linked List: {ll.calc_length()}")
    # --- Removing items from given index
    ll.remove_at_index(1)
    ll.print()  # Apple-->Banana-->
    ll.remove_at_index(0)
    ll.print()  # Banana-->
