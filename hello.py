from unicodedata import name

# 四种欢迎光临的表达方式
name = '彭泽昕'
# 1.拼串
print('欢迎'+name+'光临！')
# 2.多个参数    
print('欢迎',name,'光临！')
# 3.占位符
print('欢迎%s光临！'%name)
# 4.格式化字符串
print(f'欢迎{name}光临！')
a = 'abc'
a = a * 20
print(a)
id(name)#找出对象的id
#／/整除，只会保留计算后的整数位，总会返回一个整型
#%取模,两个数相乘的余数                       
#a+=5相当于a =a+5
result='a'>’b'#False,对字符串0进行比较的时候，比较的其实是字符串的unicode的编码，是逐位进行比较的“ab”>"d"还是先a与d去比，编码从小到大编号，所以a比b小
#！= 比  较两个对象的值是否不相等
'''条件运算符在执行时，会先对条件表达式进行求和判断
        如果判断结果为True，则执行语句1，并返回执行结果
        如果判断结果为False，则执行语句2，并返回执行结果
'''
print( A )if True else print( B ) #A
print( A )if False else print( B ) #B
#获取ab之间的最大值
a=30
b=50
max = a if a > b else b
print(max) #b
#input函数用来获取用户的输入，input调用后程序会立机暂停等待用户的输入，用户输入之后回车 