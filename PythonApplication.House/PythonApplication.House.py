from typing import List, Union

import requests
from bs4 import BeautifulSoup, NavigableString

headers = {
'Authority': 'gz.centanet.com',
'Method': 'GET',
'Path': '/ershoufang/',
'Scheme': 'https',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Cookie': 'acw_tc=1bdd1e1b15989260782651302e4b6528a41c1b7d182717d151f64532b0; Y190cmFja2lk=48f8bdf9aa4b4a8bbfc7d960383d8043; gr_user_id=03dbbe28-7f57-4239-b1c7-e46dafb3a5c8; grwng_uid=e08c5154-cf07-43ad-9ecb-244fa4204615; acw_sc__v2=5f4ef2ee864cdb097080421033ba365516e0bed0; ae0860c7e1026caa_gr_session_id=f4db51b9-74b0-42a3-bb8a-39f65ecc2a1a; Hm_lvt_2601a0f4477572ee12d6c06945adc380=1598926080,1598929735,1599009519; Hm_lpvt_2601a0f4477572ee12d6c06945adc380=1599009519; _pk_id.24.7326=8b96177692d63223.1598926080.3.1599009519.1598944800.; _pk_ses.24.7326=*; ae0860c7e1026caa_gr_session_id_f4db51b9-74b0-42a3-bb8a-39f65ecc2a1a=true',
'Referer': 'https://gz.centanet.com/ershoufang/',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
url = 'https://gz.centanet.com/ershoufang/'
#url = 'https://www.hao123.com/'
urlhtml=requests.get(url,headers = headers)
#urlhtml.encoding='utf-8'

soup=BeautifulSoup(urlhtml.text,'html.parser')

alinks = []
alink = soup.find_all('h4')
alinks.append(alink)
print(alink)

alink = soup.find_all('li',)
alinks.append(alink)
print(alink)

alink = soup.find(id='feed_news_list')
alinks.append(alink)
print(alinks)

#alink = soup.find_all('li',class_= 'feed_news_item hasimg fadeInDown animated')
#alinks.append(alink)
#print(alink)

#print("Start")
#print(alink)
#print("End")

#def parse_single_html(html):
#    soup = BeautifulSoup(html,'html.parser')
#    articles = soup.find_all('a',class_="cBlueB")

#    datas = []
#    for art in articles:
#        title_node = (
#            art
#            .find("a"))

#        title = title_node.get_text();
#        link = title_node["href"]

#        datas.append({"title":title,"link":link})
#    return datas

#for link in alink:
#    temp =  parse_single_html(str(link))
#    print(temp)
