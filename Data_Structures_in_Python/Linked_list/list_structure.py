class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

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

    def length_linkedlist(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_values(self, data_list):
        self.head = None # it will empty the linkedlist
        for data in data_list:
            self.insert_at_end(data)

    def remove_elements(self, index = 0):
        if index < 0 or index >= self.length_linkedlist():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                return
            itr = itr.next
            count += 1

    def insert_at(self, data, index=0):
        if index < 0 or index > self.length_linkedlist():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break


if __name__ == "__main__":
    ll = Linkedlist()
    ll.insert_at_beginning(23)
    ll.insert_at_beginning(25)
    ll.insert_at_beginning(27)
    ll.insert_at_beginning(29)
    ll.insert_at_end(24)
    ll.insert_at_end(25)
    ll.length_linkedlist()
    ll.insert_values(["red", "blue", "pink", "green", "yellow"])
    ll.insert_at(3,3)
    ll.print()