import re

text = 'He was carefully disguised but captured quickly police.'
 # 找出所有的副词（ly结尾的就是副词）
pattern = '[a-zA-Z]+ly'
res = re.findall(pattern,text)
print(res)