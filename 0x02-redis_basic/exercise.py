#!/usr/bin/env python3
''' redis module '''
import uuid
import redis
from typing import Any, Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    ''' calls counter'''
    @wraps(method)
    def inner(self, *args, **kwargs):
        ''' decorated function '''
        self._redis.incr(method.__qualname__, 1)
        return method(self, *args, **kwargs)
    return inner


def call_history(method: Callable) -> Callable:
    ''' call history'''
    @wraps(method)
    def inner(self, *args, **kwargs):
        ''' decorated function '''
        input = str(args)
        # for v in args:
        #     input.append(v if type(v) in [str, int, bytes] else str(v))
        self._redis.rpush("{}:inputs".format(method.__qualname__), input)
        output = method(self, *args, **kwargs)
        self._redis.rpush(
            "{}:outputs".format(method.__qualname__), output)
        return output
    return inner


def replay(fn: Callable) -> None:
    ''' prints call history '''
    r = fn.__self__._redis
    key = fn.__qualname__
    count = int(r.get(key) or 0)
    print('{} was called {} times:'.format(key, count))

    if not count:
        return

    inputs = r.lrange("{}:inputs".format(key), 0, -1)
    outputs = r.lrange("{}:outputs".format(key), 0, -1)

    for args, res in zip(inputs, outputs):
        print('{}(*{}) -> {}'.format(key, args.decode(), res.decode()))


class Cache:
    ''' cache class '''
    def __init__(self) -> None:
        ''' class constructor '''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' stores data '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        ''' gets data '''
        v: Any = self._redis.get(key)
        return fn(v) if fn is not None and v is not None else v

    def get_int(self, key: str) -> int:
        ''' gets integer '''
        return self.get(key, int)

    def get_str(self, key: str) -> int:
        ''' gets string '''
        return self.get(key, bytes.decode)
