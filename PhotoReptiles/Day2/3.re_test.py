import re

line = 'aha1ha2ha3ha4ha5ha6ha7ha8ha9123'

# 1.获取第一个h和第二个h之间的内容
# 2.使用非贪婪限定符 ?
# ?是非贪婪限定符

# pattern = 'ah(.*)ha2ha3ha4ha5ha6ha7ha8ha9123'
# res_match = re.search(pattern,line)
# print(res_match)
# print(res_match.group(1))

# pattern = 'ah(.*?)h'
# res_match = re.search(pattern,line)
# print(res_match)
# print(res_match.group(1))

# * 表示 0 - 无穷个
# ? 的另一个用法，可以表示0-1个

pattern = '^h.?3$'
line = 'he3'
res_match = re.search(pattern,line)
print(res_match)
print(res_match.group(0))
# print(res_match.group(1))

# ? 什么时候是费贪婪限定符，什么时候是0-1个
# 如果?前面是分子赴，那么他代表0-1个前面字符，如果前面是个数限定符，就是非贪婪模式
# {1,} 等于+
# + 就是前面的字符出现一次到无穷次
# {,8} 前面如果不写内容就是0

# {，} 0-无穷
#  + = {1，}
#  * = {0，}
#  ? = {0,1}
#  h{5} = hhhhh 这个代表前面的内容出现五次