class MaxBinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    
    def insert(self, item):
        self.heapList.append(item)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
    
    def percUp(self, i):
        while i//2 > 0:
            if self.heapList[i//2] < self.heapList[i]:
                temp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = temp
            i = i//2
        
    def delete(self):
        self.heapList[1] = self.heapList.pop()        
        self.currentSize = self.currentSize - 1
        self.percDown(1)
    
    def max_child(self, i):
        if self.heapList[i*2] > self.heapList[i*2 + 1]:
            return i*2
        else:
            return i*2 + 1
        
    
    def percDown(self, i):
        while i*2 <= self.currentSize:
            index = self.max_child(i)
            if self.heapList[i] < self.heapList[index]:
                temp = self.heapList[index] 
                self.heapList[index] = self.heapList[i]
                self.heapList[i] = temp
            i = index
                                
    def __str__(self):
        return "[" + ", ".join(str(x) for x in self.heapList) + "]"
        
        
maxheap = MaxBinHeap()

populate = [16,12,17,3,5,2,10,9,20,14,18,22,30,25]
for item in populate:
    maxheap.insert(item)

print(maxheap)
maxheap.delete()
print(maxheap)
maxheap.insert(23)
print(maxheap)