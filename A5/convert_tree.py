class Tree:
    
    def __init__(self, new_key):
        self.__key = new_key    # Root key value
        self.__children = []     # List of children
        self.__num_of_descendants = 0 # Number of Descendants of this node    
        
    # Prints the given tree
    def printTree(self):
        return self.printTreeGivenPrefix("", True)   
        
    # Prints the given tree with the given prefix for the line
    # last_child indicates whether the node is the last of its parent"s child
    # or not
    def printTreeGivenPrefix(self, line_prefix, last_child):
        print(line_prefix, end="")
        if last_child:
            print("└--> ", end="")
        else:
            print("|--> ", end="")
        print(self.__key)
        
        if len(self.__children) > 0:
            next_pre = line_prefix
            if last_child:
                next_pre += "     "
            else:
                next_pre += "|    "
            for child_index in range(len(self.__children)-1):
                self.__children[child_index].printTreeGivenPrefix(next_pre, False)
            self.__children[-1].printTreeGivenPrefix(next_pre, True)
        
    def __repr__(self):
        return "[" + str(self.__key) + "".join(
            [ repr(child) for child in self.__children ]) + "]"
    
    # This static function will load a tree with the format of below:
    # [root[child_1][child_2]...[child_n]]
    # Each child_i can be a tree with the above format, too
    # pos is the position in the given string
    @staticmethod
    def loadTree(tree_str, pos = 0):
        new_node = None
        while pos < len(tree_str):
            if tree_str[pos] == "[":
                pos += 1
                new_node = Tree(tree_str[pos])
                while pos < len(tree_str) and tree_str[pos + 1] != "]":
                    pos += 1
                    child_tree, pos = Tree.loadTree(tree_str, pos)
                    if child_tree:
                        new_node.__children.append(child_tree)
                        new_node.__num_of_descendants += \
                            1 + child_tree.__num_of_descendants
                return new_node, pos + 1
            else:
                pos += 1
        return new_node, pos
    
    # This function picks and returns the child with the largest number of descendants.
    # It also includes Tie-breaking.
    def find_max(self):
        max_num = -1
        for child in self.__children:
            if child.__num_of_descendants > max_num: # Find the child with the most descendants.
                max_num = child.__num_of_descendants
                max_child = child
            elif child.__num_of_descendants == max_num: # Tie-breaking.           
                if ord(child.__key) >= ord(max_child.__key):
                    max_child = child    
                    
        return max_child # Return max_child.
    
    # Convert a general tree to a binary tree.
    def convert_to_binary_tree(self):
        if len(self.__children) > 2: # Check if the node has more than 2 children.
            left_right = [] # Create a list for new binary sub-trees.
            
            while len(left_right) < 2: # Find the left and right child.
                max_child = self.find_max() 
                self.__children.remove(max_child) # Remove max_child from the __children list.
                left_right.append(max_child) # Append max_child to the new list for new binary sub-tree.
            
            while len(self.__children) > 0: # Take the rest of children from the general tree and add them under the left and right child in the new list for new binary sub-tree.         
                item = self.find_max() # Find the max child among the rest of children in the general tree.
                
                if left_right[0].__num_of_descendants < left_right[1].__num_of_descendants: # If the left child has less descendants than the right child, add the max child under left child.
                    left_right[0].__children.append(item)
                    left_right[0].__num_of_descendants += (1 + item.__num_of_descendants) # Update the number of descendants of left child
                
                else:                 
                    left_right[1].__children.append(item) # Add the max child under right child.    
                    left_right[1].__num_of_descendants += (1 + item.__num_of_descendants) # Update the number of descendants of right child
                    
                self.__children.remove(item) # Remove the max child from the __children list.
            
            self.__children = left_right # Swap the left_right list(new binary sub-trees) with the __children list.
            
            self.convert_to_binary_tree() # Recursion! # Convert the rest of the sub-trees(descendants) into a binary tree recursively. 
            
        
        else:
            for child in self.__children: # Traverser the rest of the node to find if there're any nodes that have more than 2 children.
                child.convert_to_binary_tree() # Recursion!
                        
                
                
            
        
def main():
    tree, processed_chars = Tree.loadTree("[z[y[v]][x[w]]]")
    tree.convert_to_binary_tree()
    tree.printTree()
    print(tree)
        
if __name__ == "__main__":
    main()
