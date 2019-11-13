from doubly_linked_list import DoublyLinkedList


class StackLambda:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        return

    def pop(self):
        if self.len() <= 0:
            return
        else:
            value = self.storage.head.value
            self.storage.remove_from_head()
            return value

    def len(self):
        return len(self.storage)
