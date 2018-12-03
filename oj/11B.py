#coding=utf-8
#!/usr/bin/env python3

MAXN = 100
N = None
Graph = []
input_lines = []
S = None
T = None
D = None
INF = 2147483647

def readin():
    global N, Graph, D, S, T
    now = input()
    now_line = now.split()
    N = len(now_line)
    input_lines.append(now)

    for i in range(N-1):
        now = input()
        input_lines.append(now)
    
    temp = input()
    S = ord(temp.split()[0]) - ord('A')
    T = ord(temp.split()[1]) - ord('A')
    D = [[INF for j in range(N)] for i in range(N)]  # d[x][y] = INF

    for i in range(N):
        now_line = input_lines[i].split()
        for j in range(N):
            if(now_line[j]!="-1"):
                Graph.append([i,j,int(now_line[j])])
                D[i][j] = int(now_line[j])
    
    #print(Graph,S,T)

def floyd():
    global D
    global N
    for k in range(N):
            for i in range(N):
                for j in range(N):
                    D[i][j] = min(D[i][j], D[i][k] + D[k][j])


def main():
    readin()
    floyd()
    global D, S, T
    print(D[S][T])

if __name__=='__main__':
    main()

