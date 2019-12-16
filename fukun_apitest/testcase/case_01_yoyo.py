#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: fky
@site:
@software: PyCharm
@file: case_01.py
@time: 2018/3/16 10:58
"""
import unittest
import requests
from ddt import ddt,data,unpack
from common.sendRequests import SendRequests
from common.readExcel import ReadExcel
import os

#获取测试数据所在的目录
path = os.path.dirname(os.getcwd())+"\\data\\qq_apiTest.xlsx"

testData = ReadExcel.readExcel(path,"Sheet1")
@ddt
class Test1(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()

    def tearDown(self):
        pass

    @data(*testData)
    def test_yoyo_api(self,data):

        re = SendRequests().sendRequests(self.s, data)
        #print(re.json())

        #切割字符串取后面的部分
        expect_result1 = data["expect_result"].split(":")[1]
        #转换为字符串
        expect_result = eval(expect_result1)
        #断言
        self.assertEqual(re.json()["origin"], expect_result, "返回错误,实际结果是%s"%re.json()["origin"])


if __name__ == '__main__':
    unittest.main()
