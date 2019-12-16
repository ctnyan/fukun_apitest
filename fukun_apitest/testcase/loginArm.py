#! /usr/bin/env python
# -*- coding:utf-8 -*-

import unittest

import requests
from ddt import ddt,data,unpack
from common.sendRequests import SendRequests
from common.readExcel import ReadExcel
import os

path = os.path.dirname(os.getcwd())+"\\data\\arm_apiTest.xlsx"
testData = ReadExcel.readExcel(path,"Sheet1")
# testData = testData_o[0]
# print(testData)

@ddt
class Test1(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()

    def tearDown(self):
        pass

    @data(*testData)
    def test_loginarm_api(self,data):
        re = SendRequests().sendRequests(self.s, data)
        print(re.json()["state"])

        #切割字符串取后面的部分
        expect_result1 = data["expect_result"].split(":")[1]
        #转换为字符串
        expect_result = eval(expect_result1)
        #断言
        self.assertEqual(re.json()["state"], expect_result, "返回错误,实际结果是%s"%re.json()["state"])


if __name__ == '__main__':
    unittest.main()