#coding=utf-8
#!/usr/bin/env python3

import queue
import urllib.request
from html.parser import HTMLParser
from urllib.parse import urljoin
import numpy as np
import socket
socket.setdefaulttimeout(1.0)

class Myparser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.AllLinks = []
    
    def handle_starttag(self, tag, attrs):
        if(tag=='a' and len(attrs)!=0):
            # go find ''' <a href="xyjj/xyjs.htm" title="学院介绍">学院介绍</a> '''
            for (key, value) in attrs:
                if(key=='href' and value!='#'):
                    if(".htm" in value):
                        self.AllLinks.append(value)

graph = {}
Markov = None
N = None

def BfsLinksWithDepth(MaxDepth, RootURL):
    global graph

    Q = queue.Queue()
    Q.put(RootURL)
    Depth = {RootURL: 1}
    graph = {RootURL: {}}
    

    while(not Q.empty()):
        now = Q.get()
        
        try:
            res = urllib.request.urlopen(now)
            res = res.read()
            res = res.decode('utf-8')
        except:
            continue
        
        parser = Myparser()
        parser.feed(res)

        for nxt in parser.AllLinks:
            realURL = urljoin(now, nxt)
            
            if(realURL!=now):
                if(realURL not in graph[now].keys()):
                    graph[now].update({realURL: 1})
                else:
                    graph[now][realURL] += 1

            if(realURL not in graph.keys()):
                graph.update({realURL: {}})
            
            if(realURL not in Depth.keys() and Depth[now] < MaxDepth):
                Depth.update({realURL: Depth[now] + 1})
                Q.put(realURL)

def GetMarkovMatrix():
    global graph, Markov, N
    N = len(graph)
    # print("shape of the Markov Matrix is {}".format(N))
    Markov = [[0 for j in range(N)] for i in range(N)]

    for key in graph.keys():
        i = list(graph.keys()).index(key)
        row_sum = 0.0
        for nxt in graph[key]:
            if(nxt not in graph.keys()):
                continue
            j = list(graph.keys()).index(nxt)
            n_j = graph[key][nxt]
            Markov[i][j] = n_j
            row_sum += n_j
        if(row_sum==0):
            Markov[i] = [1.0/N for j in range(N)]
        else:
            Markov[i] = [Markov[i][j] / row_sum for j in range(N)]
    
    Markov = np.array(Markov)

def PageRank(alpha, maxIter, K, RootURL):
    global Markov, graph, N

    A = alpha * Markov + (1-alpha)*1.0/N * np.ones((N, N))

    rootIdx = (list(graph.keys()).index(RootURL))
    P0 = [(i==rootIdx) for i in range(N)]
    
    P = np.array(P0)

    for i in range(maxIter):
        P = np.matmul(P, A)
    ansP = list(P)
    for i in range(N):
        ansP[i] = (ansP[i], list(graph.keys())[i])
    
    Res = sorted(list(ansP), reverse=True, key = lambda x:x[0])
    for i in Res[:K]:
        print("{}: {}".format(i[1], i[0]))


def main():
    rootURL = input()
    BfsLinksWithDepth(2, rootURL)
    GetMarkovMatrix()
    PageRank(0.85, 100, 20, rootURL)

if __name__=='__main__':
    main()
