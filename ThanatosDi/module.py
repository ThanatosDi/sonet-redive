import base64
from random import randint

from Crypto.Cipher import AES


class AESCBC:
    """aes class"""
    @staticmethod
    def decrypt(key, iv, data):
        try:
            cryptor = AES.new(key, AES.MODE_CBC, iv)
            new = cryptor.decrypt(data)
            return new
        except Exception as e:
            return f'decrypt error : {str(e)}'

    @staticmethod
    def encrypt(key, iv, data):
        try:
            cryptor = AES.new(key, AES.MODE_CBC, iv)
            new = cryptor.encrypt(data)
            return new
        except Exception as e:
            return f'encrypt error : {str(e)}'


class UDID:
    """udid class"""
    def encode(self, s):
        arr = []
        for i in range(len(s)):
            c = s[i]
            arr.append(self.createRandomNumberString(
                2) + self.chr(self.ord(c) + 10) + self.createRandomNumberString(1))
        return self._04x(len(s)) + ''.join(arr) + self.createRandomNumberString(32)

    def decode(self, s):
        l = int(str(s[0:4]), 16)
        e = ''
        for i in range(6, len(s), 4):
            e += s[i]
        e = e[0:l]
        arr = []
        for i in range(len(e)):
            arr.append(self.chr(self.ord(e[i]) - 10))
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