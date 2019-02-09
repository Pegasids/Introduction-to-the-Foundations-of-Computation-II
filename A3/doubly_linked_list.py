class Double_Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class Doubly_Linked_List:
    
    # creates a new doubly linked list
    # head and tail are initialized to None
    def __init__(self):
        self.head = None
        self.tail = None
    
    # adds a new node with data = item to the beginning of the list    
    def add(self, item):
        temp = Double_Node(item)
        #  exception - when the dll is empty
        if self.head == None:
            self.head = temp
            self.tail = self.head
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
    
    # adds a new node with data = item to the end of the list    
    def append(self, item):
        temp = Double_Node(item)
        #  exception - when the dll is empty
        if self.tail == None:
            self.head = temp
            self.tail = self.head
        else:
            temp.prev = self.tail
            self.tail.next = temp
            self.tail = temp
                            
    # insert a new node with data = item at the given position
    # assume index is a valid position to insert at
    def insert(self, index, item):
        temp = Double_Node(item)
        # exception - if user wants to insert at index 0
        if index == 0 or index == 0 - self.size():
            self.add(item)
        # exception - if user wants to insert at the end of the dll
        elif index >= self.size():
            self.append(item)
        else:
            # if user is inserting between the front and back of the dll
            count = 0
            current = self.head
            while count != index:
                count += 1
                current = current.next
            temp.next = current
            current.prev.next = temp
            temp.prev = current.prev
            current.prev = temp
            
    # removes and returns the element at the specified index 
    # assume the index is a valid position to remove at
    # default value indicates to pop from the end of the list
    def pop(self, index=-1):
        # if user wants to pop the last item
        if index == -1 or index == self.size() - 1:
            element = self.tail.data
            # exception - if the dll only has one item
            if self.size() == 1:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        # if user wants to pop the first item
        elif index == 0 or index == 0 - self.size():
            element = self.head.data
            if self.size() == 1:
                self.head = None
                self.tail = None            
            else:
                self.head = self.head.next
                self.head.prev = None
        # if user wants to pop an item located between the front and back of the dll
        else:
            count = 0
            current = self.head
            while count != index:
                current = current.next
                count += 1
            element = current.data
            current.prev.next = current.next
            current.next.prev = current.prev
            
        return element
            
     
    # removes the first node with data = item from the list
    # do nothing if item is not in the list
    def remove(self, item):
        current = self.head
        # check if the dll is empty
        if current != None:
            # exception - the first element in the dll is the item to be removed
            if current.data == item:
                # exception - there is only one element in the dll
                if self.size() == 1:
                    self.head = None
                    self.tail = None
                else:
                    self.head = current.next
                    self.head.prev = None
            else:
                # finding the item in the dll
                while current.data != item:
                    current = current.next
                    # break the while loop if the current item is None to prevent errors
                    if current == None:
                        break
                # check if the current item is None to prevent errors
                if current != None:
                    # check if item is found
                    if current.data == item:
                        # exception - next item is None
                        if current.next == None:
                            self.tail = current.prev
                            current.prev.next = None                            
                        else:
                            current.prev.next = current.next
                            current.next.prev = current.prev
                    
    # returns the size of the doubly linked list
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next
        return count
    
    # returns True if the doubly linked list is empty, False otherwise
    def is_empty(self):
        current = self.head
        if current == None:
            return True
        else:
            return False

    # returns a string representation of the list, from head to tail
    # each piece of data is separated by "->"
    def __str__(self):
        output = []
        current = self.head
        while current:
            output.append(current.data)
            current = current.next
        return "->".join(output)    
        
    # returns a string representation of the list, from tail to head
    # each piece of data is separated by "<-"
    def reverse_string(self):
        output = []
        current = self.tail
        while current:
            output.append(current.data)
            current = current.prev
        return "<-".join(output)
    