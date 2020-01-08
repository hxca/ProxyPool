# -*- coding-8 -*-

import RawProxyCheck
import UsefulProxyCheck
from ProxyManager import ProxyManager
from apscheduler.schedulers.blocking import BlockingScheduler


class DoFetchProxy(ProxyManager):

    def __init__(self):
        ProxyManager.__init__(self)

    def main(self):
        self.fetch()


def raw_proxy_scheduler():
    do_fetch_proxy = DoFetchProxy()
    do_fetch_proxy.main()
    RawProxyCheck.do_raw_proxy_check()


def useful_proxy_check():
    UsefulProxyCheck.do_useful_proxy_check()


def run_scheduler():
    raw_proxy_scheduler()
    useful_proxy_check()

    scheduler = BlockingScheduler(timezone="Asia/Shanghai")
    scheduler.add_job(raw_proxy_scheduler, 'interval', minutes=1, id='raw_proxy_scheduler')
    scheduler.add_job(useful_proxy_check, 'interval', minutes=1, id='useful_proxy_scheduler')

    scheduler.start()


if __name__ == '__main__':
    run_scheduler()
