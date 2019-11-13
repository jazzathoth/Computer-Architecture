# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        idx = self._hash_mod(key)
        head = self.storage[idx]
        prev = None
        new_pair = LinkedPair(key, value)

        if head is not None:
            while head is not None:
                if head.key == key:
                    head.value = value
                    return
                prev = head
                head = head.next
            head = new_pair
            prev.next = head
            return

        else:
            self.storage[idx] = new_pair
            return



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        idx = self._hash_mod(key)
        head = self.storage[idx]
        prev = None

        while head is not None:
            if head.key == key:
                break
            prev = head
            head = head.next

        if head is None:
            print("Error: nothing to remove.")
            return None

        if prev is not None:
            prev.next = head.next
        else:
            self.storage[idx] = head.next

        print(f"Removed Key: {head.key} with Value: {head.value}")
        return head.value


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        idx = self._hash_mod(key)
        head = self.storage[idx]

        while head is not None:
            if head.key == key:
                return head.value

            head = head.next
        print("Error: Key not found")

        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        new_cap = len(self.storage) * 2
        new_storage = [None] * new_cap

        old_storage = self.storage

        self.capacity = new_cap
        self.storage = new_storage

        for item in old_storage:
            if item is not None:
                head = item
                while head is not None:
                    self.insert(head.key, head.value)
                    head = head.next

        return



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
