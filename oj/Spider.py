#coding=utf-8
#!/usr/bin/env python3

import queue
import urllib.request
from html.parser import HTMLParser
from urllib.parse import urljoin

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



def main():
    rootURL = input()
    BfsLinksWithDepth(2, rootURL)
    print(len(graph.keys()))

if __name__=='__main__':
    main()
