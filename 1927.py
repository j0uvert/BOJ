import heapq

n = int(input())
minheap = []

for _ in range(n):
    k = int(input())
    if k == 0:
        try:
            print(heapq.heappop(minheap))
        except:
            print(0)
    else:
        heapq.heappush(minheap, k)
