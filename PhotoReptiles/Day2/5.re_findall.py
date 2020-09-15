import  re

# line ='I want to be hero'
# pattern = '[a-zA-Z-]+'

# findall 的作用是找到所有的匹配项
# 返回值是 所有找到内容的字符串的列表
# res_match = re.findall(pattern,line)
# print(res_match)

# res_match = re.finditer(pattern,line)
# # print(next(res_match))
# for item in res_match:
#     print(item.group(0))

 # compile 的作用：能够生成一个类，这个类用于匹配数据，能够性能够高
# res_match =re.search(pattern,line)
# print(res_match)
# # 上面的search就等于下面的两行
# pat = re.compile(pattern)
# res_match = pat.search(line)
# print(res_match)

# 类的频繁的创建与删除会造成很大的性能问题
# 如果循环匹配内容时候，就需要用compile函数生成一个类
# lines = [
#     'I want to be hero',
#     'M want to be hero',
#     'N want to be hero',
#     'J want to be hero'
# ]
#
# pat = re.compile(pattern)
# for line in lines:
#     res_match = pat.search(line)
#     print(res_match)

line ='I want to be hero'
pattern = '[a-zA-Z-]+'

res = re.sub(pattern,'words',line)
print(res)