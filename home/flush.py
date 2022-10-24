import redis
import os

pw = os.environ['REDIS_PW']

def flush_cache():
    for i in range(1, 8):
        client = redis.Redis(host='localhost', port=6379, password=pw, db=i)
        client.flushdb()