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
