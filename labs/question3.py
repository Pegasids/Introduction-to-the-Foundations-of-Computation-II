class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SimpleLinkedList:

    def __init__(self):
        self.__head = None

    def add(self, item):
        """
            Adds ``item`` to the front of the linked list.
        """
        node = Node(item)
        node.next = self.__head
        self.__head = node
       
    def remove(self, item):
        """
            Removes the first occurrence of item.
        """  
        if self.is_empty():
            return

        previous = None
        current = self.__head

        if self.__head.data == item:
            self.__head = self.__head.next
        else:
            previous = current
            current = current.next
            while not current is None:
                if current.data == item:
                    previous.next = current.next
                    # We found the first occurrence! We may stop.
                    return

                previous = current
                current = current.next

    def is_empty(self):
        return self.__head is None

    def length(self):
        counter = 0
        current = self.__head
        while current is not None:
            current = current.next
            counter += 1
        return counter

    def count(self, item):
        """
            Returns an integer corresponding to the number of occurrences of 
            ``item`` in the linked list.                
        """
        time = 0
        current = self.__head
        while current is not None:
            if current.data == item:
                time = time + 1
            
            current = current.next
                
        return time

if __name__ == '__main__':

    with open('input-3.txt') as input_file:
        items_to_insert = input_file.readline().strip().split()
        items_to_count = input_file.readline().strip().split()

    linked_list = SimpleLinkedList()

    for item in items_to_insert:
        linked_list.add(item)

    for item in items_to_count:
        print('Occurrences of {}: {}'.format(item, linked_list.count(item)))
