import random
num=random.randint(1,20)
t=0
t=t+1

x=input('請猜一個數字')
x=int(x)
while x>num:
    print('數字太大了,請再猜一次')
    x=input('請再猜一次')
    x=int(x)
while x<num:
    print('數字太小了,還剩五次機會')
    x=input('請再猜一次')
    x=int(x)
while t==5:
    print('很抱歉，沒有機會了') 
    x=input('請重試')
    x=int(x)
if x==num:
    x=int(x)
    print('恭喜答對!')
