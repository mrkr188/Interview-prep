from collections import Counter
from collections import deque
from collections import namedtuple
from queue import PriorityQueue
import heapq
from collections import defaultdict


arr = [1,2,1,3,4,5,6,2,4,5,1]

# defaultdict
d = defaultdict(int)
d['a'] = 1
print(d)

# named tuple
Student = namedtuple('Student',['name','age','job']) 
x = Student('Rajeev', 27, 'ML Engineer')
print(x.name, '-', x.job)
# initialize with dictionary
di = { 'name' : "Rajeev", 'age' : 27, 'job' : 'ML Engineer' } 
print(Student(**di))

# value counts
print(Counter(arr))
print(Counter(arr).most_common(1))

# for queue use deque
queue = deque([1,2,3])
print(queue.popleft())
print(queue)

# priority queue
q = PriorityQueue()
q.put((10, 'a'))
q.put((1, 'b'))
q.put((5, 'c'))
while not q.empty():
	print(q.get())
