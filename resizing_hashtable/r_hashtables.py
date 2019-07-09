class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.count = 0



def hash(string, max):
    hashed = 5381
    for s in string:
        hashed = (hashed * 33) + ord(s)
    return hashed % max



def hash_table_insert(hash_table, key, value):
    pass
    i = hash(key, hash_table.capacity)

    if hash_table.storage[i] == None:
        hash_table.storage[i] = LinkedPair(key, value)
        hash_table.count += 1

    else:
        temp = hash_table.storage[i]
        if temp.key == key:
            hash_table.storage[i].value = value
            return None
        else:
            while temp.next != None:
                temp = temp.next
                if temp.key == key:
                    temp.value = value
                    return None
        temp.next = LinkedPair(key, value)
        hash_table.count += 1

    if hash_table.count >= 0.8*hash_table.capacity:
        hash_table = hash_table_resize(hash_table)

    return None


def hash_table_remove(hash_table, key):
    i = hash(key, hash_table.capacity)
    current = hash_table.storage[i]

    if current is None:
        print(f'Warning! {key} is not in the hash table')
        return None

    else:
        temp = hash_table.storage[i]

        if temp.next != None:
            while temp.next != None:
                if temp.next.key == key:
                    temp.next = temp.next.next
                    hash_table.count -= 1
                    break
                temp = temp.next
        else:
            if temp.key == key:
                hash_table.storage[i] = None

                return None
    return None


def hash_table_retrieve(hash_table, key):
    i = hash(key, hash_table.capacity)

    if hash_table.storage[i] != None:
        temp = hash_table.storage[i]

        while temp != None:
            if temp.key == key:
                return temp.value
            temp = temp.next

    return None


def hash_table_resize(hash_table):
    new_table = HashTable(hash_table.capacity*2)
    return new_table


def Testing():
    ht = HashTable(1)

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
