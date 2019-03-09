## 迭代器模式

### 定义

提供一种方法顺序访问一个聚合对象中各个元素 , 而又不需暴露该对象的内部表示。

### 动机

不同的对象有不同的遍历方式，即使可以 预见到所需的那些遍历操作，你可能也不希望列表的接口中充斥着各种不同遍历的操作。
有时还可能需要在同一个表列上同时进行多个遍历。

### 适用性

- 访问一个聚合对象的内容而无需暴露它的内部表示。
- 支持对聚合对象的多种遍历。
- 为遍历不同的聚合结构提供一个统一的接口 (即, 支持多态迭代)。

### 实现

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BreakfastMenu(object):
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append((name, price))

    def __iter__(self):
        """ return a Iterable object """
        return iter(self.items)


class LaunchMenu(object):
    def __init__(self):
        self.items = set()

    def add_item(self, name, price):
        self.items.add((name, price))

    def __iter__(self):
        """ return a Iterable object """
        return iter(self.items)


class DinnerMenu(object):
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price

    def __iter__(self):
        """ return a Iterable object """
        return iter(((name, price) for name, price in self.items.items()))


if __name__ == '__main__':
    breakfast_menu = BreakfastMenu()
    breakfast_menu.add_item('milk', 5)
    breakfast_menu.add_item('bread', 6)
    breakfast_menu.add_item('coffee', 7)
    breakfast_menu.add_item('donuts', 3)

    print('\nBreakfastMenu:')
    for item in breakfast_menu:
        print(item)

    launch_menu = LaunchMenu()
    launch_menu.add_item('milk', 5)
    launch_menu.add_item('bread', 6)
    launch_menu.add_item('coffee', 7)
    launch_menu.add_item('donuts', 3)

    print('\nLaunchMenu:')
    for item in launch_menu:
        print(item)

    dinner_menu = DinnerMenu()
    dinner_menu.add_item('milk', 5)
    dinner_menu.add_item('bread', 6)
    dinner_menu.add_item('coffee', 7)
    dinner_menu.add_item('donuts', 3)

    print('\nDinnerMenu:')
    for item in dinner_menu:
        print(item)
```