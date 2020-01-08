# -*- coding:utf-8 -*-

from flask import Flask, jsonify, request
from werkzeug.wrappers import Response

from ProxyManager import ProxyManager


class JsonResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, (dict, list)):
            response = jsonify(response)

        return super(JsonResponse, cls).force_type(response, environ)


app = Flask(__name__)
app.response_class = JsonResponse

api_list = {
    'get': u'get an useful proxy',
    # 'refresh': u'refresh proxy pool',
    'get_all': u'get all proxy from proxy pool',
    'delete?proxy=127.0.0.1:8080': u'delete an unable proxy',
    'get_status': u'proxy number'
}


@app.route('/')
def index():
    return api_list


@app.route('/get/')
def get():
    proxy = ProxyManager().get()
    return proxy.info_json if proxy else {"code": 0, "src": "no proxy"}


@app.route('/get_all/')
def get_all():
    proxies = ProxyManager().get_all()
    return jsonify([_.info_dict for _ in proxies])


@app.route('/delete/', methods=['GET'])
def delete():
    proxy = request.args.get('proxy')
    ProxyManager().delete(proxy)
    return {"code": 0, "src": "success"}


@app.route('/get_status/')
def get_status():
    status = ProxyManager().get_number()
    return status


def run_flask():
    app.run(host='192.168.20.128', port=5010)


if __name__ == '__main__':
    run_flask()
