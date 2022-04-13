import main
import pickle
import numpy as np
import re
from eunjeon import Mecab

reg1 = re.compile(r'https?://[a-zA-Z0-9_/:%#\$&\?\(\)~\.=+-]*') # url -> 삭제
reg2 = re.compile(r'(@)[a-zA-Z0-9_]*:*') # 계정 태그(@아이디) -> 삭제
reg3 = re.compile(r'(\d)([,.])(\d+)') # 숫자.숫자 -> 1.1로 변환
reg4 = re.compile(r'\d+') # 숫자 여러개 -> 1 하나로 줄임
reg5 = re.compile(r'[\r\n\t]+') # 줄바꿈, 탭 -> 공백으로 변환
reg6 = re.compile(r'[\.・…,]+') # 물음표/느낌표 제외 문장부호들 -> .으로 통일 
reg7 = re.compile(r'[?]+') # 물음표 여러개 -> 물음표 1개로 줄임
reg8 = re.compile(r'[!]+') # 느낌표 여러개 -> 느낌표 1개로 줄임
reg9 = re.compile(r'[\[{「〈【［≪《〔＜｛『]+') # 이렇게 생긴 문장부호들 -> <으로 통일
reg10 = re.compile(r'[\]}」〉】］≫》〕＞｝』]+') # 이렇게 생긴 문장부호들 -> >으로 통일
symbol = ['「','」','.','?','!']


# 트윗 텍스트에서 불필요한 부분 제거 및 변환
def parge_tweet(tweet):
    # t = neologdn.normalize(t).lower()
    t = tweet
    t = reg1.sub('', t)
    t = reg2.sub('', t)
    t = reg3.sub(r'\1\3', t)
    t = reg4.sub('1', t)
    t = reg5.sub(' ', t)
    t = reg6.sub('.',t)
    t = reg7.sub('?', t)
    t = reg8.sub('!', t)
    t = reg9.sub('<',t)
    t = reg10.sub('>',t)
    return t

def tweet2wak(tweet):
    t = parge_tweet(tweet)
    return t #txt2wak(t)

# list of Tweet -> array of tokens
def tweets2tokens(tweets):
    # mecab.morphs("형태소로 분리해줌")
    """mecab = Mecab()
    # print(mecab.morphs(tweets))
    for tweet in tweets:
        print(mecab.morphs(tweet))
        print(mecab.tagger(tweet))"""
    
    for tw in tweets:
        print("tw: ", tw)
        w = tweet2wak(tw)
        print("w : ", w)
        

# receive list of Tweet and return list of tag of those 
def classify_tweets(twts):
    toks = tweets2tokens(twts) # 트윗->토큰 변환
    return toks











"""tweets_by_disaster = {
    "typhoon" : [],
    "downpour" : [],
    "snow" : [],
    "gale" : [],
    "drought" : [],
    "forestfire" : [],
    "earthquake" : [],
    "coldwave" : [],
    "heatwave" : [],
    "dust" : []
}

def classify_tweets(tweet_all):

    for tweet in tweet_all:
        
        if any(disaster in tweet["text"] for disaster in main.queries_typhoon):
            print("태풍 관련 트윗이다.")
            tweets_by_disaster["typhoon"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_downpour):
            print("폭우 관련 트윗이다.")
            tweets_by_disaster["downpour"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_snow):
            print("폭설 관련 트윗이다.")
            tweets_by_disaster["snow"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_gale):
            print("강풍 관련 트윗이다.")
            tweets_by_disaster["gale"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_drought):
            print("가뭄 관련 트윗이다.")
            tweets_by_disaster["drought"].append(tweet)
        
        elif any(disaster in tweet["text"] for disaster in main.queries_forestfire):
            print("산불 관련 트윗이다.")
            tweets_by_disaster["forestfire"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_earthquake):
            print("지진 관련 트윗이다.")
            tweets_by_disaster["earthquake"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_coldwave):
            print("한파 관련 트윗이다.")
            tweets_by_disaster["coldwave"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_heatwave):
            print("폭염 관련 트윗이다.")
            tweets_by_disaster["heatwave"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_dust):
            print("미세먼지 관련 트윗이다.")
            tweets_by_disaster["dust"].append(tweet)

        else:
            print("무관한 트윗이다.")

    return tweets_by_disaster
"""