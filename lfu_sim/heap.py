class MinHeap:
    def __init__(self, *args):
        if len(args) != 0:
            self.__A = args[0]
        else:
            self.__A = []

    def insert(self, x):
        self.__A.append(x)
        self.__percolateUp(len(self.__A)-1)

    def __percolateUp(self, i:int):
        parent = (i-1)//2
        if i > 0 and self.__A[i] < self.__A[parent]: # freq 기준으로 비교하게끔..
            self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
            self.__percolateUp(parent)

    def deleteMin(self):
        if (not self.isEmpty()):
            min = self.__A[0]
            if (len(self.__A)==1):
                return self.__A.pop()
            self.__A[0] = self.__A.pop()
            self.__percolateDown(0)
            return min
        else:
            return None
    
    def __percolateDown(self, i:int):
        # self.__A[i] as the root
        left = 2 * i + 1   # left child
        right = 2 * i + 2 # right child
        if left <= len(self.__A)-1:
            if right <= len(self.__A)-1 and self.__A[left] > self.__A[right]:
                left = right  # index of larger child
            if self.__A[i] > self.__A[left]:
                self.__A[i], self.__A[left] = self.__A[left], self.__A[i]
                self.__percolateDown(left)

    def percolateDown(self, i:int):
        self.__percolateDown(i)

    def min(self):
        return self.__A[0]

    # def buildHeap(self):
    #     for i in range((len(self.__A)-2)//2, -1, -1):
    #         self.__percolateDown(i)

    def isEmpty(self) -> bool:
        return len(self.__A) == 0

    def clear(self):
        self.__A = []

    def size(self):
        return len(self.__A)
    
    def heapPrint(self):
        ...

import random as rd

if __name__ == "__main__":
    a = MinHeap()
    for i in range(100):
        r = rd.randint(-1000, 1000)
        a.insert(r)
    b = []
    for i in range(100):
        b.append(a.deleteMin())
    print(b==sorted(b))