#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Duck(object):
    """ 鸭子的动作 """
    def quack(self):
        print('Quack')
    
    def fly(self):
        print('fly')


class Turkey(object):
    """ 火鸡的动作 """
    def gobble(self):
        print('gobble')
    
    def fly(self):
        print('fly a short distaance')

class TurkeyAadpter(object):
    """ 火鸡适配器，转化成鸭子 """
    def __init__(self, turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()
    
    def fly(self):
        """ 火鸡飞行距离是鸭子的五分之一 """
        for _ in range(5):
            self.turkey.fly()

def duck_activity(duck):
    duck.quack()
    duck.fly()

if __name__ == '__main__':
    # 鸭子正常活动
    duck = Duck()
    duck_activity(duck)

    # 某天鸭子走丢了，一只火鸡冒充了鸭子
    turkey = Turkey()
    duck_activity(TurkeyAadpter(turkey))

