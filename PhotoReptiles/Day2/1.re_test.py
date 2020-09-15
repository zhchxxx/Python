import re

text = '<div class="anci_header_content"><div class="article-title"><h2>2021款斯巴鲁翼豹美国上市 售18795美元起</h2></div><div class="article-desc clearfix"><div class="author-icon"><img src="https://pic.rmb.bdstatic.com/bjh/user/08b8702d4245a519e343e2447d4e32a0.jpeg"><i class="author-vip author-vip-2"></i></div><div class="author-txt"><p class="author-name">太平洋汽车网</p><div class="article-source article-source-bjh"><span class="date">发布时间：09-06</span><span class="time">12:09</span><span class="account-authentication">太平洋汽车网官方百家号</span></div></div></div></div>'
pattern = '<h2>(.*)</h2>'

title_text = re.search(pattern,text)
print(title_text.group(1))