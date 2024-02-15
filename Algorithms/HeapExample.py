import heapq

priority_queue = [(0, 'A'), (2, 'B'), (1, 'C')]


heapq.heapify(priority_queue)
'''
heapifying the list

'''


heapq.heappush(priority_queue, (1, 'D'))
'''
pushing another element onto the heap
'''

smallest_distance, node = heapq.heappop(priority_queue)
