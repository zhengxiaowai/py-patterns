#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


class Pizza(object):
    """ Pizza 抽象类 """

    def __init__(self):
        self.name = self.getPizzaName()

    def prepare(self):
        print('准备...')

    def bake(self):
        print('烘焙...')

    def cut(self):
        print('切片...')

    def box(self):
        print('装盒...')


class NYStyleCheesePizza(Pizza):
    """ Pizza 子类 """

    def getPizzaName(self):
        return '纽约风味 cheese 披萨'


class ChicagoCheesePizza(Pizza):
    """ Pizza 子类 """

    def getPizzaName(self):
        return '芝加哥风味 cheese 披萨'

    def cut(self):
        """ 覆盖父类方法 """
        print('方块切片...')


class PizzaStore(object):
    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class NYPizzaStore(PizzaStore):
    def create_pizza(self, item):
        if item == 'cheese':
            return NYStyleCheesePizza()
        elif item == 'veggie':
            # 同上
            pass


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, item):
        if item == 'cheese':
            return ChicagoCheesePizza()
        elif item == 'veggie':
            # 同上
            pass


if __name__ == '__main__':
    ny_pizza_store = NYPizzaStore()
    ny_cheese_pizza = ny_pizza_store.order_pizza('cheese')
    print('获得 {}'.format(ny_cheese_pizza.name))

    print('\n')

    chicago_pizza_store = ChicagoPizzaStore()
    chicago_cheese_pizza = chicago_pizza_store.order_pizza('cheese')
    print('获得 {}'.format(chicago_cheese_pizza.name))
