# 有1、2、3、4四个数字，能组成多少个互不相同且无重复数字订单三位数
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j & j!=k & k!=i:
#                 print(i, j, k)
# # ----------------------------------------------------------------
# #一个数加100的平方数是一个完全平方数，再加168也是一个完全平方数，求这个数是多少
# import math
# for i in range(1,10000):
#     x=int(math.sqrt(i+100))
#     y=int(math.sqrt(i+268))
#     if (x*x==i+100)& (y*y==i+268):
#         print(i)
# ---------------------------------------------------
#输入某年的某一天，判断它是某年的第几天
# dat=input("请输入年月日,格式为yyyy-mm-dd: ")
# y=int(dat[0:4])  #提取年
# m=int(dat[5:7])  #提取月
# d=int(dat[8:]) #提取天
# ly=False
# if y%400==0:
#     if y%4==0:
#         ly=True
# elif y%4==0:
#     ly=True
# else:
#     ly=False
# if ly==True:
#     ms=[31,29,31,30,31,30,31,31,30,31,30,31]
# else:
#     ms=[31,28,31,30,31,30,31,31,30,31,30,31]
# sum=0
# for i in range(1,13):
#     if i==m:
#         for j in range(i-1):
#             sum=sum+ms[j]
#     else:
#         continue
# print("%s是%s年的第%s天"%(dat,y,sum))
# ----------------------------------------------
#输入三个输入，xyz，请他们由小到大输出
# x=int(input("请输入x: "))
# y=int(input("请输入y: "))
# z=int(input("请输入z: "))
# if x>y:
#     x,y=y,x
# if x>z:
#     x,y=z,x
# if y>z:
#     y,z=z,y
# print(x,y,z)
#用#打印出字母C的图形
# print('*' * 10)
# for i in range(5):
#     print('*        ')
# print('*' * 10)
# 打印楼梯，同时在楼梯上方打印两个笑脸
# import sys
# sys.stdout.write(chr(1))
# sys.stdout.write(chr(1))
# print ('')
#
# for i in range(1,11):
#     for j in range(1,i):
#         sys.stdout.write(chr(219))
#         sys.stdout.write(chr(219))
#     print('')
# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
# isinstance(),判断字符类型内置函数，
# import string
s= input('input a string:\n')
letters=0
space= 0
digit= 0
lowwer=0
upper= 0
others= 0
for c in s:
    if c.isalpha(): #判断是否为字符
        letters+=1
    elif c.isspace():#判断是否为空格
        space+=1
    elif c.isdigit():#判断是否为数字
        digit+=1
    elif c.islower():#判断是否为小写
        lowwer+=1
    elif c.upper():#判断是否为大写
        upper+=1
    else:
        others+=1
print('letters=%d,space=%d,digit=%d,lowwer=%d,upper=%d,others=%d'%(letters,space,digit,lowwer,upper,others))
isinstance()