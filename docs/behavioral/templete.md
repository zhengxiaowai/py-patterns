## 模板方法模式

### 定义

在一个方法中定义一个算法的骨架，而将一些步骤延迟到子类中。模板方法使得子类可以在不改变算法结构的情况下，重新定义算法中的某些步骤。

### 动机

设计一个应用框架，这个框架按照固定的流程实现，但是某些方法需要子类来提供。也可以提供钩子，让子类来决定做什么。

### 适用性

- 一次性实现一个算法的不变部分，将可变的行为留给子类实现。
- 各子类中公共方法的行为应被提取出来并集中到一个公共父类中以避免代码重复。
- 控制子类扩展，在特定的点调用钩子操作，只允许在这些点进行扩展。

### 实现

```python
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
```