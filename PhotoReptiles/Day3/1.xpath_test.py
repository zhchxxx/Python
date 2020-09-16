import requests
from lxml import etree

url = 'http://lol.178.com/'
response = requests.get(url)
# with open('lol.html','wb') as f:
#     f.write(response.content)

html_ele = etree.HTML(response.text)
print(html_ele)

# 使用xpath
title = html_ele.xpath('/html/head/title')[0]
print(title)

# 获取title内的文字，xpath函数 text()
title = html_ele.xpath('/html/head/title/text()')[0]
print(title)

meta_ele_list = html_ele.xpath('/html/head/meta')
print(meta_ele_list)

# 需要标签的属性信息怎么办, /html/head/meta[1]/@charset
charset_list = html_ele.xpath('/html/head/meta[1]/@charset')[0]
print(charset_list)

li_ele = html_ele.xpath('//li[@class="news-box-big"]/a/span/p/text()')[0]
print(li_ele)