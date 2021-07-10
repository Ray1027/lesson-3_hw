import random

x=input('請猜一個數字')
x=int(x)
num=random.randint(1,20)
t=1

while t<5 and x!=num:
    if x>num:
        print('數字太大了,請再猜一次')
    elif x<num:
        print('數字太小了,還剩五次機會')
    x=input('請輸入大小')
    x=int(x)
    t=t+1
    
if t==5:
    print('恭喜答對!')
    print ('你玩了',t,'次')
elif x!=num:
    print('很抱歉，沒有機會了')
