inp = input().split()
N = int(inp[0])
Target = inp[1]
mat = [[] for i in range(N)]

nodes = []

def get_id(string):
    if(string not in nodes):
        nodes.append(string)
    return nodes.index(string)


Visit = [0 for i in range(N)]
ans = []
bad = []
path = []

def dfs(Source, now):
    global Visit
    global path

    if(now == Target):
        return

    count_nxt = 0
    for next in mat[now]:
        if(Visit[next]==1): # can form a cycle
            bad.append(nodes[Source])
        if(Visit[next]==0):
            count_nxt += 1
            
            path.append(next)
            Visit[next] = 1
            dfs(Source, next)
            path.remove(next)
            Visit[next] = 0
    
    if(count_nxt==0): # terminal of a path
        if(Target not in path):
            bad.append(nodes[Source])


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

        if(node_y_id not in mat[node_id]): # 去重边
            mat[node_id].append(node_y_id)



Target = get_id(Target)

for Source in range(N):
    if(Source==Target):
        continue
    
    path = [Source]
    Visit[Source] = 1
    
    dfs(Source, Source)
    
    Visit = [0 for i in range(N)]
    path = []

for node in nodes:
    if(node not in bad and node!=nodes[Target]):
        ans.append(node)

if(ans!=[]):
    print(" ".join(sorted(ans)))
else:
    print("None")