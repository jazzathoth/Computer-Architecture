"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        if not isinstance(value, ListNode):
            node = ListNode(value)
        else:
            node = value

        if self.head is None:
            self.head = node
            node.prev = None
            node.next = None
            self.tail = node
        else:
            self.tail.next = node
            self.head.prev = node
            node.prev = self.tail
            node.next = self.head
        self.head = node
        self.length += 1
        return

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        current_head = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        elif self.length == 0:
            return
        elif self.length > 1:
            self.head = current_head.next
            self.head.prev = current_head.prev
            self.tail.next = self.head
            self.length += -1
        return current_head.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if not isinstance(value, ListNode):
            node = ListNode(value)
        else:
            node = value

        if self.tail is None:
            node.next = None
            node.prev = None
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.head.prev = node
            node.prev = self.tail
            node.next = self.head
            self.tail = node
        self.length += 1
        return

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        current_tail = self.tail
        if current_tail is None:
            return
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        elif self.length == 0:
            return
        elif self.length > 1:
            self.tail = current_tail.prev
            self.head.prev = self.tail
            self.tail.next = self.head
            self.length += -1
        return current_tail.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if self.length <= 1:
            return
        elif (self.length == 2) & (node != self.head):
            self.head, self.tail = self.tail, self.head
            return
        elif (node != self.head) & (self.length > 2):
            if self.tail == node:
                self.tail = node.prev
            node.prev.next = node.next
            node.next.prev = node.prev
            self.head.prev = node
            self.tail.next = node
            node.next = self.head
            node.prev = self.tail
            self.head = node
        else:
            return
        return

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if self.length <= 1:
            return
        elif (self.length == 2) & (node != self.tail):
            self.head, self.tail = self.tail, self.head
        elif (node != self.tail) & (self.length > 2):
            if node == self.head:
                self.head = node.next
            node.prev.next = node.next
            node.next.prev = node.prev
            self.head.prev = node
            self.tail.next = node
            node.prev = self.tail
            node.next = self.head
            self.tail = node
        return

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if self.length == 0:
            return
        elif self.length == 1:
            self.head, self.tail = None, None
            self.length = 0
        elif self.head == node:
            self.remove_from_head()
        elif self.tail == node:
            self.remove_from_tail()
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            self.length += -1
        return
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        current = self.head
        if self.length == 0:
            return
        else:
            max = self.head.value
            for _ in range(self.length):
                if current.value > max:
                    max = current.value
                current = current.next
            return max
