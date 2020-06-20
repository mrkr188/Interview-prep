import heapq

arr = [3,2,3,1,2,4,5,5,6]
# min heapify
heapq.heapify(arr)
print(arr)


arr = [3,2,3,1,2,4,5,5,6]
# heappop - pops min element 
heapq.heapify(arr)
print(heapq.heappop(arr))
print(arr)

# pushes into heap
heapq.heappush(arr, -5)
heapq.heappush(arr, 10)
print(arr)


arr = [3,2,3,1,2,4,5,5,6]
# get kth largest and smallest
print(heapq.nlargest(3, arr)[-1])
print(heapq.nsmallest(3, arr)[-1])


