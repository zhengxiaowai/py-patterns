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
