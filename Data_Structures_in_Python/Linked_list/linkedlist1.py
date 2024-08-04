class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + " --> "
            itr = itr.next

        print(llstr)


if __name__ == "__main__":
    ll = Linkedlist()
    ll.insert_at_beginning(6)
    ll.insert_at_beginning(23)
    ll.insert_at_beginning(24)
    ll.insert_at_beginning(25)
    ll.insert_at_beginning(237)
    ll.insert_at_beginning(2385)
    ll.print()







