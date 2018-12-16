from collections import deque


visit = [0 for i in range(300)]
dis = [2147483647 for i in range(300)]
path = [[] for i in range(300)]

station = {}
edges = []


def ShortestPath(S):
    Q = deque()
    Q.append(S)
    global visit, edges, dis
    visit[S] = 1
    dis[S] = 0
    path[S] = []
    while(len(Q)!=0):
        now = Q.popleft()
        for edge in edges:
            if(edge[0]==now):
                to = edge[1]
            elif(edge[1]==now):
                to = edge[0]
            else:
                continue
            
            if(dis[now] + 1 < dis[to]):
                dis[to] = dis[now] + 1
                path[to] = path[now] + [(now, to, edge[2])]
                if(visit[to]==0):
                    if(dis[to]<=dis[now]):
                        Q.appendleft(to)
                    else:
                        Q.append(to)
                    visit[to] = 1
        visit[now] = 0
    return 


def ReadFile():
    with open("bgstations_pinyin.txt") as f:
        total = f.readline()
        total = int(total)
        for i in range(total):
            if(i!=0):
                wasted = f.readline()
            info = f.readline()
            No = int(info.split()[0])
            StationsCnt = int(info.split()[1])
            tmpIDlist = []
            for i in range(StationsCnt):
                aStation = f.readline()
                name = aStation.split()[0]
                transit = int(aStation.split()[1])
                if(name not in station.keys()):
                    station.update({name:[transit, No]})
                tmpIDlist.append(list(station.keys()).index(name))
            for i in range(len(tmpIDlist)):
                if(i!=len(tmpIDlist)-1):
                    edges.append([tmpIDlist[i], tmpIDlist[i+1], No])


def main():

    ReadFile()

    Source = input()
    Target = input()
    Sid = list(station.keys()).index(Source)
    Tid = list(station.keys()).index(Target)
    ShortestPath(Sid)

    ansPath = path[Tid]
    simPath = []

    for i in range(len(ansPath)):
        a,b,c = ansPath[i]
        if(simPath==[]):
            simPath.append((a,b,c,1))
        else:
            x,y,z,u = simPath[-1]
            if(c!=z):
                simPath.append((a,b,c,1))
            else:
                simPath[-1] = (x,b,z, u+1)
    
    for item in simPath:
        s,t,l,c = item
        print("{}-{}({})-".format(list(station.keys())[s], l, c), end='')
    print(Target)

if __name__=='__main__':
    main()
