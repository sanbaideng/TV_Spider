import csv
from os.path import abspath, join, dirname, exists
from sympy import true
import tqdm
import urllib3
from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk
import sys,json
# from handleM3u8t import *
from redisqueue import *
from spider import *
import peewee as pw
import pymysql

from utils import douban
# from flask import Flask, abort, request, jsonify
# from flask_cors import CORS
import concurrent.futures
import json

site_list = [
    "bdys01",
    "bttwoo",
    "cokemv",
    "czspp",
    "ddys",
    "dy555",
    "gitcafe",
    "lezhutv",
    "libvio",
    "onelist",
    "smdyy",
    "sp360",
    "voflix",
    "yiso",
    "zhaoziyuan"
]

myDB = pw.MySQLDatabase("movie", host="192.168.1.200", port=3306, user="root", passwd="yyxb716654052",charset='utf8')


client = Elasticsearch("http://localhost:9200")


def vod(wd,sites):
    try:
       
        # wd = request.args.get('wd')
        
        play = True
        flag = True
        

        # sites = request.args.get('sites')
        # ali_token = request.args.get('ali_token')
        # try:
        #     timeout = int(request.args.get('timeout'))
        # except Exception as e:
        timeout = 10

        # if not ali_token:
        ali_token = ""
 


        # 站点筛选
        search_sites = []
        if not sites or sites == "all":
            search_sites = site_list
        else:
            try:
                for site in sites.split(","):
                    if site in site_list:
                        search_sites.append(site)
            except Exception as e:
                print(e)
                search_sites = site_list
 

        # 搜索
        if wd:
            res = []
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(search_sites)) as executor:
                to_do = []
                for site in search_sites:
                    future = executor.submit(eval(f"{site}.searchContent"), wd, ali_token)
                    to_do.append(future)
                try:
                    for future in concurrent.futures.as_completed(to_do, timeout=timeout):  # 并发执行
                        # print(future.result())
                        res.extend(future.result())
                except Exception as e:
                    print(e)
                    import atexit
                    atexit.unregister(concurrent.futures.thread._python_exit)
                    executor.shutdown = lambda wait: None
            return res
 

        # 播放
        if play and flag:
            playerContent = eval(f"{play.split('___')[0]}.playerContent")(play, flag, ali_token)
            return playerContent

 

        # return jsonify({
        #     "list": search_sites
        # })
    except Exception as e:
        print(e)
        return []





if __name__ == '__main__':
    
    keyword = '生日快乐'
    dsl = {
            'query': {
                'match': {
                    'content': keyword
                }
            },
            
            'size':60
        }

    # result = client.search(index='my-index',  body=dsl, request_timeout=60*3)
    # jsonres = json.dumps(result.raw['hits']['hits'],ensure_ascii=False)

    # movieQueue = RedisQueue("movie")
    # for row in result["hits"]["hits"]:
    #     rowsource = row['_source']
    #     print(rowsource)
    #     print(rowsource["starttime"])
    #     print(rowsource["endtime"])
    #     print(rowsource["movieId"])
    #     moviename = movieQueue.getmovie(rowsource["movieId"]).decode('utf-8')
    #     moviechname = moviename.split('字幕下载')[0]
    #     print(moviechname)
    #     print(movieQueue.getmovie(rowsource["movieId"]).decode('utf-8'))
        
    res = vod('冰与火','all')
    # res = searchContent("大坏狐狸的故事", "")
    # res = detailContent('dy555$367659', "")
    # res = detailContent('dy555$363063', "")
    # res = playerContent("dy555___292787-1-1", "", "")
    # res = playerContent("dy555___363063-1-1", "", "")
    print(res)
