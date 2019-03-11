import base64
from module import *
import msgpack
import requests

requests.urllib3.disable_warnings()
""" headers = {
    'PARAM': 'af8fb18cdd9445b77b9c962cd0f58a8414b8e032',
    'KEYCHAIN': '',
    'APP_VER': '1.3.0',
    'RES_VER': '00005000',
    'PLATFORM': '2',
    'LOCALE': 'Jpn',
    'IP_ADDRESS': '172.17.100.15',
    'DEVICE_NAME': 'samsung SM-G955N',
    'X-Unity-Version': '2017.1.2p2',
    'Content-Type': 'application/x-www-form-urlencoded',
    'SID': '6be9eb222ff69c7084fa446e716d4e78',
    'GRAPHICS_DEVICE_NAME': 'Adreno (TM) 540',
    'DEVICE_ID': '63a6d1e81ee9ffaf24bb999049787466',
    'REGION_CODE': '',
    'PLATFORM_OS_VERSION': 'Android OS 5.1.1 / API-22 (LYZ28N/500190227)',
    'BATTLE_LOGIC_VERSION': '2',
    'BUNDLE_VER': '',
    'SHORT_UDID': '000975=424A626@442C878@355:782;234?882B745275482235273773627488164272258',
    'DEVICE': '2',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G955N Build/LYZ28N)',
    'Host': 'api-pc.so-net.tw',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip'
} """
headers = {
    'Host': 'api-pc.so-net.tw',
    'User-Agent': 'princessconnect/17 CFNetwork/758.3.15 Darwin/15.4.0',
    'PARAM': '42cb38693c53d80e450c47e5e2213352eb8cdb35',
    'REGION_CODE': '',
    'BATTLE_LOGIC_VERSION': '1',
    'PLATFORM_OS_VERSION': 'iPhone OS 9.3.1',
    'DEVICE_ID': 'DAAF343A-ED51-4923-A24A-AD128AA69092',
    'KEYCHAIN': '692807689',
    'GRAPHICS_DEVICE_NAME': 'Apple A7 GPU',
    'SHORT_UDID': '000974;156A655>551<835?218@261C861C817A776112486341741361616451827355827',
    'DEVICE_NAME': 'iPhone6,2',
    'BUNDLE_VER': '',
    'LOCALE': 'Jpn',
    'IP_ADDRESS': '192.168.0.109',
    'SID': 'fbfc84002187655acdce2a88638fd3f4',
    'X-Unity-Version': '2017.1.2p2',
    'PLATFORM': '1',
    'Connection': 'keep-alive',
    'Accept-Language': 'zh-cn',
    'APP_VER': '1.3.0',
    'RES_VER': '-1',
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip, deflate',
    'DEVICE': '1'
}
#response = base64.b64decode('E47TtA+1REw1ULHtpALWCxQlSegkFRRBh4+YZ2hAN36nnc93oUUNXXvzL1Szs86/52xmFM2fGuIFiKxjDXaQqP8BSBmQrHPk8BRr5XwhH666Y0PH4XuNJ9jmMwwtHDUQMYGlspljKt/l63KnCb6ObBBRzYdktsiGzvvSBUkvFI/bNxPssxGjfUNFyyFI94CdHgIuMYnjF/k14rynGZt9u3wRzOBn9tlVheq9RdUZmMhOR0l5WkRJMk1tRmhOell5WXpnNVlXTmhOMlEyWkRneA==')
data = base64.b64decode('E47TtA+1REw1ULHtpALWCxQlSegkFRRBh4+YZ2hAN36nnc93oUUNXXvzL1Szs86/52xmFM2fGuIFiKxjDXaQqP8BSBmQrHPk8BRr5XwhH666Y0PH4XuNJ9jmMwwtHDUQMYGlspljKt/l63KnCb6ObBBRzYdktsiGzvvSBUkvFI/bNxPssxGjfUNFyyFI94CdHgIuMYnjF/k14rynGZt9u3wRzOBn9tlVheq9RdUZmMhOR0l5WkRJMk1tRmhOell5WXpnNVlXTmhOMlEyWkRneA==')

with requests.post('https://api-pc.so-net.tw/check/game_start',headers=headers, data=data, verify=False, timeout=5) as resp:
    if resp.status_code==200:
        print(resp.text)

response = base64.b64decode(resp.text)
udid = '2eae8edf16a744f5a593a026ec46e895'
iv = str.encode(udid[0:16])
key = response[-32:]
data = response[0:-32]

new = AESCBC.decrypt(key, iv, data)

print(new)


""" new = b'\x87\xa8app_type\x00\xadcampaign_data\xa0\xadcampaign_sign\xa0\xadcampaign_user\xd2\x00\x02\x8b\x9e\xabendpointArn\xa0\xabcountrycode\xa2CN\xa9viewer_id\xda\x00@DJqDuanIhlBAqklYwh5jOk5EWmpNVE13T0RJNE1HWTFaRE13WVRKak5UWTNaR015\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b'
print(new)

try:
    new.decode(encoding='utf-8')
except UnicodeDecodeError as e:
    pass

#print(msgpack.packb({'app_type':{'campaign_data':{'campaign_sign':{'campaign_user':'123'}}}}))
print(msgpack.unpackb(b'\xa8')) """