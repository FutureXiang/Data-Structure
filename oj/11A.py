#coding=utf-8
#!/usr/bin/env python3

MAXN = 100
N = None
Graph = []
input_lines = []
fa = []

def readin():
    global N
    global Graph
    global fa
    try:
        while(True):
            now = input()
            if(now==""):
                break
            input_lines.append(now)
    except EOFError:
        pass

    N = len(input_lines)
    for i in range(N):
        now_line = input_lines[i].split()
        for j in range(N):
            if(now_line[j]!="-1" and ([j,i,int(now_line[j])] not in Graph)):
                Graph.append([i,j,int(now_line[j])])
    fa = [i for i in range(N)]


def find_fa(now):
    if(now!=fa[now]):
        fa[now]= find_fa(fa[now])
        return fa[now]
    else:
        return fa[now]

def kruskal():
    global N
    global Graph
    Graph.sort(key = lambda x:x[2])
    #print(Graph)
    ANS = 0

    for edge in Graph:
        x = edge[0]
        y = edge[1]
        w = edge[2]
        fx = find_fa(x)
        fy = find_fa(y)
        #print("{}:{}, {}:{}".format(x,fx,y,fy))
        if(fx!=fy):
            ANS += w
            fa[fy] = fx
    return ANS

def main():
    readin()
    print(kruskal())

if __name__=='__main__':
    main()

