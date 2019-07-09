

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hashed = 5381
    for s in string:
        hashed = (hashed * 33) + ord(s)
    return hashed % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    pass
    i = hash(key, hash_table.capacity)
    element = LinkedPair(key, value)
    current = hash_table.storage[i]

    if current is not None:
        current.next = element
        hash_table.storage[i] = element
    else:
        hash_table.storage[i] = element


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    i = hash(key, hash_table.capacity)
    current = hash_table.storage[i]

    if current is None:
        print(f'Warning! {key} is not in the hash table')
    elif len(current) > 1:
        for x in current:
            if x == key:
                x = None
    else:
        current = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    i = hash(key, hash_table.capacity)
    current = hash_table.storage[i]

    return current.value if current.next is None else current.next


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    pass


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
