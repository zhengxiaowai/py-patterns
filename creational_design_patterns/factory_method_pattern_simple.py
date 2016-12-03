#!/usr/bin/env python
# -*- coding:utf-8 -*-

__all__ = [
    "image_reader_factory"
]


def gif_reader(image_file_path):
    return 'gif reader created'


def jpeg_reader(image_file_path):
    return 'jpeg reader created'


def image_reader_factory(image_file_path):
    reader = None
    if image_file_path.endswith('gif'):
        reader = gif_reader(image_file_path)
    elif image_file_path.endswith('jpeg'):
        reader = jpeg_reader(image_file_path)
    else:
        raise ValueError('invalid image type')

    return reader

if __name__ == '__main__':
    gif = image_reader_factory('hexiangyu.gif')
    jpeg = image_reader_factory('zhengxiaowai.jpeg')

    print(gif, jpeg)