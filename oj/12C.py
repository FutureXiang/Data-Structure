#coding=utf-8
#!/usr/bin/env python3

N = 0
M = 0
edges_dict = {}
path = []
pathes = []
visit = []

def dfs(x):
    global N, path, visit, edges_dict, pathes
    if(x==N-1):
        pathes.append(path[:])

    for i in range(N):
        if(visit[i]==0 and (x, i) in edges_dict.keys()):
            for edge in edges_dict[(x, i)]:
                path.append(edge)
                visit[i] = 1
                dfs(i)
                path.pop()
                visit[i] = 0




def main():
    global N,M, visit, edges_dict, pathes
    
    inpline = input()
    N = int(inpline.split()[0])
    M = int(inpline.split()[1])
    for i in range(M):
        inpline = input()
        id = int(inpline.split()[0])
        x = int(inpline.split()[1])
        y = int(inpline.split()[2])
        if((x,y) not in edges_dict.keys()):
            edges_dict.update({ (x,y):[id], (y,x):[id] })
        else:
            edges_dict[(x,y)].append(id)
            edges_dict[(y,x)].append(id)
    visit = [0 for i in range(N)]
    visit[0] = 1
    dfs(0)

    pathes.sort()
    for path in pathes:
        for edge in path:
            print(edge,end=' ')
        print()

if __name__=='__main__':
    main()
