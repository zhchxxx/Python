import requests
import os
import sys

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

}

url ='https://www.baidu.com/'
response = requests.get(url,headers = headers)
response.encoding = 'utf-8'

print(response)
print(response.text)

print(os.getcwd())

path = os.getcwd() + '\\Offline\\'
print(path)
# 判断目录是否存在
if not os.path.exists(os.path.split(path)[0]):
    # 目录不存在创建，makedirs可以创建多级目录
    os.makedirs(os.path.split(path)[0])

with open(path +'baidu.html','wb') as f:
    f.write(response.content)
