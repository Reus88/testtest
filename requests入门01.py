import requests
query = input("输入一个你喜欢的明星")    #让用户输入想要输入的程序

url=f'https://www.sogou.com/web?query={query}'

myheaders = {
    "User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}     #request headers中的user agent

resp = requests.get(url,headers=myheaders) #处理一个小小的反爬


print(resp)
print(resp.text) #拿到网页源代码