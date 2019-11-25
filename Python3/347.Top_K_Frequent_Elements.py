import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        heap = []
        counter = 0
        for num, freq in freq_map.items():
            if (counter < k):
                heapq.heappush(heap, (freq, num))
                counter += 1
                continue
            smallest_in_heap = heapq.heappop(heap)
            if (freq > smallest_in_heap[0]):
                heapq.heappush(heap, (freq, num))
                continue
            heapq.heappush(heap, smallest_in_heap)
            
        
        for i in range(len(heap)):
            heap[i] = heap[i][1]

        return heap

        

        