#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://blog.csdn.net/enjoyyl
# @Version : $1.0$

import random


def randperm(start, end, num):
    """random permutation.

    returns a row vector containing ``num`` unique integers
    selected randomly from ``start:end``.  For example,
    randperm(3, 10, 3) might be [9, 4, 7].

    Arguments:
      start {[number]} -- [start number]
      end {[number]} -- [end number]
      num {[number]} -- [number of unique integers]

    Returns:
      [type] -- [description]
    """
    R = random.sample(range(start, end), num)
    return R


if __name__ == '__main__':

    x = randperm(3, 10, 3)
    print(x)
