#CMPUT 175
#Lab 9 Skeleton File

class Tree:
    def __init__(self, new_key):
        self.__key = new_key # Root key value
        self.__children = [] # List of children
    
    @staticmethod
    # This static function will load a tree with the format of below:
    # [root[child_1][child_2]...[child_n]]
    # Each child_i can be a tree with the above format, too
    # pos is the position in the given string
    def loadTree(tree_str, pos = 0):
        new_node = None
        while pos < len(tree_str):
            if tree_str[pos] == '[':
                pos += 1
                new_node = Tree(tree_str[pos])
                while pos < len(tree_str) and tree_str[pos + 1] != ']':
                    pos += 1
                    child_tree, pos = Tree.loadTree(tree_str, pos)
                    if child_tree:
                        new_node.__children.append(child_tree)
                return new_node, pos + 1
            else:
                pos += 1
        return new_node, pos
    
    def count_nodes(self):
        count = 1
        for item in self.__children:
            count += item.count_nodes()
        return count
                
        
    def print_preorder(self):
        print(self.__key, end = " ")
        for item in self.__children:
            item.print_preorder()
    
def main():
    # Loading the tree from input file
    with open("input.txt","r") as input_file:
        for line in input_file.readlines():
            # tree_root is a Tree object and processed_chars are the number of 
            # characters we read from the line. We don't need to it for the lab
            tree_root, processed_chars = Tree.loadTree(line)
            
            cnt = tree_root.count_nodes()
            print(cnt, end=" ")
            tree_root.print_preorder()
            print()
           
if __name__ == "__main__":
    main()
