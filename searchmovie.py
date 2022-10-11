import spider
from redisqueue import *

import peewee as pw
import pymysql
myDB = pw.MySQLDatabase("movie", host="192.168.1.200", port=3306, user="root", passwd="yyxb716654052",charset='utf8')
class MySQLModel(pw.Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = myDB
class Movie(MySQLModel):
    id = pw.IntegerField()
    name = pw.CharField()
    score = pw.CharField()
    subtitleUrl = pw.CharField()
    pageNo = pw.CharField()
    language = pw.CharField()
    movieType = pw.CharField()
    fileFolder = pw.CharField()
    subtitleName = pw.CharField()
    zipfileName = pw.CharField()
    threadname = pw.CharField()
    subtitlestatus = pw.CharField()
 #https://apid.13to.com/m3/5a9fcad1665419627/91Q2hyb21lJGh0dHBzOi8vd3d3LmJ0dHdvby5jb20vd3AtY29udGVudC91cGxvYWRzLzIwMjIvMDgvNTg4OTMyMWZlY2VkMTgubTN1OCQxNjY1MzkwNzI36343d88732ffb.m3u8 --downloadRange 100-200
 
# import subprocess
# nowtime = subprocess.Popen('date', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

# print("nowtime.stdout.read(): {}\n".format(nowtime.stdout.read()))


# import os
# os.system("ipconfig")

# import os
# d = os.popen("N_m3u8DL-CLI_v3.0.2 https://apid.13to.com/m3/5a9fcad1665419627/91Q2hyb21lJGh0dHBzOi8vd3d3LmJ0dHdvby5jb20vd3AtY29udGVudC91cGxvYWRzLzIwMjIvMDgvNTg4OTMyMWZlY2VkMTgubTN1OCQxNjY1MzkwNzI36343d88732ffb.m3u8 --downloadRange 100-110")
# print(d.read())
# https://apid.13to.com/m3/cffccdb1665501292/76Q2hyb21lJGh0dHBzOi8vd3d3LmJ0dHdvby5jb20vd3AtY29udGVudC91cGxvYWRzLzIwMjIvMDgvNTg4OTMyMWZlY2VkMTgubTN1OCQxNjY1NDcyMzky63451788461ad.m3u8

# import subprocess
# result = subprocess.Popen("N_m3u8DL-CLI_v3.0.2 https://apid.13to.com/m3/cffccdb1665501292/76Q2hyb21lJGh0dHBzOi8vd3d3LmJ0dHdvby5jb20vd3AtY29udGVudC91cGxvYWRzLzIwMjIvMDgvNTg4OTMyMWZlY2VkMTgubTN1OCQxNjY1NDcyMzky63451788461ad.m3u8 --downloadRange 100-110", shell=True,
#                           stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True)
# output,error = result.communicate()
# print (output)
movieQueue = RedisQueue("movie")
# movieQueue.addmovie(1,'这个杀手不太冷')
# movieQueue.addmovie(2,'2打分')
# moviename = movieQueue.getmovie(1).decode('utf-8')
# print(moviename)

# query = Movie.select()
# for m in query:
#     movieQueue.addmovie(m.id,m.name)