from django.shortcuts import render
import redis
import json
from django.conf import settings
from datetime import timedelta


client_redis = redis.Redis(host=settings.REDIS_HOST,
                           port=settings.REDIS_PORT,
                           db=settings.REDIS_DB)


def intialize_views(request):

    client_redis.set('views', json.dumps({0: []}))
    return render(request, 'mohsen.html')

def add_views(request):

    views = client_redis.get('views')
    views = json.loads(views)
    keys = views.keys()
    key_iter = iter(keys)
    f_key = next(key_iter)
    views_ls = views[f_key]
    views_ls.append("one")
    f_key = int(f_key) + 1
    client_redis.set('views', json.dumps({f_key: views_ls}))
    return render(request, 'mohsen.html')

def expire_views(request):

    client_redis.expire('views', timedelta(seconds=20))
    return render(request, 'mohsen.html')

def expire_at(request): #wrong function

    client_redis.expireat('views', '2022-1-28 13:00:00')
    return render(request, 'mohsen.html')