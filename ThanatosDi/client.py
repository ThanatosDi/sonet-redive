import requests

headers = {
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
}

data = {
    'a':'a'
}

with requests.post('http://127.0.0.1:5000/', headers=headers, data=data) as resp:
    if resp.status_code==200:
        print(resp.text)