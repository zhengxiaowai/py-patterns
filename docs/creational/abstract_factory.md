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