#Bo Cen and Canopus Tong
#Lab Section D03 
#Lecture Section A1

def cracker(pair):  # Decrypt a encrypted text.
    ALL_LETTERS = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    new_text = ""
    if len(pair) == 1:  # Check if Key is missing.
        new_text = "Missing key!"
    else:
        text, key = pair[0], pair[1]  # Given a pair of string in a list, assign the cyphertext and key.
        for char in text:  # Translate the cyphertext by its according key using a alphabetical ordered list.
            index = ALL_LETTERS.index(char)  
            new_index = index - int(key)  # Find the new index of each letter by subtracting the key.
            while new_index >= 26:  
                new_index = new_index - 26
            while new_index < 0:
                new_index = new_index + 26
            new_char = ALL_LETTERS[new_index]
            new_text = new_text + new_char
    
    return new_text


filename = input("Enter the input filename: ")  # Main program to run function and print out the resuslt.
file = open(filename)
for line in file:
    line = line.strip()
    line = line.split(" ")  # Split the cyphertext and key apart if applicable.
    print(cracker(line))
