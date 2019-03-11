# IMPORT
```python
form module import *
```

# USE

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

| Python code | return type |
| ------ | ------ |
| UDID.decode(data) | str |
| UDID.encode(data) | str |

## HTTPClient

```python
clinet = HTTPClient()
client.make_request(method, endpoint, headers=None, data=None, timeout=5, verify=False)
```
