from urllib.request import urlopen

url = 'https://www.taobao.com/'
rep = urlopen(url)

# 获取网页编码，如果没有声明则默认使用 UTF-8
encoding = rep.headers.get_content_charset() or 'utf-8'

# 读取内容并解码
html_content = rep.read().decode(encoding)

# 保存到文件
with open('mtaobao.html', mode='w', encoding='utf-8') as f:
    f.write(html_content)
