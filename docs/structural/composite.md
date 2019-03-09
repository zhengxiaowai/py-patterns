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