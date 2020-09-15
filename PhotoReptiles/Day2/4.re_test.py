import re

# line = 'sss127'
# # | 表示或者
# pattern = '(sss|127)'
# res_match = re.search(pattern,line)
# print(res_match)

# [] 代表的是：中括号内的字符可以被匹配
#  [123] = (1|2|3)

# pattern = '[123]+'
# line = 'sss127'
# res_match = re.search(pattern,line)
# print(res_match)

 # 数字是0-9，数字是 \d = [0123456789] = [0-9]
# [abc],如果想要表示小写字母[a-z]
# [acb],如果想要表示大写字母[A-Z]

# 邮箱格式怎么写
# zhchxxx@126.com
# ^[0-9a-zA-Z_]+@[0-9a-zA-Z_]+\.[a-z]+
# \w+@\w+\.[a-z]
# 如果想要确切的匹配之前的特殊字符，需要用转义符号\
# pattern = '^[0-9a-zA-Z_]+@[0-9a-zA-Z_]+\.[a-z]+'
# email = 'zhchxxx@126.com'
# res_match = re.search(pattern,email)
# print(res_match)

# '^'在字符串最前表示为以什么开头
# [^]表示为非的功能
