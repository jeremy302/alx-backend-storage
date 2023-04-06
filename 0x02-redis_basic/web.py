#!/usr/bin/env python3
''' redis module '''
import redis
from typing import Any, Union, Callable, Optional
from functools import wraps
import requests

store = redis.Redis()


def cache(fn: Callable) -> Callable:
    ''' caches procedure '''
    @wraps(fn)
    def inner(*args, **kwargs):
        ''' inner procedure '''
        store.incr("count:{}".format(args[0]))
        cache_key = "cache:{}".format(args[0])
        res = store.get(cache_key)
        if res is not None:
            return res.decode()
        res = fn(*args, **kwargs)
        store.set(cache_key, res, ex=10)
        return res
    return inner


@cache
def get_page(url: str) -> str:
    ''' gets page '''
    res = requests.get(url)
    return res.text


# @cache
# def get_page(url: str) -> str:
#     ''' mock get_page '''
#     import datetime
#     return 'abc'+url + str(datetime.datetime.now())
