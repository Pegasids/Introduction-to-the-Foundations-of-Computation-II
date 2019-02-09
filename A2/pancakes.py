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

# Function for reversing a stack and return the reversed stack.
def reverse_a_stack(stack):
    reversed_stack = Stack()
    for i in range(stack.size()):
        reversed_stack.push(stack.pop())
    return reversed_stack

# Function for flipping values in a stack and return the stack after being flipped.
def flip_cakes(lst):
    initial_stack = Stack()
    pancakes_stack = Stack()
    to_be_flipped_stack = Stack()
    
    # Push numbers to initial_stack from 1 to the first numeber of the input file.
    for i in range(1, int(lst[0]) + 1):
        initial_stack.push(i)
        
    # Flip numbers in a stack for sets of times which the user desired.
    for flip_num in lst[1:]:
        # Push numbers that don't need to be flipped into pancakes_stack.
        for i in range(int(lst[0]) - int(flip_num)):
            pancakes_stack.push(initial_stack.pop())
        # Push numbers that are needed to be flipped into a temporary stack.
        for i in range(int(flip_num)):
            to_be_flipped_stack.push(initial_stack.pop())
        # Flipping the numbers by popping values from the temporary stack and push it into pancakes_stack.
        for i in range(int(flip_num)):
            pancakes_stack.push(to_be_flipped_stack.pop())
        
        # Reverse pancakes_stack and assign it to initial_stack to proceed to the next set of flips.
        initial_stack = reverse_a_stack(pancakes_stack)
        # Empty pancakes_stack.
        pancakes_stack.__init__()
    
    # After all the flippings, reverse the initial_stack again back to the correct order and return it.
    return reverse_a_stack(initial_stack)
    

# Ask user for input filename and open file.
filename = input("Enter input filename: ")
file = open(filename)
# Read the lines in the file.
for line in file:
    # Call the flip_cakes function to start the flipping.
    output = flip_cakes(line.split())
    # Print all the values that are in the output stack.
    for i in range(output.size()):
        print(output.pop())
