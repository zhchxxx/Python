print("hello world!");
print("Hello Python!");
if True:
    print("True")
else:
    print("False")

str = 'Runoob'
print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str *2)
print(str + '你好')
print('----------------------------')
print('hello\nrunoob')
print(r'hello\nrunoob')

#input('\n\n按下Enter键后退出')

import sys; x = 'runoob'; sys.stdout.write(x + '\n')

x="a"
y="b"
# 换行输出
print( x )
print( y )
 
print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()


days = ['Monday','Tuesday','Wednesday','Thursday','Friday']
#a = input("按下 enter 键退出，其他任意键显示...\n")
#print(a)
print()

list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list)               # 输出完整列表
print (list[0])            # 输出列表的第一个元素
print (list[1:3])          # 输出第二个至第三个元素 
print (list[2:])           # 输出从第三个开始至列表末尾的所有元素
print (tinylist * 2)       # 输出列表两次
print (list + tinylist)    # 打印组合的列表


tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
#tuple[2] = 1000    # 元组中是非法应用
list[2] = 1000     # 列表中是合法应用

print(tuple[2])
print(list[2])


dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
 
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one'])          # 输出键为'one' 的值
print (dict[2])             # 输出键为 2 的值
print (tinydict)             # 输出完整的字典
print (tinydict.keys())      # 输出所有键
print (tinydict.values())    # 输出所有值

a = 21
b = 10
c = 0
 
c = a + b
print ("1 - c 的值为：", c)
 
c = a - b
print ("2 - c 的值为：", c )
 
c = a * b
print ("3 - c 的值为：", c )
 
c = a / b
print ("4 - c 的值为：", c )
 
c = a % b
print ("5 - c 的值为：", c)
 
# 修改变量 a 、b 、c
a = 2
b = 3
c = a**b 
print ("6 - c 的值为：", c)
 
a = 10
b = 5
c = a//b 
print ("7 - c 的值为：", c)

