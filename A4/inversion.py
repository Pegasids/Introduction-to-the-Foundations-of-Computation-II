# typical mergeSort with inversion modifications
def count_inversions(lst):
    count = 0 # initialize inversion implementation, set count to zero
    mid = len(lst) // 2
    
    if len(lst) > 1:
        lefthalf = lst[:mid]
        righthalf = lst[mid:]    
        count += count_inversions(lefthalf) # add every count in each recursion
        count += count_inversions(righthalf) # add every count in each recursion
        
        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                lst[k]=lefthalf[i]
                i=i+1
            else:
                count += len(lefthalf[i:]) # if both halves are not empty and item from the righthalf is chosen, add the remaining length of lefthalf that havn't been chosen to count
                lst[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            lst[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            lst[k]=righthalf[j]
            j=j+1
            k=k+1
        
    return count # return the total number of inversion


