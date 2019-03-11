from module import *


API = 'https://api-pc.so-net.tw'
headers = {
    'PARAM': '21d7337286f43a47527a9b4a674fb65ace784736',
    'KEYCHAIN': '',
    'APP_VER': '1.3.0',
    'RES_VER': '00005000',
    'PLATFORM': '2',
    'LOCALE': 'Jpn',
    'IP_ADDRESS': '172.17.100.15',
    'DEVICE_NAME': 'samsung SM-G955N',
    'X-Unity-Version': '2017.1.2p2',
    'Content-Type': 'application/x-www-form-urlencoded',
    'SID': 'c2240ae8e024efced1bc6d297066c72a',
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
    udid = '88d177ecf20241e39ef2a9c9dd6bc17c'
    #response = client.make_request('POST',f'{API}/check/game_start',headers=headers, verify=True)
    d = 'kdbR/56gs7SGLylrOmzv3sGRJx63NyjMXJEa4SNBcJjFzuoZLbT6xtSzLFp2B0plontLuVkjPE4/9nB/gcgqaeDyg8tq7ubMwgpzoIu8fIfq8C9jEwrsG0cdTFwfhLuimHV/Q00hoyx6U17WQlv5CBaDgnFApLKjd9KW4stg2KUR04POLlJLdMHfuRTVAhcvO9yE31PyrxcaCLHDzOw+Rt4XN2YM9JdaBE/vyq5PBN/bBkUjS6cKKOO7PP3E1rbEXKICiGD4xEXf2r4Lj9pIa1QyttmqMGNnorJhRNgaqPRsnMINlzi8Q86egMRb9v+3yjtI8PsMtapmb2lXQP+EA7TWYQtasBw5tNOAjEJnnigBlMnFxn57uMib9TZqyaf1llJgSORcDVY0VmFf0w5xcTOIFPi0zVyaiUM20t+xYXKL+4Ol/v4aELd0pkheWpesk7uUsORZHug5BzZ+IDtfhD0qalr+dGWFq1Jj/G5jrLg345hIiEhs743cz6/KlDu4E5hEPLIbBFDVhlXoHsuCD+T+0w/baqgo856JivmDgn5lZjhkZjIwNWZhZjJhNzdmOGFkYmNhNzRhZDQ4NmVmNA=='
    """ d
    \x87
    \xa8app_type\x00
    \xadcampaign_data\xa0
    \xadcampaign_sign\xa0
    \xadcampaign_user\xd2\x00\x02\x8b\x9e
    \xabendpointArn\xa0
    \xabcountrycode\xa2CN
    \xa9viewer_id
    \xda\x00@DJqDuanIhlBAqklYwh5jOk5EWmpNVE13T0RJNE1HWTFaRE13WVRKak5UWTNaR015

    \x87\xa8app_type\x00\xadcampaign_data\xa0\xadcampaign_sign\xa0\xadcampaign_user\xd2\x00\x02\x8b\x9e\xabendpointArn\xa0\xabcountrycode\xa2CN\xa9viewer_id\xda\x00@DJqDuanIhlBAqklYwh5jOk5EWmpNVE13T0RJNE1HWTFaRE13WVRKak5UWTNaR015

    \x87\xa8app_type\x00\xadcampaign_data\xa0\xadcampaign_sign\xa0\xadcampaign_user\xce\x00\x02\x8b\x9e\xabendpointArn\xa0\xabcountrycode\xa2CN\xa9viewer_id\xda\x00@DJqDuanIhlBAqklYwh5jOk5EWmpNVE13T0RJNE1HWTFaRE13WVRKak5UWTNaR015
     """
    key = Base64(d).key
    data = Base64(d).data
    iv = AESCBC.b(udid[0:16])

    resp = AESCBC.decrypt(key, iv, data)
    #print(resp)

    print(MSP(3).pack)
    print(str(MSP(b'\xa13').unpack))
    a = msgpack.unpackb(resp,raw=False)
    print(a)
    