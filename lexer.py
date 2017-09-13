#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

PUNCTATION = ["λ", "|", "(", ")"]
WHITESPACE = list(string.whitespace)

class Token:
    def __init__(self, kind, value):
        self.kind = kind
        self.value = value
    def __repr__(self):
        return "Token(kind:'{}' value:{})".format(self.kind, self.value)

class Lexer(object):
    def __init__(self, source):
        self.source = source
        self.size = len(source)
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        self._clear_whitespace()

        if self.position > self.size:
            raise StopIteration()
        elif self.position == self.size:
            self.position += 1
            return Token('EOF', None)
        elif self._present_character() in PUNCTATION:
            char = self._present_character()
            self.position += 1
            return Token(char, None)
        else:
            symbol = ''
            while (self.position < self.size and
                    not self._present_character() in PUNCTATION + WHITESPACE):
                symbol += self._present_character()
                self.position += 1
            return Token("SYMBOL", symbol)

    def _clear_whitespace(self):
        while (self.position < self.size and
                self._present_character() in WHITESPACE):
            self.position += 1
    def _present_character(self):
        return self.source[self.position]
