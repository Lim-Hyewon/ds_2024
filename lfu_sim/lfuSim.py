from heap import MinHeap


frq_dict = {}

class Node:
  def __init__(self, lpn):
    self.lpn = lpn
    self.frq = frq_dict[lpn]

  def __lt__(self, other:"Node"):
    return self.frq < other.frq
  
  def __eq__(self, other:"Node"):
    return self.frq == other.frq
  
  def __gt__(self, other:"Node"):
    return self.frq > other.frq


def lfu_sim(cache_slots):
  cache_hit = 0
  tot_cnt = 0

  data_file = open("linkbench.trc")

  hp = MinHeap()
  frq_dict.clear()

  for line in data_file.readlines():
    lpn = line.split()[0]
    tot_cnt += 1

    if lpn not in frq_dict: # 초기화
      frq_dict[lpn] = None
      
    n = Node(lpn)

    if hp.size() < cache_slots: # cache 빈 공간 o
      if n.frq == None: # 처음 나온 lpn
        n.frq = 1
        frq_dict.update({lpn:n.frq})
        hp.insert(n)

      else: # 이미 나온 적 있는 lpn
        n.frq += 1
        frq_dict.update({lpn:n.frq})
        idx = hp.getIndex(lpn)
        if idx != -1: # lpn in cache
          hp.getNode(idx).frq += 1
          hp.percolateDown(idx)
          cache_hit += 1
        else: # lpn not in cache
          hp.insert(n) 

    else: # cache 빈 공간 x
      if n.frq == None: # 처음 나온 lpn
        n.frq = 1
        frq_dict.update({lpn:n.frq})
        hp.deleteMin()
        hp.insert(n)

      else: # 이미 나온 적 있는 lpn
        n.frq += 1
        frq_dict.update({lpn:n.frq})
        idx = hp.getIndex(lpn)
        if idx != -1: # lpn in cache
          hp.getNode(idx).frq += 1
          hp.percolateDown(idx)
          cache_hit += 1
        else:  # lpn not in cache
          hp.deleteMin()
          hp.insert(n)

  print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", cache_hit / tot_cnt)


if __name__ == "__main__":
  for cache_slots in range(100, 1000, 100):
    lfu_sim(cache_slots)
