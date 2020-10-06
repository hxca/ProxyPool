# -*- coding:utf-8 -*-

from RedisClient import RedisClient


class Singleton(type):
    """
    Singleton Metaclass
    """

    _inst = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._inst:
            cls._inst[cls] = super(Singleton, cls).__call__(*args)
        return cls._inst[cls]


class DBClient(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.__init_db_client()

    def __init_db_client(self):
        host = "192.168.20.128"
        port = 6379
        password = ""
        self.client = RedisClient(host=host, port=port, password=password)

    def get(self, key):
        return self.client.get(key)

    def put(self, key_value):
        return self.client.put(key_value)

    def update(self, key_value):
        return self.client.update(key_value)

    def delete(self, key):
        return self.client.delete(key)

    def exists(self, key):
        return self.client.exists(key)

    def get_all(self):
        return self.client.get_all()

    def clear(self):
        return self.client.clear()

    def change_table(self, name):
        self.client.change_table(name)

    def get_number(self):
        return self.client.get_number()
