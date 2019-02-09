filename = input("Enter input filename: ") # ask user for input file name
file = open(filename) # open input file
dct = {} # create a dictionary
for line in file: # read the file by each line
    follower, leader = line.strip("\n").split(" follows ") # split the names of the two users and assign them as follower and leader
    if leader not in dct.keys(): # if the leader's name is not in the keys, create a new key and name it as the leader's name
        dct[leader] = [1, 0] # default as one follower and followering zero leader
    else:
        dct[leader][0] += 1 # if key already exists, add one to the number of follower
        
    if follower not in dct.keys(): # if follower's name is not in the keys, create a new key and name it as the follower's name
        dct[follower] = [0, 1] # default as zero follower and followering one leader
    else:
        dct[follower][1] += 1 # if key already exists, add one to the number of users the user follows

file.close() # close input file

output = open(filename + ".out.txt", "w") # create a new file for writing
for item in dct: # output the dictionary with this format - {username} {number of followers} {number of users the user follows}
    output.write(item + " " + str(dct[item][0]) + " " + str(dct[item][1]) + "\n") 

output.close() # close output file