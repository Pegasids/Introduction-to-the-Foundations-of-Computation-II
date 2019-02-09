import timeit

class Queue_Fast_Front:
    """
        Queue implementation with O(1) dequeue and O(n) enqueue, where n is
        the size of the queue.
    """

    def __init__(self):
        self.__queue = []

    def enqueue(self, item):
        self.__queue.insert(0,item)
        

    def dequeue(self):
        return self.__queue.pop()

    def size(self):
        return len(self.__queue)

    def is_empty(self):
        return self.size() == 0


class Queue_Fast_Back:
    """
        Queue implementation with O(1) enqueue and O(n) dequeue, where n is
        the size of the queue.
    """    

    def __init__(self):
        self.__queue = []

    def enqueue(self, item):
        self.__queue.append(item)



    def dequeue(self):
        return self.__queue.pop(0)

    def size(self):
        return len(self.__queue)

    def is_empty(self):
        return self.size() == 0  

def setup(queue, number_of_elements):
    """
        Enqueues elements, so as to allow visible contrast between enqueue
        dequeue in Queue_Fast_Front and Queue_Fast_Back.
    """
    for i in range(number_of_elements):
        # It does not matter what we enqueue.
        queue.enqueue("--")
        
    return queue
    

if __name__ == "__main__":
    
    number_of_elements = int(input("What should the size " +
                                   "of the queue be? "))
    number_of_repetitions = 100
    
    for operation_type in ("enqueue", "dequeue"):
        for queue_type in ("Queue_Fast_Front","Queue_Fast_Back"):
            
            setup_str = (("from __main__ import setup, {0}; " + 
                         "queue = setup({0}(),{1})")
                         .format(queue_type, number_of_elements))
        
            if operation_type == "enqueue":
                stmt_str = "queue.enqueue(\"--\")"
            else:
                stmt_str = "queue.dequeue()"
            
            time = min(timeit.repeat(stmt=stmt_str, setup=setup_str, 
                                     repeat=number_of_repetitions,
                                     number=1))
          
            print(("For {} with {} elements, the estimated running time " +
                   "for {} was {:.0f} \u03BCs.")
                  .format(queue_type, number_of_elements, operation_type,
                          time*10**6))