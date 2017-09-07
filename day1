#!/usr/bin/env python
import os

user_dic = {
    'jyd' : {'password': 'abc', 'count': 0},
    'test': {'password': 'test', 'count': 0}
}
if not os.path.isfile('lock'):
    open('lock','w').close()
total_error = 0
print("Exit from the username and enter : quit")
while total_error < 9 :
    user = input('username-->:')
    if user == 'quit':
        break
    if user in user_dic.keys():
#看锁文件中是否有该用户，若有则被锁并重定义lock_u为yes，再跳出锁判断循环。根据lock_u的值确定用户是否被锁。
        lock = open('lock', 'r')
        for lock_u in lock.read().split('\n'):
            if user == lock_u :
                print('User %s is in a locked state' %user)
                lock_u = 'yes'
                break
        lock.close()
        if lock_u == 'yes': continue
        passwd = input('password-->:')
        if passwd == user_dic[user]['password']:
            print('Login successfully!')
            break
        else:
            print('Password error')
        if user_dic[user]['count'] < 3:
            user_dic[user]['count'] += 1
        else:
            lock = open('lock', 'a')
            lock.write(user+'\n')
            print('User %s has been locked' %user)
            break
    else:
        print('Username does not exist.')
    total_error+=1
