# -*- coding:utf-8 -*-

from redis import Redis, BlockingConnectionPool


class RedisClient(object):

    def __init__(self, **kwargs):
        self.name = None
        self.__conn = Redis(connection_pool=BlockingConnectionPool(**kwargs))

    def get(self, proxy_str):

        data = self.__conn.hget(name=self.name, key=proxy_str)
        if data:
            return data
        else:
            return None

    def put(self, proxy_obj):

        data = self.__conn.hset(name=self.name, key=proxy_obj.proxy, value=proxy_obj.info_json)
        return data

    def delete(self, proxy_str):
        self.__conn.hdel(self.name, proxy_str)

    def exists(self, proxy_str):
        return self.__conn.hexists(self.name, proxy_str)

    def update(self, proxy_obj):
        self.__conn.hset(self.name, proxy_obj.proxy, proxy_obj.info_json)

    def get_all(self):
        item_dict = self.__conn.hgetall(self.name)
        return [value.decode('utf8') for key, value in item_dict.items()]

    def clear(self):
        return self.__conn.delete(self.name)

    def get_number(self):
        return self.__conn.hlen(self.name)

    def change_table(self, name):
        self.name = name


a = dict()
a.values()

def main():
    pass


if __name__ == '__main__':
    main()
