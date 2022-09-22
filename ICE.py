def dfs(x,y):
    if x < 0 or x >= se or y < 0 or y >= ga:
        return False
    if ices[x][y] == 0:
        ices[x][y] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

se,ga = map(int,input().split())
ices = []
cnt = 0
for _ in range(se):
    ices.append(list(map(int,input())))
for i in range(se):
    for j in range(ga):
        if dfs(i,j) == True: cnt += 1

print(cnt)
