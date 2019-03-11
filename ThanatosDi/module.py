import base64
from random import randint

import requests #requests
from Crypto.Cipher import AES #pycryptodome


class AESCBC:
    """AES decrypt and encrypt function. AES.decrypt(key, iv, data), AES.encrypt(key, iv, data)"""

    def __init__(self):
        print(
            """AES decrypt and encrypt function.
    AESCBC.decrypt(key:bytes, iv:bytes, data:bytes)
        decrypt data.
    AESCBC.encrypt(key:bytes, iv:bytes, data:bytes)
        encrypt data
    AESCBC.b(s:str)
        convert s(str) to bytes"""
    )

    @staticmethod
    def decrypt(key, iv, data):
        try:
            cryptor = AES.new(key, AES.MODE_CBC, iv)
            new = cryptor.decrypt(data)
            return new
        except Exception as e:
            return print(f'AESCBC.decrypt : {str(e)}')

    @staticmethod
    def encrypt(key, iv, data):
        try:
            cryptor = AES.new(key, AES.MODE_CBC, iv)
            new = cryptor.encrypt(data)
            return new
        except Exception as e:
            return print(f'AESCBC.encrypt : {str(e)}')

    @staticmethod
    def b(s: str):
        try:
            return str.encode(s)
        except Exception as e:
            return print(f'string.b : {str(e)}')


class B64:
    """ base64 encode and decode function. """

    def __init__(self):
        print("""base64 encode and decode function.\n   B64.encode(s:str)\n   B64.decode(s:str)""")

    @staticmethod
    def encode(s:str):
        """ encode string to base64 """
        try:
            return base64.b64encode(str(s))
        except Exception as e:
            return print(f'B64.encode : {str(e)}')

    @staticmethod
    def decode(s:str):
        """ decode string to base64 """
        try:
            return base64.b64decode(str(s))
        except Exception as e:
            return print(f'B64.decode : {str(e)}')


class UDID:
    """UDID encode and decode function. UDID.encode(string), UDID.decode(string)"""
    @staticmethod
    def encode(s:str):
        arr = []
        for i in range(len(s)):
            c = s[i]
            arr.append(UDID().createRandomNumberString(
                2) + UDID().chr(UDID().ord(c) + 10) + UDID().createRandomNumberString(1))
        return UDID()._04x(len(s)) + ''.join(arr) + UDID().createRandomNumberString(32)

    @staticmethod
    def decode(s:str):
        l = int(str(s[0:4]), 16)
        e = ''
        for i in range(6, len(s), 4):
            e += s[i]
        e = e[0:l]
        arr = []
        for i in range(len(e)):
            arr.append(UDID().chr(UDID().ord(e[i]) - 10))
        return ''.join(arr)

    def _04x(self, n: int):
        s = hex(n).lstrip('0x')
        s = s.zfill(4)
        return s

    def createRandomNumberString(self, l):
        s = []
        for i in range(l):
            s.append(str(randint(0, 9)))
        return ''.join(s)

    def ord(self, string):
        return ord(str(string))

    def chr(self, code):
        return chr(int(code))


class HTTPClient:
    """ HTTPClient class post data to server and return response. """

    def make_request(self, method, endpoint, headers=None, data=None):
        with requests.request(method, endpoint, headers=headers, data=data) as resp:
            if resp.status_code == 200:
                resp = resp.encoding('utf-8')
                return resp.text
