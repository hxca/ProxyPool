# -*- coding:utf-8 -*-

import json


class Proxy(object):

    def __init__(self, proxy, create_time="", checkout_time="", source=""):
        self.__proxy = proxy
        self.__create_time = create_time
        self.__checkout_time = checkout_time
        self.__source = source

    @classmethod
    def new_proxy_from_json(cls, proxy_json):
        proxy_dict = json.loads(proxy_json)
        return cls(
            proxy=proxy_dict['proxy'],
            create_time=proxy_dict['create_time'],
            checkout_time=proxy_dict['checkout_time'],
            source=proxy_dict['source']
        )

    @property
    def proxy(self):
        return self.__proxy

    @property
    def create_time(self):
        return self.__create_time

    @create_time.setter
    def create_time(self, value):
        self.__create_time = value

    @property
    def checkout_time(self):
        return self.__checkout_time

    @checkout_time.setter
    def checkout_time(self, value):
        self.__checkout_time = value

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        self.__source = value

    @property
    def info_dict(self):
        return {
            "proxy": self.__proxy,
            "create_time": self.__create_time,
            "checkout_time": self.__checkout_time,
            "source": self.__source
        }

    @property
    def info_json(self):
        return json.dumps(self.info_dict)
