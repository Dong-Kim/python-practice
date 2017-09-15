#!/usr/bin/env python
#-*- coding:utf-8 -*-

places = {'山西省':{'运城市':['闻喜县','陶村镇'],
                   '太原市':['X县','Y镇']},
            '河北省':{'保定市':['Q县','W镇'],
                    '廊坊市':['A县','B镇']}}

#定义一个打印菜单的函数。便于调用输出菜单
def menu():
    for p,c in places.items():
        print('-------------------')
        print(p)
        for city,zhen in c.items():
            print(city,'\n',zhen)

#TAG控制整体循环。逻辑很清晰。写的比较啰嗦
TAG=True
while TAG:
    print(menu())
    print("退出请输入'quit'")
    province = input('输入省份->')
    if province == 'quit':
        TAG = False
    elif province not in places:
        continue
    while TAG:
        print('包含如下城市%s' %list(places[province].keys()))
        print("返回上一级菜单请输入'back'，退出请输入'quit'，查看菜单请输入'menus'")
        city = input('输入城市->')
        if city == 'menus':
            print(menu())
            continue
        elif city == 'back':
            break
        elif city == 'quit':
            TAG=False
        elif city not in places[province]:
            continue
        while TAG:
            print('包含如下县镇%s' %places[province][city])
            print('END')
            print("返回上一级菜单请输入'back'，退出请输入'quit'，查看菜单请输入'menus'")
            operate = input('继续输入操作->')
            if operate == 'menus':
                print(menu())
            elif operate == 'back':
                break
            elif operate == 'quit':
                TAG=False
            elif operate not in places[province]:
                continue

