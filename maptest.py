from heapq import heapify, heappop
from heapq import heappush, heappop


class HeapItem:
    def __init__(self, node_id, distance):
        self.node_id = node_id
        self.distance = distance

    def __lt__(self, other_heap_item):
        return self.distance < other_heap_item.distance  # We want to rank by distance


pq = []
heappush(pq, HeapItem(1, 4.2))
heappush(pq, HeapItem(2, 6.28))
print(pq[0].distance)
print(pq[0] < pq[1])
