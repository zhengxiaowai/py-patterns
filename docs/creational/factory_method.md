## 工厂方法

### 定义

定义一个用于创建对象的接口，让子类决定实例化哪一个类。工厂方法使一个类实例化延迟到其子类。

### 动机

框架使用抽象类定义和维护对象之间的关系。这些对象的创建通常也由框架负责。

### 适用性

- 当一个类不知道它所必须创建的对象的类的时候。
- 当一个类希望由它的子类来指定它所创建的对象的时候。
- 当类将创建对象的职责委托给多个帮助子类中的某一个，并且你希望将哪一个帮助子类是代理者这一信息局部化的时候。

### 优缺点

- 不绑定特定应用相关的类到代码中。
- 需要为每一个特定情况创建一个子类

### 实现

> 有两个披萨店，提供纽约风味披萨和芝加哥风味披萨——《Head First 设计模式》

```python
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
```