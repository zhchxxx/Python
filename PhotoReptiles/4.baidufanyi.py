import requests
import json
import encodings

url = 'https://fanyi.baidu.com/sug'
data = {'kw':'测试'}

# win下命令行参数为gbk编码：star.gbk2utf8(sys.argv[1]) + '也有'
# 百度返回需要进行转换操作，不然多数是/u开头unicode编码字符串
def gbk2utf8(s):
    return s.encode('utf-8').decode('unicode_escape')

response = requests.post(url, data = data)

print('登录结果：',response, '\n')
print('返回结果：',response.text, '\n')

encodingstr = gbk2utf8(response.text)

print('类型:',type(response.text) , '\n')

print(encodingstr)

print('类型:',type(encodingstr), '\n')

print('开始Jsson序列化')

json_dic = json.loads(encodingstr)
print('类型:',type(json_dic), '\n')
print(json_dic)