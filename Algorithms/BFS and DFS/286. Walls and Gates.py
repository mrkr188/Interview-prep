from collections import deque

def walls_and_gates(rooms):
    """
    Do not return anything, modify rooms in-place instead.
    """
    M = len(rooms)
    if M == 0:
        return
    N = len(rooms[0])

    for i in range(M):
        for j in range(N):
            if rooms[i][j] != 0:
                continue
            # BFS
            queue = deque()
            queue.append((i, j, 0))
            while queue:
                x, y, dis = queue.popleft()
                if x+1 < M and rooms[x+1][y] > 0 and rooms[x+1][y] > dis+1:
                    rooms[x+1][y] = dis+1
                    queue.append((x+1, y, rooms[x+1][y]))
                if x-1 >= 0 and rooms[x-1][y] > 0 and rooms[x-1][y] > dis+1:
                    rooms[x-1][y] = dis+1
                    queue.append((x-1, y, rooms[x-1][y]))
                if y+1 < N and rooms[x][y+1] > 0 and rooms[x][y+1] > dis+1:
                    rooms[x][y+1] = dis+1
                    queue.append((x, y+1, rooms[x][y+1]))
                if y-1 >= 0 and rooms[x][y-1] > 0 and rooms[x][y-1] > dis+1:
                    rooms[x][y-1] = dis+1
                    queue.append((x, y-1, rooms[x][y-1]))

    return rooms

print(walls_and_gates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))



def walls_and_gates_(rooms):
    if not rooms: 
        return
    
    queue = deque()
    
    for i in range(len(rooms)): 
        for j in range(len(rooms[0])): 
            if rooms[i][j]==0: 
                queue.append((i,j,0))
    
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while queue: 
        i,j, dist = queue.popleft()
        for x,y in dirs: 
            if 0<=i+x<len(rooms) and 0<=j+y<len(rooms[0]) and rooms[i+x][j+y] > dist+1: 
                rooms[i+x][j+y] = dist+1
                queue.append((i+x,j+y,dist+1))
    return rooms

print(walls_and_gates_([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))


# You are given a m x n 2D grid initialized with these three possible values.

# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# Example: 

# Given the 2D grid:

# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:

#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4