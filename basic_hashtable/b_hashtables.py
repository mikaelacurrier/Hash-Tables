

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.elements = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    djb2 = 5381
    for s in string:
        djb2 = (djb2 * 33)+ ord(s)
    return djb2 % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    i = hash(key, hash_table.capacity)
    element = Pair(key, value)
    existing = hash_table.elements[i]
    
    if existing is not None:
        print(f'Warning! You are overwring a key at {i}')
    
    hash_table.elements[i] = element


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    i = hash(key, hash_table.capacity)
    existing = hash_table.elements[i]

    if hash_table.elements[i] is None:
        print(f'Warning! {key} is not in the hash table')
    else:
        hash_table.elements[i] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    i = hash(key, hash_table.capacity)
    element = hash_table.elements[i]

    return element.value if element is not None else None


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
