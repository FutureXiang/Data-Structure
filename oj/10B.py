inp = input().split()
N = int(inp[0])
Source = inp[1]
mat = [[] for i in range(N)]

nodes = []

def get_id(string):
    if(string not in nodes):
        nodes.append(string)
    return nodes.index(string)


Visit = [0 for i in range(N)]

def dfs(now):
    global Visit
    print(nodes[now], end=' ')
    for next in mat[now]:
        if(Visit[next]==0):
            Visit[next] = 1
            dfs(next)


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

Source = get_id(Source)
Visit[Source] = 1
dfs(Source)