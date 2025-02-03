from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen (url)

#print (resp.read().decode("utf-8")) 如果添加这行代码会使段代码，会报错，因为resp.read()是字节流，decode()是解码，所以resp.read().decode("utf-8")是字节流，解码成字符串，所以会报错
content =resp.read().decode("utf-8")

with open("pybaidu.html",mode="w",encoding="utf-8") as f:
    f.write(content)
print("over")