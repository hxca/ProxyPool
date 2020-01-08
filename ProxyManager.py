# -*- coding:utf-8 -*-

import time
import random
from Proxy import Proxy
from GetProxy import GetProxy
from DBClient import DBClient
from CheckProxy import CheckProxy

PROXY_GETTER = [
    'data5u'
]

TIME_COUNT = 5


class ProxyManager(object):

    def __init__(self):
        self.db = DBClient()
        self.raw_proxy_queue = "raw_proxy"
        self.useful_proxy_queue = "useful_proxy"

    def fetch(self):
        proxy_set = set()
        self.db.change_table(self.raw_proxy_queue)
        for proxy_getter_item in PROXY_GETTER:

            try:
                proxy = getattr(GetProxy, proxy_getter_item.strip())()
                if not proxy or not CheckProxy.verify_proxy_format(proxy):
                    print("Proxy: {} format is error.".format(proxy))
                elif proxy in proxy_set:
                    print("Proxy: {} is exist.".format(proxy))
                else:
                    create_time = time.strftime("%Y-%m-%d %H:%M:%S")
                    checkout_time = time.strftime("%Y-%m-%d %H:%M:%S")
                    source = proxy_getter_item.strip()
                    self.db.put(Proxy(proxy=proxy, create_time=create_time, checkout_time=checkout_time, source=source))
                    proxy_set.add(proxy)

            except Exception as e:
                print(e)
            time.sleep(TIME_COUNT)

    def get(self):
        self.db.change_table(self.useful_proxy_queue)
        item_list = self.db.get_all()

        if item_list:
            random_choice = random.choice(item_list)
            return Proxy.new_proxy_from_json(random_choice)
        else:
            return None

    def delete(self, proxy_str):
        self.db.change_table(self.useful_proxy_queue)
        self.db.delete(proxy_str)

    def get_all(self):
        self.db.change_table(self.useful_proxy_queue)
        item_list = self.db.get_all()
        return [Proxy.new_proxy_from_json(x) for x in item_list]

    def get_number(self):
        self.db.change_table(self.raw_proxy_queue)
        total_raw_proxy = self.db.get_number()

        self.db.change_table(self.useful_proxy_queue)
        total_useful_proxy = self.db.get_number()

        return {
            "raw_proxy": total_raw_proxy,
            "useful_proxy": total_useful_proxy
        }

    def clear(self):
        self.db.change_table(self.useful_proxy_queue)
        self.db.clear()

        self.db.change_table(self.raw_proxy_queue)
        self.db.clear()


def main():
    pp = ProxyManager()
    pp.clear()

    for x in range(3):
        pp.fetch()

    print("-------------------------------------------")

    item_dict = pp.get_all()
    print(item_dict)

    for proxy_item in item_dict:
        print(proxy_item.proxy)


if __name__ == '__main__':
    main()
