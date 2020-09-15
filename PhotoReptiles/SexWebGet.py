import os
import re
import time
import uuid

import requests

import PhotoReptiles.mysqlhelper as mysqlhelper

helper = mysqlhelper.MysqlHelper()


# get a UUID - URL safe, Base64
def get_a_uuid():
    # r_uuid = base64.urlsafe_b64encode(uuid.uuid4().bytes)
    # return r_uuid.replace('=', '')
    return uuid.uuid4().hex


# 内容解码成utf-8
def gbk2utf8(s):
    return s.encode('utf-8').decode('unicode_escape')


# 内容解码成utf-8
def decode2uft8(s):
    return s.encode("raw_unicode_escape").decode("utf-8")


# 判断是否有重复的title实体存在
def hassametitle(title, url):
    querysql = 'SELECT COUNT(id) FROM title WHERE title = %s and url = %s'
    data = (title, url,)
    result = helper.is_has_same_data(querysql, data)
    return result


# 入库操作
def inserttitle(id, infodate, title, url):
    if hassametitle(title, url) == 0:
        insert_sql = 'INSERT INTO title (id,infodate,title,url) VALUES (%s,%s,%s,%s); '
        data = (id, infodate, title, url,)
        helper.execute_modify_sql(insert_sql, data)


# 判断是否有重复的title_info实体存在
def hassametitleinfo(title, url):
    querysql = 'SELECT COUNT(id) FROM title_info WHERE titlename = %s and tdurl = %s'
    data = (title, url,)
    result = helper.is_has_same_data(querysql, data)
    return result


# 入库操作
def inserttitleinfo(id, titledate, titleid, titlename, titlesize, titlelenth, tdurl):
    if hassametitleinfo(titlename, tdurl) == 0:
        insert_sql = 'INSERT INTO title_info (id,titledate,titleid,titlename,titlesize,titlelenth,tdurl) VALUES (%s,%s,%s,%s,%s,%s,%s); '
        data = (id, titledate, titleid, titlename, titlesize, titlelenth, tdurl,)
        helper.execute_modify_sql(insert_sql, data)


# 判断是否有重复的torrent实体存在
def hassametorrent(tname, path):
    querysql = 'SELECT COUNT(id) FROM torrent WHERE tname = %s and path = %s'
    data = (tname, path,)
    result = helper.is_has_same_data(querysql, data)
    return result


# 入库操作
def inserttorrent(tiid, url, tname, path):
    if hassametorrent(tname, path) == 0:
        insert_sql = 'INSERT INTO torrent (tiid,url,tname,path) VALUES (%s,%s,%s,%s); '
        data = (tiid, url, tname, path,)
        helper.execute_modify_sql(insert_sql, data)


# 判断是否有重复的图片存在
def hassamephoto(url, path):
    querysql = 'SELECT COUNT(id) FROM photo WHERE url = %s and path = %s'
    data = (url, path,)
    result = helper.is_has_same_data(querysql, data)
    return result


# 入库操作
def insertphoto(infoid, titledate, url, path):
    if hassamephoto(url, path) == 0:
        insert_sql = 'INSERT INTO photo (infoid,titledate,url,path) VALUES (%s,%s,%s,%s); '
        data = (infoid, titledate, url, path,)
        helper.execute_modify_sql(insert_sql, data)


# 下载图片
def download_img(img_url, phtoname, guid, tdate):
    try:
        datestring = time.strftime("%Y%m%d", time.localtime())
        savepath = defaultpath + datestring + '\\'
        if not os.path.exists(savepath):
            os.makedirs(savepath)
        filename = savepath + phtoname
        if not os.path.exists(filename):
            try:
                r = requests.get(img_url, stream=True)
                if r.status_code == 200:
                    try:
                        open(filename, 'wb').write(r.content)  # 将内容写入图片
                    except:
                        print('图片写入失败：' + img_url)
                else:
                    print('图片下载失败：' + img_url)
                del r
            except:
                print('请求超时：' + img_url)
            # print(r.status_code) # 返回状态码
            # print("done")
            # insert_sql = 'INSERT INTO photo (infoid,titledate,url,path) VALUES (%s,%s,%s,%s); '
            # data = (guid, tdate, img_url, filename,)
            # helper.execute_modify_sql(insert_sql, data)
            insertphoto(guid, tdate, img_url, filename)

    except:
        print('图片下载失败！' + 'download_img')


# 下载种子，当前为获取磁力链接
def download_torrent(turl, titlename, titleid):
    try:
        # 把下载地址发送给requests模块
        r = requests.get(turl)
        # defaultpath = 'H:\\PythonDownload\\Torrent\\'
        # datestring = time.strftime("%Y%m%d", time.localtime())
        # savepath = defaultpath + datestring + '\\'
        # if not os.path.exists(savepath):
        #     os.makedirs(savepath)
        # filename = savepath + titlename + '.torrent'

        # print(turl)
        # print(filename)

        # print(r.text)

        # pattern = 'href="/Download/(.*?)">下載檔案</a>'
        # res_torrent = re.search(pattern, r.text)
        # # print(res_torrent.group(1))
        #
        # downloadurl = 'https://www1.hgcdown.net/Download/' + res_torrent.group(1)
        # print(downloadurl)
        #
        # downloadheaders['path'] =  '/Download/' + res_torrent.group(1)
        # downloadheaders['referer'] = turl
        #
        # print(downloadheaders)
        # requests_torrent = requests.get(downloadurl, headers=downloadheaders)

        if r.status_code == 200:
            pattern = 'href="magnet:(.*?)">磁力連結</a>'
            res_torrent = re.search(pattern, r.text)
            # print(res_torrent.group(1))

            magnet_url = 'magnet:' + res_torrent.group(1)

            # insert_sql = 'INSERT INTO torrent (tiid,url,tname,path) VALUES (%s,%s,%s,%s); '
            # data = (titleid, turl, titlename,magnet_url,)
            # helper.execute_modify_sql(insert_sql, data)
            inserttorrent(titleid, turl, titlename, magnet_url)

        else:
            print('获取磁力链接失败')
        del r
    except:
        print('解析磁力链接失败！' + 'download_torrent')


# 获取当前网页包含链接及信息并入库，并请求其他方法进行解析
def get_page_has_link_save(str):
    try:
        # <a href="html_data/5/2009/4956100.html" id="a_ajax_4956100">[09.12] [MP4]【极品风骚】银行办业务勾引到的，吃了两次饭就跟我开房了</a>
        pattern_href_title = '<h3> 	<a href="(.*?)" id="(.*?)">\[(.*?)\] (.*?)</a>'
        res_match_href = re.search(pattern_href_title, str)
        # print('地址:')
        # print(res_match_href.group(1))
        # # print(res_match_href.group(2))
        # print('日期:')
        # print(res_match_href.group(3))
        # print('标题:')
        # print(res_match_href.group(4))

        tdate = res_match_href.group(3)
        guid = get_a_uuid()
        # print(guid)
        urlopen = 'https://k6.7086xx.xyz/pw/' + res_match_href.group(1)
        # insert_sql = 'INSERT INTO title (id,infodate,title,url) VALUES (%s,%s,%s,%s); '
        # data = (guid, tdate, res_match_href.group(4), urlopen,)
        # helper.execute_modify_sql(insert_sql, data)
        inserttitle(guid, tdate, res_match_href.group(4), urlopen)

        get_page_info_save(urlopen, guid, tdate)
    except:
        print('获取网页内链接失败！' + 'get_page_has_link_save')


def has_format(responsestring, tguid, tdate):
    try:
        # pattern = '<div class="f14" id="read_tpc">【影片名称】：(.*?)<br>【影片大小】：(.*?)<br>【影片时长】：(.*?)<br>'
        pattern = '<div class="f14" id="read_tpc"><br>【影片名稱】：(.*?)<br>【影片格式】：(.*?)<br>【字幕語言】：(.*?)<br>【是否有碼】：(.*?)<br>【影片大小】：(.*?)<br>'
        res_match = re.search(pattern, responsestring)
        print('影片名称：' + res_match.group(1))
        print('影片大小：' + res_match.group(5))
        print('影片时长：' + res_match.group(2))

        pattern_url = '<div class="f14" id="read_tpc">(.*?)</div>'
        res_match_url = re.search(pattern_url, responsestring)

        # print(res_match_url.group(1))

        pattern_turl = '"_blank" >http(.*?)</a>'
        res_match_turl = re.search(pattern_turl, res_match_url.group(1))
        # print(res_match_turl.group(1))

        guid = get_a_uuid()
        turl = 'http' + res_match_turl.group(1)
        file_name = os.path.basename(turl)
        download_torrent(turl, file_name, guid)

        # insert_sql = 'INSERT INTO title_info (id,titledate,titleid,titlename,titlesize,titlelenth,tdurl) VALUES (%s,%s,%s,%s,%s,%s,%s); '
        # data = (guid, tdate, tguid, res_match.group(1), res_match.group(5), res_match.group(2), turl,)
        # helper.execute_modify_sql(insert_sql, data)
        inserttitleinfo(guid, tdate, tguid, res_match.group(1), res_match.group(5), res_match.group(2), turl)

        pattern_photo = '<img src="(.*?)"'
        res_match_photo = re.findall(pattern_photo, responsestring)
        for purl in res_match_photo:
            if 'http' in purl:
                # print(purl)
                img_name = os.path.basename(purl)
                download_img(purl, img_name, guid, tdate)
    except:
        print('解析模块失败！' + 'has_format')


def has_other_format(responsestring, tguid, tdate):
    try:
        # pattern = '<div class="f14" id="read_tpc">【影片名称】：【MP4】042617_001-ちんぐり返しアナルいじりフェラ<br>【档案大小】：0.9G<br>【档案格式】：MP4<br>【影片时间】：如图<br>'
        # pattern = '<div class="f14" id="read_tpc"><br>【影片名稱】：(.*?)<br>【影片格式】：(.*?)<br>【字幕語言】：(.*?)<br>【是否有碼】：(.*?)<br>【影片大小】：(.*?)<br>'
        pattern = '<div class="f14" id="read_tpc">【影片名称】：(.*?)<br>【档案大小】：(.*?)<br>【档案格式】：(.*?)<br>【影片时间】：(.*?)<br>'
        res_match = re.search(pattern, responsestring)
        print('影片名称：' + res_match.group(1))
        print('影片大小：' + res_match.group(2))
        print('影片时长：' + res_match.group(4))

        pattern_url = '<div class="f14" id="read_tpc">(.*?)</div>'
        res_match_url = re.search(pattern_url, responsestring)

        # print(res_match_url.group(1))

        pattern_turl = '"_blank" >http(.*?)</a>'
        res_match_turl = re.search(pattern_turl, res_match_url.group(1))
        # print(res_match_turl.group(1))

        guid = get_a_uuid()
        turl = 'http' + res_match_turl.group(1)
        file_name = os.path.basename(turl)
        download_torrent(turl, file_name, guid)

        # insert_sql = 'INSERT INTO title_info (id,titledate,titleid,titlename,titlesize,titlelenth,tdurl) VALUES (%s,%s,%s,%s,%s,%s,%s); '
        # data = (guid, tdate, tguid, res_match.group(1), res_match.group(4), res_match.group(2), turl,)
        # helper.execute_modify_sql(insert_sql, data)
        inserttitleinfo(guid, tdate, tguid, res_match.group(1), res_match.group(4), res_match.group(2), turl)

        pattern_photo = '<img src="(.*?)"'
        res_match_photo = re.findall(pattern_photo, responsestring)
        for purl in res_match_photo:
            if 'http' in purl:
                # print(purl)
                img_name = os.path.basename(purl)
                download_img(purl, img_name, guid, tdate)
    except:
        print('解析模块失败！' + 'has_other_format')


def has_not_format(responsestring, tguid, tdate):
    try:
        # print(responsestring)
        pattern = '<div class="f14" id="read_tpc">【影片名称】：(.*?)<br>【影片大小】：(.*?)<br>【影片时长】：(.*?)<br>'
        res_match = re.search(pattern, responsestring)
        print('影片名称：' + res_match.group(1))
        print('影片大小：' + res_match.group(2))
        print('影片时长：' + res_match.group(3))

        pattern_url = '<div class="f14" id="read_tpc">(.*?)</div>'
        res_match_url = re.search(pattern_url, responsestring)

        # print(res_match_url.group(1))

        pattern_turl = '"_blank" >http(.*?)</a>'
        res_match_turl = re.search(pattern_turl, res_match_url.group(1))
        # print(res_match_turl.group(1))

        guid = get_a_uuid()
        turl = 'http' + res_match_turl.group(1)
        file_name = os.path.basename(turl)
        download_torrent(turl, file_name, guid)

        # insert_sql = 'INSERT INTO title_info (id,titledate,titleid,titlename,titlesize,titlelenth,tdurl) VALUES (%s,%s,%s,%s,%s,%s,%s); '
        # data = (guid, tdate, tguid, res_match.group(1), res_match.group(2), res_match.group(3), turl,)
        # helper.execute_modify_sql(insert_sql, data)
        inserttitleinfo(guid, tdate, tguid, res_match.group(1), res_match.group(2), res_match.group(3), turl)

        pattern_photo = '<img src="(.*?)"'
        res_match_photo = re.findall(pattern_photo, responsestring)
        for purl in res_match_photo:
            if 'http' in purl:
                # print(purl)
                img_name = os.path.basename(purl)
                download_img(purl, img_name, guid, tdate)
    except:
        print('解析模块失败！' + 'has_not_format')


def has_default(responsestring, tguid, tdate):
    try:
        pattern = '<div class="f14" id="read_tpc">(.*?)<br>(.*?)<br>(.*?)<br><br>'
        res_match = re.search(pattern, responsestring)
        print('影片名称：' + res_match.group(1))
        print('影片大小：' + res_match.group(2))
        print('种子编号：' + res_match.group(3))

        pattern_url = '<div class="f14" id="read_tpc">(.*?)</div>'
        res_match_url = re.search(pattern_url, responsestring)
        # print(res_match_url.group(1))
        pattern_turl = '"_blank" >http(.*?)</a>'
        res_match_turl = re.search(pattern_turl, res_match_url.group(1))
        # print(res_match_turl.group(1))

        guid = get_a_uuid()

        turl = 'http' + res_match_turl.group(1)
        file_name = os.path.basename(turl)
        download_torrent(turl, file_name, guid)

        # insert_sql = 'INSERT INTO title_info (id,titledate,titleid,titlename,titlesize,tid,tdurl) VALUES (%s,%s,%s,%s,%s,%s,%s); '
        # data = (guid, tdate, tguid, res_match.group(1), res_match.group(2), res_match.group(3), turl,)
        # helper.execute_modify_sql(insert_sql, data)
        inserttitleinfo(guid, tdate, tguid, res_match.group(1), res_match.group(2), res_match.group(3), turl)

        pattern_photo = '<img src="(.*?)"'
        res_match_photo = re.findall(pattern_photo, responsestring)
        for purl in res_match_photo:
            if 'http' in purl:
                # print(purl)
                img_name = os.path.basename(purl)
                download_img(purl, img_name, guid, tdate)
    except:
        print('解析模块失败！' + 'has_default')


# 获取当前页所包含的内容并请求其他方法解析
def get_page_info_save(url, guid, tdate):
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print('请求连接：' + url)
    # try:
    response = requests.get(url)
    if response.status_code == 200:
        responsestring = response.text
        # print(responsestring)
        responsestring = decode2uft8(responsestring)
        # print(responsestring)

        pattern = ''
        if '【档案格式】' in responsestring:
            has_other_format(responsestring, guid, tdate)
        else:
            if '【影片名称】' in responsestring or '【影片名稱】' in responsestring:
                if '【影片格式】' in responsestring:
                    has_format(responsestring, guid, tdate)
                else:
                    has_not_format(responsestring, guid, tdate)
            else:
                has_default(responsestring, guid, tdate)
        # except:
        #     print('连接请求失败！' + 'get_page_info_save')
    else:
        print('链接请求失败：' + url)


# 获取所有页包含内容
def get_all_url(start, end):
    urltemp = 'https://k6.7086xx.xyz/pw/thread.php?fid=5&type=4&page='
    for num in range(start, end):
        urlquery = urltemp + str(num)
        print('请求页面：' + urlquery)
        response = requests.get(urlquery)
        if response.status_code == 200:
            responsestring = response.text
            responsestring = decode2uft8(responsestring)
            # print(responsestring)

            pattern = '<tr align="center" class="tr3 t_one">(.*?)</tr>'

            res_match = re.findall(pattern, responsestring)
            # print('*'*100)

            for matchfind in res_match:
                # print(matchfind)
                # print('-'*50)
                if '置顶帖标志' not in matchfind:
                    if '精彩合集' not in matchfind:
                        get_page_has_link_save(matchfind)
            time.sleep(2)
        else:
            print('请求页面失败！')


# 首页请求header
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
# 下载请求header
downloadheaders = {
    'authority': 'www1.hgcdown.net',
    'method': 'GET',
    'path': '/Download/72b24683b2ebbb14',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'UM_distinctid=1733c9c8a7fce-0db254c87ac752-376b4502-1fa400-1733c9c8a808bc; _ga=GA1.2.236468174.1594449759; __cfduid=dea1399bf20946908bf2e1c14a7b54a4e1599976534; CNZZDATA1273152310=1852501928-1594448412-https%253A%252F%252Fk6.7086xx.xyz%252F%7C1599973194; _gid=GA1.2.1469093678.1599976537',
    'referer': 'https://www1.hgcdown.net/torrent/34CF7495184CEED40A9361FBFE98B66AD5C688A2',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}


# 电脑关机操作
def shutdownpc(stime):
    print(stime + ' 秒后电脑即将关机！')
    os.system('shutdown /s /f /t ' + stime)


# 默认下载路径
defaultpath = 'H:\\PythonDownload\\Image\\'

if __name__ == '__main__':
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print('Start')
    get_all_url(1, 377)

    # name = 'https://privacypic.com/images/2020/08/13/GIKPYu.jpg'
    # img_name = os.path.basename(name)
    # print(img_name)
    # get_page_info_save('https://k6.7086xx.xyz/pw/html_data/5/2009/4951587.html')
    # get_page_info_save('https://k6.7086xx.xyz/pw/html_data/5/2009/4956093.html')
    # get_page_info_save('https://k6.7086xx.xyz/pw/html_data/5/2009/4954644.html')
    # guid = get_a_uuid()
    # get_page_info_save('https://k6.7086xx.xyz/pw/html_data/5/2009/4953161.html', guid)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print('End')

    shutdownpc(60)
