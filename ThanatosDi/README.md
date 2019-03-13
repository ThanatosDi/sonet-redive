* [Import](#Import)
* [Use](#Use)
    * [AESCBC](#AESCBC)
    * [Base64](#Base64)
    * [UDID](#UDID)
    * [HTTPClient](#HTTPClient)
* [Endpoint list](#Endpoint-list)
* [Reference](#Reference)

# Import
```python
form module import *
```

# Use

## AESCBC
use AES_CBC decrypt or encrypt data.  
**key**, **iv**, **data** type is bytes.  

| Python code | return type |
| ------ | ------ |
| AESCBC.decrypt(key, iv, data) | bytes |
| AESCBC.encrypt(key, iv, data) | bytes |

## Base64
use base64 decode or encode data.  

| Python code | return type |
| ------ | ------ |
| Base64(data).decode | bytes |
| Base64(data).encode | bytes |
| Base64(data).key | bytes |
| Base64(data).data | bytes |

## UDID
In packet header name is **`SHORT_UDID`**  
value like this : **`000940;246<267=254>853?023@371A105B497C982757386309871755712519102590610`**  
value decode is **`123456789`**

| Python code | return type |
| ------ | ------ |
| UDID.decode(data) | str |
| UDID.encode(data) | str |

## HTTPClient

```python
clinet = HTTPClient()
client.make_request(method, endpoint, headers=None, data=None, timeout=5, verify=False)
```

# Reference
[(GitHub) marcan/deresuteme](https://github.com/marcan/deresuteme)  
[deresuteme デレステ解析ノート](https://subdiox.github.io/deresute/)  
[(GitHub) esterTion/unity-texture-toolkit](https://github.com/esterTion/unity-texture-toolkit)  
[CGSS桌面应用mishiro背后的故事](https://toyobayashi.github.io/2018/04/01/CGSS%E6%A1%8C%E9%9D%A2%E5%BA%94%E7%94%A8mishiro%E8%83%8C%E5%90%8E%E7%9A%84%E6%95%85%E4%BA%8B/#more)  

