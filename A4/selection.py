# Skeleton code for Assignment #4, Problem 3
# Note that the statements of the form
#    foo, bar = bar, foo
# will swap the contents of the variables foo and bar
def partition(a_list, first, last):
        
    pivot = a_list[last]
    i = first-1
    for j in range(first, last):
        if a_list[j] <= pivot:
            i += 1
            a_list[i], a_list[j] = a_list[j], a_list[i]

    a_list[i+1], a_list[last] = a_list[last], a_list[i+1]
    return i+1

# this function finds the distance from the first item of the entire list to the k th item of the sublist and call the modified quicksort function to find desired item
def selection(alist, first, last, k):
    return find_item_with_quicksort(alist, first, last, k + first)

# given a list unsorted, this function returns the k th item when the list is sorted
def find_item_with_quicksort(alist, first, last, k):
    if first < last:

        splitpoint = partition(alist, first, last) # call partition function to pivot the items in the list then return the splitpoint where the pivot is
    
        if splitpoint == k - 1: # if the pivot is the k th item of the list, return the item
            return alist[k - 1]        
        
        if splitpoint > k - 1: # if k is less then the splitpoint, call the modified quicksort function recursively to pivot the lefthalf of the list in which the item we want to find is located
            find_item_with_quicksort(alist, first, splitpoint - 1, k)
        
        if splitpoint < k - 1: # if k is bigger then the splitpoint, call the modified quicksort function recursively to pivot the righthalf of the list in which the item we want to find is located
            find_item_with_quicksort(alist, splitpoint + 1, last, k)
                
    return alist[k - 1] # after the item we want to find is at the sorted position, return the item

