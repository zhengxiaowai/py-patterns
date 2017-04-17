#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 定义一系列计算年终奖的算法
bouns_strategy = {
    'S': lambda s: s * 4,
    'A': lambda s: s * 3,
    'B': lambda s: s * 2,

    # 添加 S+ 和 C 算法
    'SP': lambda s: s * 5,
    'C': lambda s: s,
}


def calculate_bouns(name, strategy, salary):
    return '{name} get {salary}'.format(name=name, salary=strategy(salary))


if __name__ == '__main__':
    print(calculate_bouns('jack', bouns_strategy['S'], 10000))
    print(calculate_bouns('linda', bouns_strategy['A'], 10000))
    print(calculate_bouns('sean', bouns_strategy['B'], 10000))

    # 现在需求变化了，添加 S+ 作为最高级，C 级 作为最低级
    # jack 从 S 调整到 S+
    # sean 从 B 调整到 C
    print('需求改变以后......')

    print(calculate_bouns('jack', bouns_strategy['SP'], 10000))
    print(calculate_bouns('linda', bouns_strategy['A'], 10000))
    print(calculate_bouns('sean', bouns_strategy['C'], 10000))
