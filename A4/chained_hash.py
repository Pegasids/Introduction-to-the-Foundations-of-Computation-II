# Skeleton code for Assignment #4, Problem 1

# Do not modify the Node ADT
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

# Do not modify the LinkedList ADT        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def add(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp
        
    def __str__(self):
        str_list = []
        current = self.head
        while current:
            str_list.append(str(current.data))
            current = current.next
        return "[" + "->".join(str_list) + "]"
        
# Implement the missing functions in the ChainedHashTable ADT    
class ChainedHashTable:
    # initialize a hash table
    def __init__(self, size):
        self.size = size 
        self.slots = [None] * self.size # create a slot list with a size the user wants
        
    # function for finding a key's slot index
    def hashfunction(self, key, size):
        return (key ** 2) % size
    
    # function for inserting a key
    def insert(self, key):
        hash_val = self.hashfunction(key, self.size)        
        
        # if the slot is not occupied, create a linked list in that slot and insert the key in it
        if self.slots[hash_val] == None: 
            self.slots[hash_val] = LinkedList()
            self.slots[hash_val].add(key)
        else:
            # if the slot is already occupied, just insert the key to be the head of the linked list in that slot
            self.slots[hash_val].add(key)
    
    # function for printing the entire hash table
    def __str__(self):        
        to_be_printed = [] # create a printing list
        for key in self.slots: # iterate through the entire hash table
            if key: # if the slot has key(s) in it, call the __str__ function from the LinkedList class to return all the key(s) as a string and append it to the printing list
                to_be_printed.append(key.__str__())
            else:
                # if the slot doesn't have any key, just append "None" to the printing list.
                to_be_printed.append("None")
        return "[" + ', '.join(to_be_printed) + "]" # return the all the items in the printing list in the correct format
                
    
# Sample testing code
# You should test your ADT with other input as well
cht = ChainedHashTable(11)
cht.insert(1)
cht.insert(36)
cht.insert(3)
cht.insert(44)
cht.insert(91)
cht.insert(54)
cht.insert(18)
print(cht)