class Node():
    def __init__(self, action=""):
        self.action = action
        self.next = None
        self.prev = None


class Transactions():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
