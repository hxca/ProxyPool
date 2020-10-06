# ProxyPool

在 src/GetProxy.py 文件中添加爬取的代理 IP 函数。函数返回值为 `IP:port` 。

默认添加无忧代理的函数。其中 `order` 是在无忧代理购买代理 IP 后的订单号。
```python
    def data5u():
        order = ''
        url = 'http://api.ip.data5u.com/dynamic/get.html?order=&sep=3'.format(order)
        r = requests.get(url)
        return r.text.strip()
```



