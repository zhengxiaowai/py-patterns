# 结构型模式

- [适配器模式（Adapter）](#适配器模式)
- [外观模式（Facade）](#外观模式)
- [组合模式（Composite）](#组合模式)

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
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class HardWare(object):
    def power_on(self):
        print('上电')

    def bootloader(self):
        print('bootloader 启动')

    def power_off(self):
        print('断电')


class OperatingSystem(object):
    def load_kernel(self):
        print('加载内核')

    def load_image(self):
        print('加载镜像')

    def exit_os(self):
        print('退出操作系统')


class SoftWare(object):
    def load_app(self):
        print('加载应用程序')

    def exit_app(self):
        print('退出应用程序')


class Computer(object):
    def __init__(self):
        self.hw = HardWare()
        self.os = OperatingSystem()
        self.sw = SoftWare()

    def boot(self):
        self.hw.power_on()
        self.hw.bootloader()
        self.os.load_kernel()
        self.os.load_image()
        self.sw.load_app()

    def shut_down(self):
        self.sw.exit_app()
        self.os.exit_os()
        self.hw.power_off()


if __name__ == '__main__':
    computer = Computer()

    print('开机')
    computer.boot()

    print('\n关机')
    computer.shut_down()
```

## 组合模式

### 定义

将对象组合成树形结构以表示 "部分-整体" 的层次结构。Composite 使得用户对单个对象和组合对象的使用具有一致性。

### 动机

组合对象和单一对象拥有一致性，然客户端可以一起处理。

### 适用性

- 想表示对象的部分 -整体层次结构。
- 希望用户忽略组合对象与单个对象的不同，用户将统一地使用组合结构中的所有对象。

### 实现

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Menu(object):
    def __init__(self):
        self.items = []

    def add(self, menu):
        self.items.append(menu)

    def printer(self):
        for item in self.items:
            item.printer()


class MenuItem(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def add(self):
        raise AttributeError('MenuItem is not supported add methid')

    def printer(self):
        print(self.name, self.price)


if __name__ == '__main__':
    menu = Menu()

    launch_item1 = MenuItem('meet', 15)
    launch_item2 = MenuItem('rice', 7)
    launch_item3 = MenuItem('noddles', 10)
    menu.add(launch_item1)
    menu.add(launch_item2)
    menu.add(launch_item3)

    drink_menu = Menu()

    drink_item1 = MenuItem('milk', 5)
    drink_item2 = MenuItem('tea', 4)
    drink_item3 = MenuItem('coffee', 6)
    drink_menu.add(drink_item1)
    drink_menu.add(drink_item2)
    drink_menu.add(drink_item3)

    menu.add(drink_menu)

    menu.printer()
```