import gevent
from gevent import monkey
monkey.patch_all()
import time
# jishi:
start=time.time()
import gevent
import requests
from gevent import Timeout



urls = ['http://www.google.com','http://wwww.baidu.com']
jobs = [gevent.spawn(requests.get,url) for url in urls]
tmp=gevent.joinall(jobs, timeout=2)
# print([i.value.text for i in tmp])  这么写来获得所有的返回数据

if len(tmp)!=len(urls):
    print("有某些client未返回数据,本次epoch失效")

else:
    print("epoch训练成功.")