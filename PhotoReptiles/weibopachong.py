import time
import requests
import io
import json
import encodings
from PhotoReptiles.mysqlhelper import MysqlHelper

helper = MysqlHelper()

url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=2803301701&containerid=1076032803301701'
queryurl = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=2803301701&containerid='
urlreturn = ''

headers = {
'Accept': 'application/json, text/plain, */*',
#'Referer': 'https://m.weibo.cn/u/2803301701',
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36',
'X-Requested-With': 'XMLHttpRequest',
}

bcontinue = 1

# win下命令行参数为gbk编码：star.gbk2utf8(sys.argv[1]) + '也有'
# 百度返回需要进行转换操作，不然多数是/u开头unicode编码字符串
def gbk2utf8(s):
    return s.encode('utf-8').decode('unicode_escape')

def deal_json_invaild(str):
    str = str.replace("\n", "").replace("\r", "").replace("\n\r", "").replace("\r\n", "").replace("\t", "").replace(
        "\\\"", "\"").replace("				", "")

    str = str.replace('":"{"', "**testPasswors**5") \
        .replace('":"', '&&testPassword&&') \
        .replace('","', "$$testPassword$$") \
        .replace('":{"', "**testPasswors**1") \
        .replace('"},"', "**testPasswors**2") \
        .replace(',"', "**testPasswors**3") \
        .replace('{"', "@@testPassword@@") \
        .replace('"}', "**testPassword**") \
        .replace('":', "**testPasswors**4")
    str = str.replace('"', '”') \
                .replace("**testPasswors**5", "\":{\"").replace('&&testPassword&&', '":"').replace('$$testPassword$$',
                                                                                                   '","').replace(
                '**testPasswors**1', '":{"').replace('**testPasswors**2', '"},"').replace('@@testPassword@@',
                                                                                          '{"').replace(
                '**testPassword**', '"}').replace('**testPasswors**3', ',"').replace('**testPasswors**4', '":').replace(
                '\\"', '\"').replace(' ', '').replace("resourceExtraInfo ", "resourceExtraInfo").replace("\n",
                                                                                                         "").replace(
                "\r", "").replace("\n\r", "").replace("\r\n", "").replace("\t", "").replace(r"\"", "\"").replace(
                "				", "").replace("}\"", "}")
    return str

def autoloading(url):
    req = requests.get(url, headers=headers)

    print('返回状态', req)
    print('返回内容', req.text)

    encodingstr = gbk2utf8(req.text)
    print('转码后内容', encodingstr)

    encodingstr = encodingstr.replace('\/', '/')

    encodingstr = deal_json_invaild(encodingstr)

    print('格式化后内容', encodingstr)

    # 入库操作
    insert_sql = 'INSERT INTO weibo_test (weibo_text) VALUES (%s); '
    data = (encodingstr,)
    helper.execute_modify_sql(insert_sql,data)
    # 序列化为字典操作
    json_dic = json.loads(encodingstr)
    querystr = json_dic['data']['cardlistInfo']

    bcontinue = 0
    if 'containerid' in querystr:
        urlreturn = queryurl + '%s' % json_dic['data']['cardlistInfo']['containerid']
        print(urlreturn)
        bcontinue=1
        #&since_id=4545011050353448
        if 'since_id' in querystr:
            urlreturn = urlreturn+'&since_id=%s'%json_dic['data']['cardlistInfo']['since_id']
            print('带有since_id的Url：',urlreturn)
    url = urlreturn
    time.sleep(1)
    #return  urlreturn


while bcontinue== 1:
    autoloading(url)
