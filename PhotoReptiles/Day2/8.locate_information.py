import requests
import re
from w3lib.html import  remove_tags

# title
# source
# time
# content

# 爬虫第三步
url = 'https://baijiahao.baidu.com/s?id=1677461156592953023&wfr=spider&for=pc'
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