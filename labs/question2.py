class Stack:

    def __init__(self):
        self.__stack = []

    def push(self, element):
        self.__stack.append(element)

    def pop(self):
        return self.__stack.pop()

    def peek(self):
        return self.__stack[-1]

    def size(self):
        return len(self.__stack)

    def is_empty(self):
        return self.size() == 0


class Queue:

    def __init__(self):
        self.__queue = []

    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        return self.__queue.pop(0)

    def peek(self):
        return self.__queue[0]

    def size(self):
        return len(self.__queue)

    def is_empty(self):
        return self.size() == 0


def play_hot_potato(players, number_of_passes):
    """
        Simulates the game of hot potato, and returns the name of the winner.
        Modify this function to simulate the game of hot potato in which
        the order of play is reversed whenever a player is eliminated.
    """
            
    #Your code somewhere in this function!

    game_queue = Queue()
    reverse_stack = Stack()

    for player in players:
        game_queue.enqueue(player)

    while game_queue.size() > 1:

        for i in range(number_of_passes):
            game_queue.enqueue(game_queue.dequeue())

        # remove the player holding the potato
        game_queue.dequeue()
        
        while game_queue.size() > 0:
            reverse_stack.push(game_queue.dequeue())
        
        while reverse_stack.size() != 0:
            game_queue.enqueue(reverse_stack.pop())
        
        

    # The remaining player is the winner.
    return game_queue.dequeue()


if __name__ == '__main__':

    number_of_passes = int(input("How many times should the potato be passed"
                                 + " every round? "))

    winner = play_hot_potato(["Bob", "Joe", "Ann", "Sue", "Kim", "Tom"],
                             number_of_passes)
    print('Winner: {}'.format(winner))
