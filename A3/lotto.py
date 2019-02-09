# A recursive function to find all the possible sets with 6 lucky numbers in a list
def lotto(lst):
    # When the length of the list of 6, add the list into a set as a string seperated by a space
    if len(lst) == 6:
        sett.add(' '.join(lst))
    else:
        for i in range(len(lst)):
            # A recursive call to find all the possible set with 6 lucky numbers
            lotto(lst[:i] + lst[i + 1:])

# Ask user for filename
filename = input("Enter input filename: ")
file = open(filename)
for line in file:
    line = line.strip()
    line = line.strip("\n")
    # Make each line in the file to a list
    num_lst = line.split()
    # Create a set to store the outputs
    sett = set()
    # Calling the recursive function to find the output
    lotto(num_lst)
    # Print all the item in the set
    for item in sett:
        print(item)

file.close()