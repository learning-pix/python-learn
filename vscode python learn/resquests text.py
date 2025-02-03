import requests

r = requests.get('http://www.baidu.com')

print(r.status_code)

print(r.encoding)# 返回的编码格式
print(r.apparent_encoding)# 猜测的编码格式
print(r.text)

r.encoding = 'utf-8'
print(r.text)