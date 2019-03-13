from module import *


API = 'https://api-pc.so-net.tw'
headers = {
    'PARAM': '21d7337286f43a47527a9b4a674fb65ace784736',
    'KEYCHAIN': '',
    'APP_VER': '1.3.2',
    'RES_VER': '00005001',
    'PLATFORM': '2',
    'LOCALE': 'Jpn',
    'IP_ADDRESS': '172.17.100.15',
    'DEVICE_NAME': 'samsung SM-G955N',
    'X-Unity-Version': '2017.1.2p2',
    'Content-Type': 'application/x-www-form-urlencoded',
    'SID': '0a23416d1066739c598edf69fbe6b779',
    'GRAPHICS_DEVICE_NAME': 'Adreno (TM) 540',
    'DEVICE_ID': '16a470d0c845244e43e4b54c287a2480',
    'REGION_CODE': '',
    'PLATFORM_OS_VERSION': 'Android OS 5.1.1 / API-22 (LYZ28N/500190306)',
    'BATTLE_LOGIC_VERSION': '2',
    'BUNDLE_VER': '',
    'SHORT_UDID': '000985=645A381@343C312@712:263;213?843B613171572673343562876138112877182',
    'DEVICE': '2',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G955N Build/LYZ28N)',
    'Host': 'api-pc.so-net.tw'
}

client = HTTPClient()


if __name__ == "__main__":
    udid = 'ba0175055f4c4929bd917a3344868032'  
    # ba017505-5f4c-4929-bd91-7a3344868032
    # 587112363
    #response = client.make_request('POST',f'{API}/check/game_start',headers=headers, verify=True)


    d = 'k90eiNA51kC5BHv8wLGCQlpHSmtaakUzWmpkbE0yRTJabUUzWXpZME16a3hNelZq'
    key = Base64(d).key
    data = Base64(d).data
    iv = AESCBC.b(udid[0:16])

    resp = AESCBC.decrypt(key, iv, data)
    print(d)
    print(resp)

    print('\r\nkey 解密')
    print(key)
    k1 = Base64(key.decode('utf-8')).decode
    print(k1)
    #a = msgpack.unpackb(resp,raw=False)
    #print(a)
    #print(UDID.decode('000924=415A888@111C551@611:856;317?717B481371227114626772317458331621333'))
    #print(UDID.encode('123456789'))
    #print(ID.viewerid('698094765'))
    print(UDID.decode('000975?211B377A842;225;823<524=858@845=528546483723272361472563262742236'))