#!/usr/bin/env python
# -*- coding:utf-8 -*-


def create_win_button(button_name):
    # do something for win
    return '{} win button created'.format(button_name)


def create_mac_button(button_name):
    # do something for mac
    return '{} mac button created'.format(button_name)


class ButtonFactory(object):
    def create(self, button_name):
        raise NotImplementedError


class WinButtonFactory(ButtonFactory):
    def create(self, button_name):
        return create_win_button(button_name)


class MacButtonFactory(ButtonFactory):
    def create(self, button_name):
        return create_mac_button(button_name)


if __name__ == '__main__':
    win_button_factory = WinButtonFactory()
    mac_button_factory = MacButtonFactory()

    show_button_on_win = win_button_factory.create('show')
    close_button_on_mac = win_button_factory.create('close')

    print(show_button_on_win, close_button_on_mac)