from collections import deque
def bfs(x,y):
    queue = deque([])
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= se or ny < 0 or ny >= ga: continue
            if graph[nx][ny] == 0: continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[se - 1][ga - 1]

se,ga = map(int,input().split())
graph = []
for _ in range(se):
    graph.append(list(map(int,input())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
print(bfs(0,0))
