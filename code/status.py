import requests

url = "https://www.kookapp.cn/api/v3/game/create"

Gname = 1
GImgUrl = 2

token = "" #WebsocketToken
header={f'Authorization': f"Bot {token}"}
params ={
    "name":Gname,
    "icon":GImgUrl
}

ret = requests.post(url,headers=header,data=params)
print(ret)
print(ret.text) # 返回值中有游戏的id