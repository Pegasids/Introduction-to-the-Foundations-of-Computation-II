# Flip a number between 0 and 1
def flip (num): 
    if num == "0":
        return "1"
    if num == "1":
        return "0"

# Find the hamming distance between two strings
def check(string, old_string):
    k = 0
    for ch1, ch2 in zip(string, old_string):
        if ch1 != ch2:
            k += 1
    return k

# Find all the possible flipped strings and add them into a set.
def ham(string, k):
    if k == 0:
        sett.add(string)
    else:
        for i in range(len(string)):
            # recursion
            ham(string[:i] + flip(string[i]) + string[i + 1:], k - 1)

# Ask user for filename
filename = input("Enter input filename: ")
file = open(filename)
# Read the file and assign the strings and hamming distance to string and k accordingly
for line in file:
    line = line.strip()
    line = line.strip("\n")
    string, k = line.split()
    k = int(k)
    
    # Check for unvalid hamming distance
    if k > len(string):
        print("No strings with distance", k, "from", string, "\n")
    else:
        print("Strings with distance", k, "from", string)
        # Create a set for storing strings
        sett = set()
        # Calling the ham function and find all the flipped strings
        ham(string, k)
        # Filter all the incorrect strings in the set and print the correct string with the desired hamming distance
        for item in sett:            
            if check(item, string) == k:
                print(item)
        print()
        
file.close()