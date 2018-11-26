inp = input().split()
N = int(inp[0])
Source = inp[1]
mat = [[] for i in range(N)]

nodes = []

def get_id(string):
    if(string not in nodes):
        nodes.append(string)
    return nodes.index(string)

INF = 2147483647

dist = [[INF for j in range(N)] for i in range(N)]  # d[x][y] = INF

def floyd():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(N):
    inp = input()
    node = inp.split(':')[0]
    nxts = inp[len(node)+1:]

    node_id = get_id(node)

    nxts = nxts[2:len(nxts)-1]
    nxts = nxts.split(',')
    for j in range(len(nxts)):
        info = nxts[j] if j==0 else nxts[j][1:]
        node_y = info.split(":")[0]
        weight = int(info.split(":")[1])
        node_y_id = get_id(node_y)

        mat[node_id].append(node_y_id)
        dist[node_id][node_y_id] = weight   # d[x][y] = weight
        dist[node_id][node_id] = 0          # d[x][x] = 0

Source = get_id(Source)

floyd()

ans = 0
for i in range(N):
    ans = max(ans, dist[Source][i])

print(ans)