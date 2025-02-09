import requests

url = "https://movie.douban.com/j/chart/top_list"

# 重新封装函数
param = {
    "type": "24",
    "interval_id": "100:90",
    "action":"",
    "start": "0",
    "limit": "20"
}   #get 请求下的query string parameter

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

resp = requests.get(url=url,params=param,headers=headers)

# print(resp.request.headers)  查看请求的user agent
print(resp.json())
resp.close() #关掉resp