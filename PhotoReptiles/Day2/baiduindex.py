import requests
import re
import json
from w3lib.html import  remove_tags

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

# title
# source
# time
# content

# 爬虫第三步
# url = 'https://baijiahao.baidu.com/s?id=1677461156592953023&wfr=spider&for=pc'
def get_detailed_page(url):
    response = requests.get(url)

    with open('baidu.html','wb') as f:
        f.write(response.content)

    line = response.text
    title_pattern ='<div class="article-title"><h2>(.*?)</h2></div>'

    res_title = re.search(title_pattern,line)
    print(res_title.group(1))

    source_pattern = '<div class="author-txt"><p class="author-name">(.*?)</p><div class="article-source article-source-bjh"'
    res_source = re.search(source_pattern,line)
    print(res_source.group(1))

    time_pattern = '<div class="article-source article-source-bjh"><span class="date">发布时间：(.*)</span><span class="time">(.*)</span><span class="account-authentication">'
    res_time = re.search(time_pattern,line)
    time = res_time.group(1) + ' ' + res_time.group(2)
    print(time)

    # content 内容
    content_pattern = '<div class="article " id="article" data-islow-browser="0"><div class="article-content">(.*)<button class="report-container"'
    res_content = re.search(content_pattern,line)
    print(res_content.group(1))
    print(remove_tags(res_content.group(1)))

def get_all_url():
    url = 'https://www.baidu.com/home/pcweb/data/mancardwater?id=2&offset=1&sessionId=15999120461762&crids=&pos=3&newsNum=3&blacklist_timestamp=0&indextype=manht&_req_seqid=0x90a566ea001158a9&asyn=1&t=1599912101640&sid=7506_32606_1429_7567_31660_7552_7604_22157'
    headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Referer': 'https://www.baidu.com/',
        'Cookie':'BIDUPSID=0F5A2CE56127C8FB0A3C9C08B3857D4E; PSTM=1592377047; BAIDUID=0F5A2CE56127C8FBEF8DE67B6205F86C:FG=1; BD_UPN=12314753; BDUSS=pIZDF-ODhydTd1bXNMMllrd2N1Y0xJS3lSVms2WWREeS1kZnRDdENpV0dCQk5mRVFBQUFBJCQAAAAAAAAAAAEAAAB5WLsMemhjaHh4eAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIZ3616Gd-teVk; MCITY=-%3A; BDUSS_BFESS=pIZDF-ODhydTd1bXNMMllrd2N1Y0xJS3lSVms2WWREeS1kZnRDdENpV0dCQk5mRVFBQUFBJCQAAAAAAAAAAAEAAAB5WLsMemhjaHh4eAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIZ3616Gd-teVk; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BD_HOME=1; BDRCVFR[S4-dAuiWMmn]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; COOKIE_SESSION=15392_1_8_6_6_1_1_0_8_1_0_0_0_0_9_0_1599894465_1599556346_1599909848%7C9%2393895_62_1599556342%7C9; H_PS_645EC=b43bOSSmqvKHWBfrfcorgumB9MmBl6bL3FrIUqEmfD46cPEDtiqf6Cr5NQ%2B%2F6OT1Va8l; H_PS_PSSID=7506_32606_1429_7567_31660_7552_7604_22157; sugstore=1'
    }
    response = requests.get(url,headers=headers)
    response.encoding = 'utf-8'
    print(response.text)

    print('_'*50)
    print('字典序列化')

    # tempstring = gbk2utf8(response.text)
    temp1 = response.text
    temp2 = deal_json_invaild(temp1)
    temp3 = temp2.replace('”','"')
    print(temp3)
    temp4 = re.sub(r"\\x22",r'\"',temp3)
    print(temp4)
    # tempstring = tempstring.replace('“','"')
    # tempstring = tempstring.replace('”','"')
    #
    # print(tempstring)

    temp5 = temp4.replace('”', '__')

    print(temp5)
    res_dic = json.loads(temp5)
    print('_'*50)
    print(res_dic)
    html_str= res_dic['html']
    print(html_str)

    pattern = 'href="(.*?)"["data-rid|"title|"target|]'
    hrefs = re.findall(pattern,html_str)

    print('输出路径')
    for href in hrefs:
        print(href)
        if(50 < len(href)):
            get_detailed_page(href)

if __name__ == '__main__':
    get_all_url()