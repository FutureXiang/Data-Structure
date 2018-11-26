N = int(input())
mat = [[0 for j in range(N)] for i in range(N)]

nodes = []

def get_id(string):
    if(string not in nodes):
        nodes.append(string)
    return nodes.index(string)

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
        mat[node_id][node_y_id] = weight

for i in range(N):
    for j in range(N):
        print(mat[i][j], end=' ')
    print()