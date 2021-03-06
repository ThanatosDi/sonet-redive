# 操作
可用模組放置在 Moule 資料夾內

# 基本參數

* UDID
* short_udid
* sid
* view id
* iv

### UDID
UDID 與 short_udid 可以使用 `module.py` 中的 UDID.decode 方法進行反編碼  
UDID 出現點在於 **第一次** 開啟遊戲時，由客戶端發起請求至 `/tool/signup` 所攜帶的 header  

UDID 編碼後如下  
`
002481l244k386:736;461A823?735:518?6517275?235p634>634m1517575>367C851<225C4147488l684n533C252;7247423A434k452=537=737>131>322B681@635B282:333=473<622417656762671178217751733754235
`  

UDID 編碼前格式為 [0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}  
例如 `ba017505-5f4c-4929-bd91-7a3344868032`  

### short_udid
而 short_udid 為 [0-9]{6}\?[0-9A-Z]{11};[0-9]{3};[0-9]{3}<[0-9]{3}=[0-9]{3}@[0-9]{3}=[0-9A-Z]{33}  
例如 `000942?754B273A353;775;465<425=212@483=573836716152438876367556481657467`

反編碼的 short_udid 為一串 **9** 位數字 **※注 view id 與 viewer_id 非相同 請注意**

### sid
sid 只要抓包即可得到，sid在任何請求都不會變動


### view id
view id 一般來說是指玩家帳號的 ID ，就是加戰隊的 ID 也是在首頁(尚未開始遊戲時)右下角的 ID 

### iv 
iv 來源為 UDID 反編碼之後去掉 **-** 取得的字串取前 **16** 字元  
如 `ba0175055f4c4929`

# 回傳參數

* viewer_id


### viewer_id
viewer_id 為雜湊碼，內容為 view id 經過 AES CBC 加密後再用 base64 編碼而成  
如將 viewer_id base64 反編碼得到的結果為 `(經過AES加密資料) (key)`  
而加密的資料可以使用 key、iv 進行 AES CBC 解密，可以發現加密的資料為 view id  
爾後 key 怎麼來? key 還可以再用 base64 反編碼，得到的結果是雜湊碼，類似 `dbdf17f7e3a6fa7c6439135c`  
至於該來源目前未知

# 目前成果

當在遊戲內想要取得某人的資訊的時候，會同時送出請求給伺服器
本文使用 Fiddler 協助抓取封包

![image](https://github.com/ThanatosDi/sonet-redive/blob/master/Imgs/get_profile%20-%20game.png)
在遊戲中取得某人資訊

![image](https://github.com/ThanatosDi/sonet-redive/blob/master/Imgs/get_profile%20-%20fiddler.png)
將會同時請求至伺服器，取得該玩家資訊


![image](https://github.com/ThanatosDi/sonet-redive/blob/master/Imgs/get_profile%20-%20%E8%A7%A3%E5%AF%86.png)
~~過程就不解釋了，總之就是這樣那樣 自己看程式理解吧~~
使用程式解密(該程式路徑 相對於本github為 /sonet-redive/SentenceDot/sentencedot3.py)

![image](https://github.com/ThanatosDi/sonet-redive/blob/master/Imgs/get_profile%20-%20%E6%AF%94%E5%B0%8D.png)
最後附上把json整理好後的對比圖
