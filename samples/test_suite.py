#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# create time: 17-10-10
import unittest

from samples.test_mathfunc import TestMathFunc
from samples.HTMLTestRunner_PY3 import HTMLTestRunner
from samples.HTMLTestRunner import HTMLTestRunner as HTMLRunner

__author__ = 'Devin -- http://zhangchuzhao.site'


if __name__ == '__main__':

    # 测试套件1
    suite = unittest.TestSuite()
    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide"), TestMathFunc("test_milti")]  # TestCase run orderly
    suite.addTests(tests)  # 添加多个TestCase
    # suite.addTest(TestMathFunc("test_milti"))  # 添加单个TestCase
    runner = unittest.TextTestRunner(verbosity=0)
    runner.run(suite)

    # 测试套件2
    # loadTestsFromName()传入格式：模块名.TestCase类
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['test_mathfunc.TestMathFunc']))  # 添加多个TestCase类，TestLoader中TestCase顺序运行
    # suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc.TestMathFunc'))  # 添加一个TestCase类
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)

    # 测试套件3
    # loadTestsFromTestCase()传入格式：TestCase类
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    # 测试报告1
    # 执行结果输出至命令行
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    # 测试报告2
    # 执行结果输出至文件
    with open('UnittestTextReport.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)

    # 测试报告3
    # 执行结果输出至HTML报告(样式1）
    with open('HTMLReport.html', 'wb') as f:
        runner = HTMLRunner(stream=f, title='My unit test', description='This report output by HTMLTestRunner', verbosity=2)
        runner.run(suite)

    # 测试报告4
    # 执行结果输出为HTML报告（样式2）
    with open('HTMLReport2.html', 'wb') as f:
        runner = HTMLTestRunner(stream=f, title='MathFunc测试报告', description='generated by HTMLTestRunner', verbosity=2)
        runner.run(suite)
