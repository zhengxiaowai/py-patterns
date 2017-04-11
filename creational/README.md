# 创建型模式

创建型模式抽象了实例化过程。

它们帮助一个系统独立于如何创建、组合和表示它的那些对象。一个类创建型模式使用继承改变被实例化的类，而一个对象创建型模式将实例化委托给另一个对象。

在这些模式中有两个不断出现的主旋律：

- 它们都将关于该系统使用哪些具体的类的信息封装起来。
- 它们隐藏了这些类的实例是如何被创建和放在一起的。

整个系统关于这些对象所知道的是由抽象类所定义的接口。因此，创建型模式在什么被创建， 谁创建它，它是怎样被创建的，以及何时创建这些方面给予你很大的灵活性。

- [工厂方法（Factory Method）](#工厂方法)
- [抽象工厂（Abstract Factory）](#抽象工厂)
- [单例模式（Singleton）](#单例模式)

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

## 抽象工厂

### 定义

提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类。

### 动机

创建一系列相关的类，每一类都有一个抽象类，其子类负责具体实现。

### 适用性

在以下情况可以使用 Abstract Factory模式：

- 一个系统要独立于它的产品的创建、组合和表示时。
- 一个系统要由多个产品系列中的一个来配置时。
- 当你要强调一系列相关的产品对象的设计以便进行联合使用时。
- 当你提供一个产品类库，而只想显示它们的接口而不是实现时。

### 优缺点

- 易于添加新的抽象子类
- 难于添加新的抽象类
- 数量庞大的类难以管理

### 实现

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dougth(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass

    @abstractmethod
    def create_cheese(self):
        pass

    @abstractmethod
    def create_vegies(self):
        pass

    @abstractmethod
    def create_pepperoni(self):
        pass

    @abstractmethod
    def create_clam(self):
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def __init__(self):
        self._location = type(self).__name__

    def create_dougth(self):
        return self._location + ' dougth'

    def create_sauce(self):
        return self._location + ' sauce'

    def create_cheese(self):
        return self._location + ' cheese'

    def create_vegies(self):
        return self._location + ' vegies'

    def create_pepperoni(self):
        return self._location + ' pepperoni'

    def create_clam(self):
        return self._location + ' clam'


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def __init__(self):
        self._location = type(self).__name__

    def create_dougth(self):
        return self._location + ' dougth'

    def create_sauce(self):
        return self._location + ' sauce'

    def create_cheese(self):
        return self._location + ' cheese'

    def create_vegies(self):
        return self._location + ' vegies'

    def create_pepperoni(self):
        return self._location + ' pepperoni'

    def create_clam(self):
        return self._location + ' clam'


class Pizza(ABC):
    def __init__(self):
        self._dougth = ''
        self._sauce = ''
        self._cheese = ''
        self._vegies = ''
        self._pepperoni = ''
        self._clam = ''

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print('烘焙...')

    def cut(self):
        print('切片...')

    def box(self):
        print('装盒...')


class CheesePizza(Pizza):
    def __init__(self, factory):
        super(CheesePizza, self).__init__()
        self._factory = factory

    def prepare(self):
        print('准备 CheesePizza 中...')
        self._dougth = self._factory.create_dougth()
        self._sauce = self._factory.create_sauce()
        self._cheese = self._factory.create_cheese()

    def __str__(self):
        return 'CheesePizza 有: {}, {}, {}'.format(
            self._dougth, self._sauce, self._cheese)


class ClamPizza(Pizza):

    def __init__(self, factory):
        super(ClamPizza, self).__init__()
        self._factory = factory

    def prepare(self):
        print('准备 ClamPizza 中...')
        self._dougth = self._factory.create_dougth()
        self._sauce = self._factory.create_sauce()
        self._cheese = self._factory.create_cheese()
        self._clam = self._factory.create_clam()

    def __str__(self):
        return 'CheesePizza 有: {}, {}, {}, {}'.format(
            self._dougth, self._sauce, self._cheese, self._clam)


class PizzaStore(ABC):
    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self):
        pass


class NYPizzaStore(PizzaStore):
    def create_pizza(self, item):
        ny_pizza_ingredient_factory = NYPizzaIngredientFactory()
        if item == 'cheese':
            return CheesePizza(ny_pizza_ingredient_factory)
        elif item == 'clam':
            return ClamPizza(ny_pizza_ingredient_factory)


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, item):
        chicago_pizza_ingredient_factory = ChicagoPizzaIngredientFactory()
        if item == 'cheese':
            return CheesePizza(chicago_pizza_ingredient_factory)
        elif item == 'clam':
            return ClamPizza(chicago_pizza_ingredient_factory)


if __name__ == '__main__':
    # 纽约披萨店
    ny_pizza_store = NYPizzaStore()
    ny_pizza1 = ny_pizza_store.order_pizza('cheese')
    print(ny_pizza1)

    ny_pizza2 = ny_pizza_store.order_pizza('clam')
    print(ny_pizza1)

    # 芝加哥披萨店
    chicago_pizza_store = ChicagoPizzaStore()
    chicago_pizza1 = chicago_pizza_store.order_pizza('cheese')
    print(chicago_pizza1)

    chicago_pizza2 = chicago_pizza_store.order_pizza('clam')
    print(chicago_pizza1)

```

## 单例模式

### 定义

保证一个类仅有一个实例，并提供一个访问它的全局访问点。

### 动机

在实际编程中，有的时候制造出多个实例，就会导致许多问题的产生。例如，程序的异常行为，资源使用过量，或者是不一致的结果。

## 适用性

- 当类只能有一个实例而且客户可以从一个众所周知的访问点访问它时。
- 当这个唯一实例应该是通过子类化可扩展的，并且客户应该无需更改代码就能使用一个扩展的实例时。

### 优缺点

- 对实例受控访问
- 缩小命名空间
- 允许对操作和表示的精化 
- 允许可变数目的实例
- 比类操作更灵活

### 实现

```python
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass(object):
    __metaclass__ = Singleton
```