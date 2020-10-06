# -*- coding:utf-8 -*-

import time
from Proxy import Proxy
from threading import Thread
from queue import Queue, Empty
from CheckProxy import CheckProxy
from ProxyManager import ProxyManager


class UsefulProxyCheck(ProxyManager, Thread):

    def __init__(self, queue, thread):
        ProxyManager.__init__(self)
        Thread.__init__(self)

        self.__queue = queue

    def run(self):

        self.db.change_table(self.useful_proxy_queue)

        while True:

            try:
                proxy_json = self.__queue.get(block=False)
            except Empty as e:
                break

            proxy_obj = Proxy.new_proxy_from_json(proxy_json)
            status = CheckProxy.valid_useful_proxy(proxy_obj.proxy)

            if status:
                proxy_obj.checkout_time = time.strftime("%Y-%m-%d %H:%M:%S")
                self.db.update(proxy_obj)
                print("Update proxy: {} checkout time.".format(proxy_obj.proxy))
            else:
                print("Proxy: {} is not used.".format(proxy_obj.proxy))
                self.db.delete(proxy_obj.proxy)
            self.__queue.task_done()


def do_useful_proxy_check():
    proxy_queue = Queue()
    pm = ProxyManager()

    pm.db.change_table(pm.useful_proxy_queue)
    for proxy_ in pm.db.get_all():
        proxy_queue.put(proxy_)

    thread_list = list()
    for thread_index in range(5):
        thread_list.append(UsefulProxyCheck(proxy_queue, "thread_{}".format(thread_index)))

    for thread_ in thread_list:
        thread_.start()

    for thread_ in thread_list:
        thread_.join()


if __name__ == '__main__':
    do_useful_proxy_check()
