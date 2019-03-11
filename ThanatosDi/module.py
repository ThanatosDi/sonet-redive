import base64
import hashlib
from random import randint, randrange

import msgpack
import requests  # requests
from Crypto.Cipher import AES  # pycryptodome.
from Crypto.Util import Padding

requests.urllib3.disable_warnings()


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
            new = Padding.unpad(cryptor.decrypt(data), 16)
            return new
        except Exception as e:
            return print(f'AESCBC.decrypt : {str(e)}')

    @staticmethod
    def encrypt(key, iv, data):
        try:
            cryptor = AES.new(key, AES.MODE_CBC, iv)
            new = cryptor.encrypt(Padding.pad(data, 16))
            return new
        except Exception as e:
            return print(f'AESCBC.encrypt : {str(e)}')

    @staticmethod
    def b(s: str):
        try:
            return str.encode(s)
        except Exception as e:
            return print(f'string.b : {str(e)}')


class Base64:
    """ base64 encode and decode function. """

    def __init__(self, s):
        self.content = None
        self.s = s

    @property
    def encode(self):
        """ encode string to base64 """
        try:
            return base64.b64encode(bytes(self.s))
        except Exception as e:
            return print(f'B64.encode : {str(e)}')

    @property
    def decode(self):
        """ decode string to base64 """
        try:
            self.content = base64.b64decode(str(self.s))
            return self.content
        except Exception as e:
            return print(f'B64.decode : {str(e)}')

    @property
    def key(self):
        if not self.content:
            self.content = Base64(str(self.s)).decode
        key = self.content[-32:]
        return key

    @property
    def data(self):
        if not self.content:
            self.content = Base64(str(self.s)).decode
        data = self.content[0:-32]
        return data


class UDID:
    """UDID encode and decode function. UDID.encode(string), UDID.decode(string)"""
    @staticmethod
    def encode(s: str):
        arr = []
        for i in range(len(s)):
            c = s[i]
            arr.append(UDID().createRandomNumberString(
                2) + UDID().chr(UDID().ord(c) + 10) + UDID().createRandomNumberString(1))
        return UDID()._04x(len(s)) + ''.join(arr) + UDID().createRandomNumberString(32)

    @staticmethod
    def decode(s: str):
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


class MSP:
    def __init__(self, data):
        self.data = data

    @property
    def pack(self):
        return msgpack.packb(self.data)

    @property
    def unpack(self):
        return msgpack.unpackb(bytes(self.data),raw=False)


class HTTPClient:
    """ HTTPClient class post data to server and return response. """

    def make_request(self, method, endpoint, headers=None, data=None, timeout=5, verify=False):
        """HTTPClient.make_request(self, method, endpoint, headers=None, data=None, timeout=5)"""
        try:
            with requests.request(method, endpoint, headers=headers, data=data, timeout=timeout, verify=verify) as resp:
                if resp.status_code == 200:
                    return resp.text
                return print(f'resp.status_code : {str(resp.status_code)}')
        except Exception as e:
            return print(f'HTTPClient.make_request : {str(e)}')


    def call(self, path, args):
        vid_iv = "%016d" % randrange(10**16)
        args["timezone"] = "09:00:00"
        args["viewer_id"] = vid_iv + base64.b64encode(
            encrypt_cbc(str(self.viewer_id), vid_iv,
                        VIEWER_ID_KEY))
        plain = base64.b64encode(msgpack.packb(args))
        # I don't even
        key = base64.b64encode("".join("%x" % randrange(65536) for i in range(32)))[:32]
        msg_iv = self.udid.replace("-","").decode("hex")
        body = base64.b64encode(encrypt_cbc(plain, msg_iv, key) + key)
        sid = self.sid if self.sid else str(self.viewer_id) + self.udid
        headers = {
            "PARAM": hashlib.sha1(self.udid + str(self.viewer_id) + path + plain).hexdigest(),
            "KEYCHAIN": "",
            "USER-ID": self.lolfuscate(str(self.user)),
            "CARRIER": "google",
            "UDID": UDID.encode(self.udid),
            "APP-VER": "1.3.0",
            "RES-VER": str(self.res_ver),
            "IDFA": "",
            "PROCESSOR-TYPE": "ARMv7 VFPv3 NEON",
            "IP-ADDRESS": "127.0.0.1",
            "DEVICE-NAME": "Nexus 42",
            "X-Unity-Version": "2017.4.2f2",
            "SID": hashlib.md5(sid + SID_KEY).hexdigest(),
            "GRAPHICS-DEVICE-NAME": "3dfx Voodoo2 (TM)",
            "DEVICE-ID": hashlib.md5("Totally a real Android").hexdigest(),
            "PLATFORM-OS-VERSION": "Android OS 13.3.7 / API-42 (XYZZ1Y/74726f6c6c)",
            "DEVICE": "2",
            "Content-Type": "application/x-www-form-urlencoded", # lies
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 13.3.7; Nexus 42 Build/XYZZ1Y)",
        }
