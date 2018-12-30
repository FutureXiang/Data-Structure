#coding=utf-8
#!/usr/bin/env python3

import logging
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

import jieba
import jieba.analyse as analyse
import numpy as np
from tqdm import tqdm

from gensim.models import word2vec
from Sina import System


def GetCorpus():
    Sina = System()
    Document = []

    for item in tqdm(Sina.TopRank, desc = "cutting", ascii=True):
        URL = item["URL"]
        text = Sina.GetAllText(URL)
        text_cut = jieba.cut(text)
        tmp = " ".join(text_cut)
        tmp = tmp.replace("举报 邮箱 ： jubao @ vip . sina . comCopyright   ©   1996 - 2018   SINA   CorporationAll   Rights   Reserved     新浪 公司   版权所有", "")
        tmp = tmp.replace("更 多 猛料 ！ 欢迎 扫描 左方 二维码 关注 新浪 新闻 官方 微信 （ xinlang - xinwen ） 违法 和 不良信息 举报电话 ： 010 - 62675637", "")
        tmp = tmp.replace("新浪 简介   ┊   About   Sina   ┊   广告 服务   ┊   联系 我们   ┊   招聘 信息   ┊   网站 律师   ┊   SINA   English   ┊   通行证 注册   ┊   产品 答疑", "")
        tmp = tmp.replace("\n", " ")
        tmp = tmp.replace("\t", " ")
        Document.append(tmp+"\n")
    Document = " ".join(Document)
    Document = Document.encode("utf-8", "ignore")
    with open('./Corpus.txt', 'wb') as f2:
        f2.write(Document)

def GetModel():
    if(not os.path.exists("./Corpus.txt")):
        GetCorpus()
    if(os.path.exists("./word2vec_model")):
        model = word2vec.Word2Vec.load("word2vec_model")
        return model
    else:
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        sentences = word2vec.LineSentence('./Corpus.txt') 
        model = word2vec.Word2Vec(sentences, hs=1, min_count=1, iter=10)
        model.save('./word2vec_model')
        return model



model = GetModel()
print(model.wv.similarity("落马", "反腐"))