#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class CaffeineBeverage(metaclass=ABCMeta):
    def make_beverage(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if (self.customer_want_condiments()):
            self.add_condiments()

    def boil_water(self):
        print('把水烧开')

    def pour_in_cup(self):
        print('倒入杯子中')

    def customer_want_condiments(self):
        # hook
        return False

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass


class Tea(CaffeineBeverage):
    def brew(self):
        print('用沸水浸泡茶叶')

    def customer_want_condiments(self):
        return True

    def add_condiments(self):
        print('添加柠檬')


class Coffee(CaffeineBeverage):
    def brew(self):
        print('用沸水冲泡咖啡')

    def customer_want_condiments(self):
        return False

    def add_condiments(self):
        print('添加牛奶和糖')


if __name__ == '__main__':
    print('制作咖啡：')
    coffee = Coffee()
    coffee.make_beverage()
    print('\n制作茶：')
    tea = Tea()
    tea.make_beverage()
