from listQueue import ListQueue
import threading
import time

class Producer:
    def __init__(self, items, rank, queue_1, queue_2, queue_3):
        self.__alive = True
        self.items = items
        self.rank = rank
        self.pos = 0 # position
        self.worker = threading.Thread(target=self.run)
        self.__queue_1 = queue_1
        self.__queue_2 = queue_2
        self.__queue_3 = queue_3
        # 프로그램을 여러개 만들어서(코드는 같음) 하는 작업이 다를 때 따로 돌려서 합친다?
    def get_item(self):
        if self.pos < len(self.items):
            item = self.items[self.pos]
            self.pos += 1
            return item
        else:
            return None

    def run(self):
        while True:
            time.sleep(0.2)
            if self.__alive:
                item = self.get_item()
                if self.rank == 3:
                    self.__queue_1.enqueue(item)
                elif self.rank == 2:
                    self.__queue_2.enqueue(item)
                elif self.rank == 1:
                    self.__queue_3.enqueue(item)
                print("Arrived:", item)
            else:
                break
        print("Producer is dying...")

    def start(self):
        self.worker.start()

    def finish(self):
        self.__alive = False
        self.worker.join()

class Consumer:
    def __init__(self, queue_1, queue_2, queue_3):
        self.__alive = True
        self.worker = threading.Thread(target=self.run)
        self.__queue_1 = queue_1
        self.__queue_2 = queue_2
        self.__queue_3 = queue_3

    def run(self):
        while True:
            time.sleep(1)
            if self.__alive:
                print("Boarding:", self.__queue_1.dequeue()) # IndexError
                if self.__queue_1.isEmpty() == 0:
                    print("Boarding:", self.__queue_2.dequeue())
                elif self.__queue_2.isEmpty() == 0:
                    print("Boarding:", self.__queue_3.dequeue())
            else:
                break
        print("Consumer is dying...")

    def start(self):
        self.worker.start()

    def finish(self):
        self.__alive = False
        self.worker.join() # 배열을 문자열로 합쳐주는 함수

if __name__ == "__main__": # main 함수에서 queue를 만들어서 넘기세요?
    
    queue_platinum = ListQueue()
    queue_gold = ListQueue()
    queue_normal = ListQueue()

    customers = []
    with open("customer.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            customer = line.split()
            customers.append(customer)

    names = []
    rank = []
    for c in customers:
        names.append(c[1]) 
        rank.append(c[0])
    
    producer = Producer(names, rank, queue_platinum, queue_gold, queue_normal)

    consumer = Consumer(queue_platinum, queue_gold, queue_normal)

    producer.start()
    consumer.start()
    time.sleep(10)
    producer.finish()
    consumer.finish()
