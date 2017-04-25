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
