#coding=utf-8
#!/usr/bin/env python3

import multiprocessing as mp
import os
import pickle
import queue
import re
import socket

import urllib.request
from html.parser import HTMLParser
from math import sqrt
from urllib.parse import urljoin

import numpy as np
from tqdm import tqdm

import jieba
import jieba.analyse as analyse

from gensim.models import word2vec




class Myparser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.Sensitive = ['title', 'p']
        self.AllLinks = []
        self.Title = None
        self.AllText = ""
        self.ProcessingTag = None
    
    def handle_starttag(self, tag, attrs):
        if(tag in self.Sensitive):
            self.ProcessingTag = tag

        if(tag=='a' and len(attrs)!=0):
            for (key, value) in attrs:
                if(key=='href' and value!='#'):
                    matching = re.match(r"(.*)news.sina.com.cn(.*)(20[0-9]{2}-[0-9]{2}-[0-9]{2})(.*)((html)|(shtml)|(php))", value)
                    if(matching is not None):
                        self.AllLinks.append(value)
    
    def handle_data(self, data):
        if(self.ProcessingTag == 'title'):
            self.Title = data
        elif(self.ProcessingTag == 'p'):
            self.AllText += data
    
    def handle_endtag(self, tag):
        if(self.ProcessingTag == tag):
            self.ProcessingTag = None

class System():
    def __init__(self):
        socket.setdefaulttimeout(1.0)
        self.DEPTH = 4
        self.ALPHA = 0.85
        self.ITERATION = 150
        self.TOPRANKRATE = 0.10 # PageRank top pages
        self.TOPRANKCOUNT = 25  # TextRank top words
        self.PKL = "./Info.pkl"
        self.SHOWRESULTNUM = 10
        self.MARGIN = 0.5
        
        
        self.rootURL = "https://news.sina.com.cn/"
        self.graph = {}
        self.Markov = None
        self.N = None
        self.Statistic = {}
        self.SkipWords = ["新浪", "新闻", "微信", "猛料", "二维码", "版权所有", "责任编辑", "报道", "邮箱", "扫描", "举报", "官方", "长安街", "知事"]
        self.TopRank = None
        self.TopRankDict = None
        self.model = word2vec.Word2Vec.load("word2vec_model")
        # TopRank = [ { "Title": "abcdef", 
        #               "Value": 0.012345,
        #               "URL": "https://www.baidu.com",
        #               "KeyWords": [("HoHoHo", 0.222), ("HaHaHa", 0.111)] }, {}, {}, ...... ]
        
        self.GetAllNewsInfo()

    def GetParsing(self, URL):
        try:
            res = urllib.request.urlopen(URL)
            res = res.read()
            res = res.decode('utf-8')
            parser = Myparser()
            parser.feed(res)
            return parser
        except:
            return None

    def BfsLinksWithDepth(self, MaxDepth, RootURL):
        print("******************** Spider Starting ********************")
        Q = queue.Queue()
        Q.put(RootURL)
        Depth = {RootURL: 1}
        self.graph = {RootURL: {}}
        

        while(not Q.empty()):
            now = Q.get()
            
            parser = self.GetParsing(now)
            if(parser==None):
                continue
            
            if(now == self.rootURL):
                parser.AllLinks.extend(["https://news.sina.com.cn/roll/",   "http://news.sina.com.cn/hotnews/",
                                        "https://news.sina.com.cn/china/",  "http://news.sina.com.cn/world/",       "http://mil.news.sina.com.cn/",
                                        "http://gov.sina.com.cn/",          "http://cul.news.sina.com.cn/"])

            for nxt in parser.AllLinks:
                realURL = urljoin(now, nxt)
                
                if(realURL!=now):
                    if(realURL not in self.graph[now].keys()):
                        self.graph[now].update({realURL: 1})
                    else:
                        self.graph[now][realURL] += 1

                if(realURL not in self.graph.keys()):
                    self.graph.update({realURL: {}})
                
                if(realURL not in Depth.keys() and Depth[now] < MaxDepth):
                    Depth.update({realURL: Depth[now] + 1})
                    Q.put(realURL)
        print("******************** Spider Finished ********************")
    
    def GetMarkovMatrix(self):
        print("******************** PageRank Starting ********************")
        self.N = len(self.graph)
        print("Total Number of Webpages is {}".format(self.N))
        self.Markov = [[0 for j in range(self.N)] for i in range(self.N)]

        for key in self.graph.keys():
            i = list(self.graph.keys()).index(key)
            row_sum = 0.0
            for nxt in self.graph[key]:
                if(nxt not in self.graph.keys()):
                    continue
                j = list(self.graph.keys()).index(nxt)
                n_j = self.graph[key][nxt]
                self.Markov[i][j] = n_j
                row_sum += n_j
            if(row_sum==0):
                self.Markov[i] = [1.0/self.N for j in range(self.N)]
            else:
                self.Markov[i] = [self.Markov[i][j] / row_sum for j in range(self.N)]
        
        self.Markov = np.array(self.Markov)
    
    def PageRank(self, alpha, maxIter, K, RootURL):
        Result = []

        A = alpha * self.Markov + (1-alpha)*1.0/self.N * np.ones((self.N, self.N))

        rootIdx = (list(self.graph.keys()).index(RootURL))
        P0 = [(i==rootIdx) for i in range(self.N)]
        
        P = np.array(P0)

        for i in tqdm(range(maxIter), desc="PageRanking"):
            P = np.matmul(P, A)
        ansP = list(P)
        for i in range(self.N):
            ansP[i] = (ansP[i], list(self.graph.keys())[i])
        
        Res = sorted(list(ansP), reverse=True, key = lambda x:x[0])
        min_pr = sqrt(Res[K-1][0])
        max_pr = sqrt(Res[0][0])

        def normalize(score):
            nonlocal min_pr, max_pr
            return (sqrt(score) - min_pr) / (max_pr - min_pr)

        for i in tqdm(Res[:K], desc="Getting Result"):
            Result.append({"Title": self.GetTitleFromURL(i[1]), "URL": i[1], "Value": normalize(i[0])})
        
        print("******************** PageRank Finished ********************")
        return Result # Length = K = TOPRANKRATE * N

    def GetTitleFromURL(self, URL):
        parser = self.GetParsing(URL)
        if(parser==None):
            return "GB2312 encoded, cannot resolve title!"
        return parser.Title

    def GetAllText(self, URL):
        parser = self.GetParsing(URL)
        if(parser==None):
            return ""
        parser.AllText = parser.AllText.replace(u'\u3000', u' ')
        return parser.AllText

    def GetKeyWords(self, URL):
        text = self.GetAllText(URL)
        AnaRes = jieba.analyse.textrank(text, self.TOPRANKCOUNT, withWeight=True, allowPOS=('n','nr','ns','nt','nz','nl','t','v','vn'))
        return AnaRes

    def GlobalStatistic(self, word, weight):
        if(word in self.SkipWords):
            return
        
        if(word not in self.Statistic):
            self.Statistic.update({word: weight})
        else:
            self.Statistic[word] += weight

    def SearchEngine(self, Query):

        def word_word_Distance(word1, word2):
            if(word1 in word2):
                return 1
            else:
                try:
                    score =self.model.wv.similarity(word1, word2)
                    score = (score if score > self.MARGIN else 0)
                    return score * 0.05
                except:
                    return word1 in word2

        def word_page_Distance(word, page):
            KeyWordsWithWeight = page["KeyWords"]   # [["aaa", 0.01], ["bbb", 0.001]]
            res = 0.0
            count = 0.0
            for wordBox in KeyWordsWithWeight:
                if(word in wordBox[0]):
                    count += 1
                tmp = wordBox[1] * word_word_Distance(word, wordBox[0])
                res += tmp
            return res, count
        
        seg_list = analyse.extract_tags(Query, 3, allowPOS=('n','nr','ns','nt','nz','nl','t','v','vn'))
        print("Query Splitted into : ", seg_list)
        ResultPage = [] # [ (dist, Title, count, reRank) ]
        
        self.TopRankDict = {}
        for page in self.TopRank:
            self.TopRankDict.update({page['Title']: [word[0] for word in page['KeyWords']]})
        
        for page in self.TopRank:
            tmp_result = [0, page["Title"], 0, 0]
            for word in seg_list:
                dist, count = word_page_Distance(word, page)
                tmp_result[0] += dist
                tmp_result[2] += count
                tmp_result[3] += (1 if(word in self.TopRankDict[page["Title"]][:5]) else 0)
            ResultPage.append(tuple(tmp_result))
        ResultPage.sort(reverse = True, key = lambda x: x[0])
        ResultPage.sort(reverse = True, key = lambda x: x[2])

        print("********** BEFORE Re-Ranking **********")
        for page in ResultPage[:self.SHOWRESULTNUM]:
            print(page[1], page[3])
        
        ResultPage.sort(reverse = True, key = lambda x: x[3])

        print("********** AFTER  Re-Ranking **********")
        for page in ResultPage[:self.SHOWRESULTNUM]:
            print(page[1], page[3])
        
        return ResultPage[:self.SHOWRESULTNUM]

    def GetAllNewsInfo(self):
        path = os.path.join(os.getcwd(), self.PKL)
        if(os.path.exists(path)):
            print("******************** Loading Info Existed ********************")
            with open(path, 'rb') as f:
                self.TopRank = pickle.load(f)
        
        else:
            print("******************** Generating Info from Spider ********************")
            self.BfsLinksWithDepth(self.DEPTH, self.rootURL)
            self.GetMarkovMatrix()
            self.TopRank = self.PageRank(self.ALPHA, self.ITERATION, int(self.TOPRANKRATE * self.N), self.rootURL)

            for i in tqdm(range(len(self.TopRank)), desc="Calculating Scores"):
                item = self.TopRank[i]
                ret = self.GetKeyWords(item['URL'])
                tmp = []
                for word in ret:
                    word_text = word[0]
                    score = word[1]
                    score = score * item['Value']       # KeyWord Score = Analysis * PageRank
                    tmp.append((word_text, score))
                tmp.sort(reverse=True, key=lambda x: x[1])
                item.update({'KeyWords': tmp})
        
            with open(self.PKL, 'wb') as f:
                pickle.dump(self.TopRank, f)

def main():

    Sina = System()

    for item in Sina.TopRank:
        for word in item['KeyWords']:
            word_text = word[0]
            score = word[1]
            Sina.GlobalStatistic(word_text, score)   # Gen Hot Words
    StatisticList = []
    for item in Sina.Statistic:
        StatisticList.append((item, Sina.Statistic[item]))
    TopWords = sorted(StatisticList, reverse=True, key = lambda x:x[1])
    
    print("Top 50 Hot Words are :")
    for i in range(50):
        print(TopWords[i][0], end=' ')
    print()


    # -------------------- Search Engine: Enter a Key Word --------------------
    print(Sina.SearchEngine(input()))


if __name__=='__main__':
    main()
