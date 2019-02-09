#Bo Cen and Canopus Tong
#Lab Section D03 
#Lecture Section A1

def read_file(filename): # Read a file and return a list of rows of the sudoku.
    puzzle = []
    file = open(filename)
    for line in file:
        puzzle.append(line[:-1])
        
    return puzzle    

def check(num_lst): # Checks a list of numbers and return if there are any same numbers.
    validity = True
    num_lst.sort()
    for i in range(num_lst.count(0)):
        num_lst.remove(0)
    last_num = 0
    while len(num_lst) > 0:
        popped_num = num_lst.pop()
        if last_num == popped_num:
            validity = False
            break 
        else:
            last_num = popped_num
    
    return validity


filename = input("Enter the input filename: ")
puzzle = read_file(filename) 
validity = True
for line in puzzle: # Check all rows of the sudoku.
    temp_lst = []
    for num in line: 
        temp_lst.append(int(num)) 
    if check(temp_lst) == False:
        validity = False
                
for i in range(9): # Check all columes of the sudoku.
    temp_lst = []
    for line in puzzle:
        temp_lst.append(int(line[i]))
    if check(temp_lst) == False:
        validity = False

box1 = []; box2 = []; box3 = [] # A list for each 3x3 box.
box4 = []; box5 = []; box6 = []
box7 = []; box8 = []; box9 = []

for line in puzzle[:3]: # Append and check the first 3 boxes. 
    for n in line[:3]:
        box1.append(int(n))
    for n in line[3:6]:
        box2.append(int(n))
    for n in line[6:9]:
        box3.append(int(n))     
if check(box1) == False:
    validity = False    
elif check(box2) == False:
    validity = False
elif check(box3) == False:
    validity = False  

for line in puzzle[3:6]: # Append and check the next 3 boxes.     
    for n in line[:3]:
        box4.append(int(n))
    for n in line[3:6]:
        box5.append(int(n))
    for n in line[6:9]:
        box6.append(int(n))
if check(box4) == False:
    validity = False    
elif check(box5) == False:
    validity = False
elif check(box6) == False:
    validity = False     
    
for line in puzzle[6:9]: # Append and check the last 3 boxes.
    for n in line[:3]:
        box7.append(int(n))
    for n in line[3:6]:
        box8.append(int(n))
    for n in line[6:9]:
        box9.append(int(n))
if check(box7) == False:
    validity = False    
elif check(box8) == False:
    validity = False
elif check(box9) == False:
    validity = False
  
if validity == False: # Print the final result (validity).
    print("The puzzle is not valid!")
elif validity == True:
    print("The puzzle is valid!")
    

        
            
        
        
        
        
            
        
            

        
            
            
        


            
    
        
        

        
    
    
        
            
            
            