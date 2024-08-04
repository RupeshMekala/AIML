# This class (Node) will assign the Linked list its element(data) and the address to the next element(next)
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


# This class does multiple operations
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head) # missed adding self.head
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


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(56)
    ll.insert_at_beginning(57)
    ll.insert_at_beginning(58)

    ll.print()  # missed







