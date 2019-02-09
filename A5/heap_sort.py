from binheap import BinHeap

# HEAP SORT RUNNING TIME O(nlogn)
def heap_sort(my_list):
    sortlst = [] # create a list for sorted values
    heap = BinHeap() # create a heap
    heap.buildHeap(my_list) # build heap from an unsorted list
    while not heap.isEmpty(): # stop the loop when heap is empty
        sortlst.append(heap.delMin()) # keep deleting the min value in the heap and reorganizing the heap and append the min value to sortlst
   
    return  sortlst # return the sorted list
    

def main():
    print(heap_sort([-5,3,10,0]))
    
if __name__ == '__main__':
    main()
