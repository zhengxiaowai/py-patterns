#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import namedtuple
from math import cos, sin, pi

# 禁止「构造函数 _create()」导出
__all__ = [
    'ComplexCreator'
]

Complex = namedtuple('Complex', 'x y')


def _create(a, b):
    return Complex(a, b)


class ComplexCreator(object):
    @staticmethod
    def from_cartesian_factory(real, imaginary):
        return _create(real, imaginary)

    @staticmethod
    def from_polar_factory(modulus, angle):
        return _create(modulus * cos(angle), angle * sin(modulus))


if __name__ == '__main__':
    cartesian_complex = ComplexCreator.from_cartesian_factory(3, 4)
    polar_complex = ComplexCreator.from_polar_factory(5, pi)

    print(cartesian_complex, polar_complex)

