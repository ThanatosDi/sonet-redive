import module

response = 'XBRPXgtHUwZ36qLoWj70deNEjQlYYmsuk47c9+190wdYrAi5xufpke2IKvldp4flREmt0FYb5pGfgjtjb5slOItq85v5OjzhgAmx2P34kw3tTPn3OzhvK5SXwkipj06SwdF+jANNaki/8KxYtFdkohDy6D1S8iQk3MAsSvEWtkl5yYvdl5wJwAPa3JrsXynx2slObS3u0jSoRJgVtfuCDFM/agpU6WTFbzZlAk2ZLjf44/BOdXy5B9PrZvPHXvXLybcSkW/LsaJhQT4/gjXqAU4/yh+nVr352wCZfxppOA2S9+1N07fhdxRAiP+zxrWgHXITecwIiiwOzROa5X7iymU2OTNlZjZlNTY0N2RhYzNmZTNmOGE5OTQzYjg1N2Jh'
de_UDID = '707498d3ef554b8298bc866f6078c627'

b64 = module.Base64(response)

key = b64.key
data = b64.data
iv = str.encode(de_UDID[0:16])

result = module.AESCBC.decrypt(key,iv,data)
result = module.MSP(result)

print(result.unpack)