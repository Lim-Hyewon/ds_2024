from listNode import ListNode

class CircularLinkedList:
    def __init__(self):
        self.__tail = ListNode("dummy", None)
        self.__tail.next = self.__tail
        self.__numItems = 0

    def insert(self, i:int, newItem) -> None:
        if i >= 0 and i <= self.__numItems:
            prev = self.getNode(i-1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            if i == self.__numItems:
                self.__tail = newNode
            self.__numItems += 1
        else:
            print("index", i, ":out of bound in insert()")

    def append(self, newItem) -> None:
        newNode = ListNode(newItem, self.__tail.next)
        self.__tail.next = newNode
        self.__tail = newNode
        self.__numItems += 1

    def pop(self, *args):
        if self.isEmpty():
            return None
        if len(args) != 0:
            i = args[0]
        if len(args) == 0 or i == -1:
            i = self.__numItems - 1
        if (i >= 0 and i <= self.__numItems-1):
            prev = self.getNode(i-1)
            retItem = prev.next.item
            prev.next = prev.next.next
            if i == self.__numItems - 1:
                self.__tail = prev
            self.__numItems -= 1
            return retItem
        else:
            return None

    def remove(self, x):
        (prev, curr) = self.__findNode(x)
        if curr != None:
            prev.next = curr.next
            if curr == self.__tail:
                self.__tail = prev
            self.__numItems -= 1
            return x
        else:
            return None

    def get(self, *args): # i:int 대신 *args
        # i번째 index에 저장된 value 값
        if self.isEmpty():
            return None # edge case 예외처리
        
        if len(args) != 0:
            i = args[0] # 인자가 들어왔을 때 index 설정
        if len(args) == 0 or i == -1:
            i = self.__numItems - 1
        if (i >= 0 and i <= self.__numItems - 1):
            return self.getNode(i).item
        else:
            return None

    def index(self, x) -> int:
        cnt = 0
        for element in self:
            if element == x:
                return cnt
            cnt += 1
        return -2 # 안쓰는 index

    def isEmpty(self) -> bool:
        return self.__numItems == 0

    def size(self) -> int:
        return self.__numItems

    def clear(self):
        self.__tail = ListNode("dummy", None)
        self.__tail.next = self.__tail
        self.__numItems = 0

    def count(self, x) -> int:
        cnt = 0
        for element in self:
            if element == x:
                cnt += 1
        return cnt # return만 다르고 index랑 똑같음?

    def extend(self, a): #a는 순회가능한 모든 객체
        for x in a:
            self.append(x)

    def copy(self) -> b'CircularLinkedList':
        a = CircularLinkedList() # LinkedListBasic()
        for element in self:
            a.append(element)
        return a

    def reverse(self) -> None:
        __head = self.__tail.next
        prev = __head
        curr = prev.next
        next = curr.next
        curr.next = __head
        __head.next = self.__tail
        self.__tail = curr
        for i in range(self.__numItems-1):
            prev = curr
            curr = next
            next = next.next
            curr.next = prev

    def sort(self) -> None:
        a = []
        for element in self:
            a.append(element)
        a.sort()
        self.clear()
        for element in a:
            self.append(element)

    def __findNode(self, x) -> (ListNode, ListNode):
        __head = prev = self.__tail.next
        curr = prev.next
        while curr != __head:
            if curr.item == x:
                return (prev, curr)
            else:
                prev = curr
                curr = curr.next
        return (None, None)

    def getNode(self, i:int) -> ListNode:
        curr = self.__tail.next
        for index in range(i+1):
            curr = curr.next
        return curr

    def printList(self) -> None:
        for element in self:
            print(element, end = ' ')
        print()

    def __iter__(self): #generating iterator and return
        return CircularLinkedListIterator(self)
    

    
class CircularLinkedListIterator:
    def __init__(self, alist):
        self.__head = alist.getNode(-1)
        self.iterPosition = self.__head.next

    def __next__(self):
        if self.iterPosition == self.__head:
            raise StopIteration
        else:
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item