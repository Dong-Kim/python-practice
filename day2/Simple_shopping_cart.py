#!/usr/bin/env python
#-*- coding:utf-8 -*-


import os
userfile = 'user_info'
menu = [(1,'apple',5000),(2,'mac',7000),(3,'food',10)]
shop = []
money = 0
login_count = 0
if not os.path.isfile(userfile):
    open(userfile,'w').close()

#定义个退出函数，不管在哪里退出时均调用。
def quit():
    print('Shopping included %s , overage %s' %(shop,money))
    exit()

print("Exit the input 'quit'")
while login_count < 3:
    user = input('username-->:')
    passwd = input('password-->:')
    if 'quit' in [user,passwd]: quit()
    for info in open(userfile,'r').readlines():
        username,password = info.split('|')
        if user == username and passwd == password.strip('\n'):
            print('Login successfully!')
            try:
            #判断用户输入的money若不是int则会抛出异常被except捕捉。
                money = int(input('total money:'))
                print('shopping')
                print('Product information (number,commodity,money)',menu)
                while True:
                    shopping = input('Enter the purchased item:')
                    if shopping == 'quit': quit()
                    #以下两个if循环为根据商品ID和商品名称来获取商品并加入购物车及扣费
                    if shopping.isnumeric() and len(shopping)==1:
                        for list in menu:
                            if int(shopping) == list[0] :
                                if list[2] <= money:
                                    shop.append(list)
                                    money -= list[2]
                                    break
                                elif list[2] >= money:
                                    print('Lack of money')
                                    break
                        else:
                            print('Do not have this product')
                    else:
                        for list in menu:
                            if shopping == list[1] :
                                if list[2] <= money:
                                    shop.append(list)
                                    money -= list[2]
                                    break
                                elif list[2] >= money:
                                    print('Lack of money')
                                    break
                        else:
                            print('Do not have this product')
            except ValueError :
                print('Enter the integer')
    else:
        print('username or password is error!')
        login_count += 1
else:
    print('Too many attempts')
    quit()
# print(money)
