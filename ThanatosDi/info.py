import asyncio
import json
import re

import aiohttp
from flask import Flask

app = Flask(__name__)

class HTTPClientError(Exception):
    def __str__(self):
        return 'HTTPClient Error'

class HTTPClient:
    def __init__(self, loop):
        self._session = aiohttp.ClientSession(loop=loop)

    async def request(self, method:str, url:str, data=None, headers=None):
        try:
            async with self._session.request(method.upper(), url, data=data, headers=headers, timeout=5) as resp:
                if resp.status!=200:
                    raise HTTPClientError('無法與伺服器連線，可能伺服器正在維護中')
                return (await resp.text())
        except Exception as e:
            return f'無法與伺服器連線，可能伺服器正在維護中'
    
    def close(self, loop):
        async def close():
            if not self._session.closed:
                await self._session.close()
        loop.run_until_complete(close())

class INFO:
    API = 'https://api-pc.so-net.tw/'
    HOST = 'http://127.0.0.1:8000/info/'

    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.HTTPClient = HTTPClient(self.loop)

    def make_request(self, method, endpoint, data=None ):
        headers = {
            'X-Requested-With': 'tw.sonet.princessconnect',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G955N Build/LYZ28N) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36',
            'Referer': 'https://api-pc.so-net.tw/information/index/0/1/10/1'
        }
        resp = self.loop.run_until_complete(self.HTTPClient.request(method, url=self.API+endpoint, data=data, headers=headers))
        return resp

client = INFO()

@app.route('/info/')
@app.route('/info/index')
def index():
    endpoint = 'information/index/0/1/'
    resp = client.make_request('get', endpoint)
    resp = resp.replace('https://api-pc.so-net.tw/information/', client.HOST)
    resp = re.sub(r'/1/10/[\d]+\?list_category=[\d]+&rnd=[\d]+', '', resp)
    return resp

@app.route(f'/info/detail/<int:postid>')
def detail(postid):
    endpoint = f'information/detail/{postid}/'
    resp = client.make_request('get', endpoint)
    resp = resp.replace('https://api-pc.so-net.tw/information/', client.HOST)
    resp = re.sub(r'/0\?rnd=[\d]+', '', resp)
    return resp

if __name__ == "__main__":
    app.run(port=8000, debug=True)
