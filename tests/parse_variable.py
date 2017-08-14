#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os
import unittest

sys.path.append(os.pardir)
import main

class TestStringMethods(unittest.TestCase):

    def test_single(self):
        self.assertEqual(main.parse_variable("x"), "x")

    def test_multi(self):
        self.assertEqual(main.parse_variable("xyz"), "xyz")

    def test_digit(self):
        self.assertEqual(main.parse_variable("f012"), "f012")

    def test_starts_with_digit(self):
        self.assertEqual(main.parse_variable("0xyz"), "")

    def test_starts_with_symbol(self):
        self.assertEqual(main.parse_variable("@x"), "")

    def test_starts_with_space(self):
        self.assertEqual(main.parse_variable(" x"), "")


if __name__ == '__main__':
    # write your code here
    unittest.main()
