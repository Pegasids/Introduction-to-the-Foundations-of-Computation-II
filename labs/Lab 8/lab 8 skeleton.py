# sorts a list of numbers between 1 and n, using the counting sort algorithm
def counting_sort(lst, n):
    sort_lst = []
    counter = [0] * (n+1)
    for i in lst:
        counter[int(i)] += 1
    
    index = 0
    for item in counter:
        time = item
        while time != 0:
            sort_lst.append(index)
            time -= 1
        index += 1
    
    return sort_lst
    
    

# given a list of strings containing numbers, returns a list of numbers
def numerize(lst):
    return lst.split()

# prints a string containing the elements of a given list separated by spaces
def show(lst):
    print(" ".join(str(x) for x in lst))

def main():
    max_num = 100
    file = open("lists.txt")
    for line in file:
        out = counting_sort(numerize(line.strip()), max_num)
        show(out)
        
        

if __name__=="__main__":
    main()
