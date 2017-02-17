#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'A group of testcases in a class'
__author__ = 'zhangjingjun'
__mtime__ = '2017/2/16'
# ----------Dragon be here!----------
              ┏━┓      ┏━┓
            ┏━┛ ┻━━━━━━┛ ┻━━┓
            ┃       ━       ┃
            ┃  ━┳━┛   ┗━┳━  ┃
            ┃       ┻       ┃
            ┗━━━┓      ┏━━━━┛
                ┃      ┃神兽保佑
                ┃      ┃永无BUG！
                ┃      ┗━━━━━━━━━┓
                ┃                ┣━┓
                ┃                ┏━┛
                ┗━━┓ ┓ ┏━━━┳━┓ ┏━┛
                   ┃ ┫ ┫   ┃ ┫ ┫
                   ┗━┻━┛   ┗━┻━┛
"""
import pytest

class TestClass():
	def test_one(self):
		x = "this"
		assert 'h' in x

	def test_two(self):
		x = "hello"
		assert hasattr(x,'check')

if __name__ == '__main__':
	pytest.main('test_class.py')