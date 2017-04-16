# 结构型模式

- [适配器模式（Adapter）](#适配器模式)
- [外观模式（Facade）](#外观模式)

# 适配器模式

## 定义

将一个类的接口转换成客户希望的另外一个接口。

## 动机

有时，为复用而设计的工具箱类不能够被复用的原因仅仅是因为它的接口与专业应用领域所需要的接口不匹配。

## 适用性

- 你想使用一个已经存在的类，而它的接口不符合你的需求。
- 你想创建一个可以复用的类，该类可以与其他不相关的类或不可预见的类（即那些接口可能不一定兼容的类）协同工作。
- （仅适用于对象 Adapter ）你想使用一些已经存在的子类，但是不可能对每一个都进行子类化以匹配它们的接口。对象适配器可以适配它的父类接口。

## 实现

```python
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
```

# 外观模式

## 定义

提供了一个统一的接口，用来访问子系统中的一群接口。外观定义了一个高层接口，让子系统更容易使用。

## 动机

将一个系统划分成为若干个子系统有利于降低系统的复杂性。

## 适用性

- 当你要为一个复杂子系统提供一个简单接口时。
- 客户程序与抽象类的实现部分之间存在着很大的依赖性。
- 当你需要构建一个层次结构的子系统时，使用 Facade 模式定义子系统中每层的入口点 。

## 实现

```python
```

