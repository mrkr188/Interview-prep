# to heapify subtree rooted at index i
def max_heapify(arr, n, i): 
	largest = i 
	left = 2 * i + 1	 # left = 2*i + 1 
	right = 2 * i + 2	 # right = 2*i + 2 

	if left < n and arr[i] < arr[left]: 
		largest = left
	if right < n and arr[largest] < arr[right]: 
		largest = right 

	if largest != i: 
		arr[i], arr[largest] = arr[largest], arr[i] # swap 
		max_heapify(arr, n, largest) 


# heap sort
def heap_sort(arr): 
	n = len(arr) 
	# build a maxheap
	for i in range(n//2 - 1, -1, -1): 
		max_heapify(arr, n, i) 
	# one by one extract elements 
	for i in range(n-1, 0, -1): 
		arr[i], arr[0] = arr[0], arr[i] # swap 
		max_heapify(arr, i, 0) 

arr = [1,3,2,4,7,5,6]

heap_sort(arr) 

print(arr)

