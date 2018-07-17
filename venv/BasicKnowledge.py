a = '''This symbol has more lines
one line
two line
three line'''
print(a)
# ====================
#格式化方法format
age = 20
name = 'Swaroop'
print('{0} was {1} years old.'.format(name,age),end=' ')
print('{0} is playing'.format(name))
print('{0:.3f}'.format(1.0/3))  #三位浮点数
print('{0:_^11}'.format('hello'))   #总字符长为11并用下划线填充使其对称
print('{name} wrote {book}'.format(name = "Hebe",book = "<<Life>>"))

print('This is a string. \
This continues the string') #字符串结尾处的\表示"不换行"
