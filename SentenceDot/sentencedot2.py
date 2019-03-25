import module

udid = '707498d3ef554b8298bc866f6078c627' 
viewer_id = 'TwYyp0mKm9811nIyYYdQWk5UVXhOemsyTW1ZMk9ETXhNVFU1WkRJeVptRTJNekU1'

test = module.Base64(viewer_id)

print (test.decode)

key = module.Base64(viewer_id).key
print (key)
data = module.Base64(viewer_id).data
iv = str.encode(udid[0:16])

resp = module.AESCBC.decrypt(key, iv, data)

print(viewer_id)
print(resp)