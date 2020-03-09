# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"{self.key}: {self.value}, next: {self.next}"

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
        """
        if we have an item at the designated index we want to create a Linked List at that index
        add the item to the Linked List
        """

        index = self._hash_mod(key)

        if self.storage[index] is not None:
            # print(f"There was a collision at {index}")
            new_pair = LinkedPair(key, value)
            """
            go inside collision
            New pair should be first
            Old pair should be last
            """
            old_pair = self.storage[index]

            self.storage[index] = new_pair
            new_pair.next = old_pair
        else:
            self.storage[index] = LinkedPair(key, value)
        
        # print(f"inserting {key}: {value} at {index}")
        # print(f"{self.storage}")
        # print("")

    

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            if self.storage[index].key == key:
                self.storage[index].value = None
            else:
                current = self.storage[index]
                while current.next is not None:
                    current = current.next
                    
                    if current.key == key:
                        current.value = None
                
                return f"No key found at {index}"
        else:
            return f"No key found at {index}"

        


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            if self.storage[index].key == key:
                return self.storage[index].value
            else:
                current = self.storage[index]
                while current.next is not None:
                    current = current.next

                    if current.key == key:
                        return current.value

                return None
        else:
            return None

            



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        old_storage = self.storage
        self.storage = [None] * self.capacity

        """
        copy items from old_storage into new_storage where new_storage is updated self.storage
        """

        for i in range(0, len(old_storage)):
            """
            walk through old storage[i] and assign values to new_storage
            """
            if old_storage[i]:
                pair = old_storage[i]
                if pair.next is not None:
                    current = pair
                    while current:
                        self.insert(current.key, current.value)
                        current = current.next
                else:
                    self.insert(pair.key, pair.value)


            




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
