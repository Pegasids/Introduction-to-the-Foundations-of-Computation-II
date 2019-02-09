class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def insert(self,item):
        self.items.insert(0,item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

# Function for finding the discarded cards and remaining cards and print them.
def discarded_and_remaining_cards(n, k):
    cards = Queue()
    discard = Stack()
    # Enqueue numbers to a queue from 1 to n.
    for i in range(1, n + 1):
        cards.enqueue(i)
    
    # Stop discarding and flipping cards when only two cards are remained in the queue.
    while cards.size() >= 3:
        # Discard the top card and push it into the discard stack as references.
        discard.push(cards.dequeue())
        # Flip the next top two cards and put in at the bottom of the queue.
        first = cards.dequeue()
        second = cards.dequeue()
        cards.enqueue(second)
        cards.enqueue(first)
    
    # Print the k discarded cards in a list.
    last_k_card = []
    for i in range(k):
        last_k_card.append(discard.pop())
    print("The last", k, "cards discarded are:", last_k_card)
    
    # Print the two remaining cards in a list.
    remain_card = []
    for i in range(2):
        remain_card.insert(0, cards.dequeue())
    print("The two remaining cards are:", remain_card)


# Ask user for the input filename and open the file.
filename = input("Enter input filename: ")
file = open(filename)
# Read each line of the file and assign the first and second value to n and k accordingly.
for line in file:
    n, k = line.split()
    # Call the discarded_and_remaining_cards function and start the task.
    discarded_and_remaining_cards(int(n), int(k))