import redis
class RedisQueue(object):
    def __init__(self, name, namespace='queue', **redis_kwargs):
        self.__db = redis.Redis(host='192.168.1.200', port=6379, db=8, password=None)
        self.key = f"{name,namespace}"
        # self.headerkey = f"{name+'header',namespace}"

    # 返回队列大小
    def qsize(self):
        return self.__db.llen(self.key)

    # 判断队列用尽
    def empty(self):
        return self.qsize() == 0

    # rpush进去或者lpush都可以
    def put(self, item):
        self.__db.rpush(self.key, item)

    # get出来
    def get(self, block=True, timeout=None):
        if block:
            item = self.__db.blpop(self.key, timeout=timeout)
        else:
            item = self.__db.lpop(self.key)
        return item

    def get_nowait(self):
        return self.get(False)

    def autherexsit(self,uname):
        return self.__db.sismember(self.key,uname)
    def headerexsit(self,uname):
        return self.__db.sismember(self.key,uname)
    def putauthor(self,uname):
        self.__db.sadd(self.key,uname)


    def adderrurl(self,url):
        self.__db.sadd(self.key,url)
    def geterrurl(self):
        return self.__db.spop(self.key)
    def delerrurl(self,url):
        self.__db.srem(self.key,url)

    def addundoauthor(self,author):
        self.__db.rpush(self.key,author)
    def popundoauthor(self):
        return self.__db.lpop(self.key)
    
    def addmovie(self,id,name):
        self.__db.hsetnx(self.key,id,name)
    def getmovie(self,id):
        return self.__db.hget(self.key,id)