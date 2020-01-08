# -*- coding:utf-8 -*-

import requests


class GetProxy(object):

    @staticmethod
    def data5u():
        order = ''
        url = 'http://api.ip.data5u.com/dynamic/get.html?order=&sep=3'.format(order)
        r = requests.get(url)
        return r.text.strip()
