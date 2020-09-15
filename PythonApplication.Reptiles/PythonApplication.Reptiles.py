
#import requests
#from bs4 import BeautifulSoup
#import pprint
#import json

#def download_all_htmls():
#    htmls = []
#    for idx in range(1):
#        url = "https://www.360kuai.com/9b8e4c67503757242?scene=&uid=1ece3a683752a5320c72a3d25b85e7d1&sign=360_79aabe15&tj_url=9b8e4c67503757242&refer_scene="
#        print(url)
#        r = requests.get(url);
#        if r.status_code != 200:
#            raise Exception("Error")
#        htmls.append(r.text)
#    return htmls

#def parse_single_html(html):
#    soup = BeautifulSoup(html,'html.parser')
#    articles = soup.find_all('card-liner')

#    datas = []
#    for art in articles:
#        title_node = (
#            art
#            .find("h1",class_ ="card__title")
#            .find("a"))

#        title = title_node.get_text();
#        link = title_node["href"]

#        datas.append({"title":title,"link":link})
#    return datas
#    #for articls in articles:
#    #    title_node = ()

#htmls = download_all_htmls()

#print(htmls)

#print("节点开始"+ "\n")

#for html in htmls:
#    temp=  parse_single_html(html)
#    print(temp)

import requests
from bs4 import BeautifulSoup
 
url = 'https://gz.centanet.com/ershoufang/'
urlhtml=requests.get(url)
urlhtml.encoding='utf-8'

soup=BeautifulSoup(urlhtml.text,'html.parser')

alink = soup.find_all("h4",class_= "house-title")

print(alink)

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
