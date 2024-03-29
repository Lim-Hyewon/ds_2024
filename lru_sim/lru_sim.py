from circularLinkedList import CircularLinkedList


class CacheSimulator:
    def __init__(self, cache_slots):
        self.cache_slots = cache_slots
        self.cache_hit = 0
        self.tot_cnt = 1
        self.container = CircularLinkedList()
    
    def do_sim(self, page):
        self.tot_cnt += 1
        if self.container.index(page) != -2:
            self.cache_hit += 1
            self.container.remove(page)
            self.container.append(page)
            return
        if self.container.size() < self.cache_slots:
            self.container.append(page)
        else:
            self.container.pop(0)
            self.container.append(page)

        # if data가 겹침:
        #         cache_hit += 1
        #         (append 안하는데) 자리는 recently, 즉 tail쪽으로 이동 -> update

        # if cache_slot < cache_slots: 캐시 슬롯에 빈자리 있음
        #     그냥 append # append 구문을 위로 빼도 되지만 실제 상황에서 어려울 수 있다 (메모리 이슈)
        
        # else: 캐시 슬롯에 빈자리 없음
        #     기존 head를 쫓아내고 new tail로 새 page append

        
    def print_stats(self):
        print("cache_slot = ", self.cache_slots, "cache_hit = ", self.cache_hit, "hit ratio = ", self.cache_hit / self.tot_cnt)


if __name__ == "__main__":

    data_file = open("./linkbench.trc")
    lines = data_file.readlines()
    for cache_slots in range(100, 1001, 100):
        cache_sim = CacheSimulator(cache_slots)
        for line in lines:
            page = line.split()[0] # "\n" escape sequence 삭제
            cache_sim.do_sim(page)
        
        cache_sim.print_stats()