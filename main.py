#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SyntaxError(Exception):
    def __init__(self, message):
        self.message = message



class Application:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Lambda:
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr


class Variabl:
    def __init__(self, var):
        self.var = var


def parser(expr):
    if expr.startswith('/'):
        pass

def parse_variable(expr):
    var = ""
    i = 0

    # 1文字目
    if 0 < len(expr) and expr[0].isalpha():
        var += expr[0]
        # 2文字目以降
        i += 1
        while i < len(expr) and expr[i].isalnum():
            var += expr[i]
            i += 1
    return var


if __name__ == '__main__':
    # write your code here
