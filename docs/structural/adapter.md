
## 适配器模式

### 定义

将一个类的接口转换成客户希望的另外一个接口。

### 动机

有时，为复用而设计的工具箱类不能够被复用的原因仅仅是因为它的接口与专业应用领域所需要的接口不匹配。

### 适用性

- 你想使用一个已经存在的类，而它的接口不符合你的需求。
- 你想创建一个可以复用的类，该类可以与其他不相关的类或不可预见的类（即那些接口可能不一定兼容的类）协同工作。
- （仅适用于对象 Adapter ）你想使用一些已经存在的子类，但是不可能对每一个都进行子类化以匹配它们的接口。对象适配器可以适配它的父类接口。

### 实现

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