# -*- coding:utf-8 -*-

import re
import requests


class CheckProxy(object):

    @staticmethod
    def verify_proxy_format(proxy):
        verify_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}"
        _proxy = re.findall(verify_regex, proxy)
        return True if len(_proxy) == 1 and _proxy[0] == proxy else False

    @staticmethod
    def valid_useful_proxy(proxy):
        proxies = {"http": "http://{}".format(proxy)}

        try:
            r = requests.get('http://www.baidu.com', proxies=proxies, timeout=30, verify=False)
            if r.status_code == 200:
                return True
        except Exception:
            pass
        return False
