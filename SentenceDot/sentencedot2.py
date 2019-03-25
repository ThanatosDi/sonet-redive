import module

udid = '8d57018464c5424ab42299fe8c514d2b'
viewer_id = '73nswLK1jDNqE/H0F0UgX1ptRTBaV1poTVRNNVlqTXlZakkyTXpGbE5EWTVOalpo'

test = module.Base64(viewer_id)

print(test.decode)

key = module.Base64(viewer_id).key
print(key)
data = module.Base64(viewer_id).data
iv = str.encode(udid[0:16])

resp = module.AESCBC.decrypt(key, iv, data)

print(viewer_id)
print(resp)
