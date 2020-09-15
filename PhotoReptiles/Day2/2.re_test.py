import re
# 写什么样子的模式

# line = 'huang123'

# *代表出现零次或多次

# 1.以 h 开头
# ^代表着以后面的字符作为开头
# pattern = '^h'
# res_math = re.search(pattern,line)
# print(res_math)

# 2.以h开头后面跟着一个字符,如果是一个字符则是‘^h.’，如果是任意字符则是'^h*'
# pattern = '^h*'
# res_math = re.search(pattern,line)
# print(res_math)

# 3. 以h开头后面跟着任意数兵的数字，‘\d’标示数字
# line = 'h123456789'
# pattern = '^h\d*'
# res_math = re.search(pattern,line)
# print(res_math)

# 4.以3结尾
# pattern = '3$'
# res_math = re.search(pattern,line)
# print(res_math)

# 5.以h开头，以3结尾，中间T看一个字符申
# pattern = '^h.3$'
# line = 'hj3'
# res_match = re.search(pattern,line)
# print(res_match)

# 6.以h开头，以3结尾。中间可以存在任意数量的字符串
# pattern = '^h.*3$'
# line = 'h1111112222233333'
# res_match = re.search(pattern,line)
# print(res_match)

# 7.以h开头，以3结尾。输出中间任意数量的字符串
# .能够匹配任意的字符，例外：\n
# 如果需要匹配换行符‘.’，添加一个flag
# 添加的标志就是 re.S
# pattern = '^h(.*)j$'
# line = 'h111222333444555j'
# res_match = re.search(pattern,line)
# print(res_match)
# # group(1)输出h与j之间所有字符串
# print(res_match.group(1))

# .能够匹配任意的字符，例外：\n
# 如果需要匹配换行符‘.’，添加一个flag
pattern = '^h(.*)j$'
line = 'h111222\n333444555j'
res_match = re.search(pattern,line,re.S)
print(res_match)
# group(1)输出h与j之间所有字符串
print(res_match.group(1))