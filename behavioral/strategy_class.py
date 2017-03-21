#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 定义一系列计算年终奖的算法
bouns_strategy = {
    'S': lambda s: s * 4,
    'A': lambda s: s * 3,
    'B': lambda s: s * 2,

    # 添加 S+ 和 C 算法
    'SP': lambda s: s * 5,
    'C': lambda s: s ,
}


class Bouns:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        # 计算方法通过属性来设定，这样可以容易被替换
        self.calculate = None

    def __str__(self):
        return "{} get {}".format(self.name, self.bouns)

    @property
    def bouns(self):
        return self.calculate(self.salary)


if __name__ == '__main__':
    jack_bouns = Bouns('jack', 10000)
    jack_bouns.calculate = bouns_strategy['S']
    print(jack_bouns)

    linda_bouns = Bouns('linda', 10000)
    linda_bouns.calculate = bouns_strategy['A']
    print(linda_bouns)

    sean_bouns = Bouns('sean', 10000)
    sean_bouns.calculate = bouns_strategy['B']
    print(sean_bouns)

    # 现在需求变化了，添加 S+ 作为最高级，C 级 作为最低级
    # jack 从 S 调整到 S+
    # sean 从 B 调整到 C
    print('需求改变以后......')

    jack_bouns.calculate = bouns_strategy['SP']
    print(jack_bouns)

    print(linda_bouns)

    sean_bouns.calculate = bouns_strategy['C']
    print(sean_bouns)

    # 从上面的计算年终的算法可以看出
    # 需求改变以后只需要替代原来算法就可实现了
