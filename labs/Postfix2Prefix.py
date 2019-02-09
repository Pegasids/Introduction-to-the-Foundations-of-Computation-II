class Stack:
     def __init__(self):
          self.items = []

     def is_empty(self):
          return self.items == []

     def push(self, item):
          self.items.append(item)

     def pop(self):
          return self.items.pop()

     def peek(self):
          return self.items[len(self.items)-1]

     def size(self):
          return len(self.items)

#implement postfix to prefix converstion
def postfix_to_prefix(postfix_expr):
     varstack = Stack()
     opstack = Stack()

     for letter in postfix_expr:
          if letter in "ABCDEFGHIJKLMNOPQWXYZ":
               varstack.push(letter)
          
          elif letter in "+-*/^":
               opstack.push(letter)
          
          while opstack.size() == 1:
               num2 = varstack.pop()
               num1 = varstack.pop()
               op = opstack.pop()
               varstack.push(op + num1 + num2)
     
     return varstack.pop()
               
               
               
         
          
          
          
          
               

def main():

     postfix_expr = input("postfix:")
     print("prefix:" + postfix_to_prefix(postfix_expr))
    
if __name__ == "__main__":
     main()
    
    
