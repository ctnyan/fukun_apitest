# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: fky
@site:
@software: PyCharm
@file: sendRequests.py
@time: 2018/3/24 11:40
"""
from common.readExcel import ReadExcel
import requests
import json

class SendRequests():

    def sendRequests(self,s,apiData):
        '''
        从读取的表格中获取响应的参数作为传递
        '''
        # try:
        #     method = apiData["method"]
        #     url = apiData["url"]
        #     if apiData["params"] == "":
        #         par = None
        #     else:
        #         par = eval(apiData["params"])
        #
        #     if apiData["headers"] == "":
        #         h = None
        #     else:
        #         h = apiData["headers"]
        #
        #     if apiData["body"] == "":
        #         body_data = None
        #     else:
        #         body_data = eval(apiData["body"])
        #
        #     type = apiData["type"]
        #     v = False
        #     if type == "json":
        #         body = json.dumps(body_data)
        #     if type == "data":
        #         body = body_data
        #     else:
        #         body = body_data
        #
        #     #发送请求
        #     re = s.request(method=method,url=url,headers=h,params=par,data=body,verify=v)
        #     return re
        #
        # except Exception as e:
        #     print(e)

        method = apiData["method"]
        url = apiData["url"]
        if apiData["params"] == "":
            par = None
        else:
            par = eval(apiData["params"])

        if apiData["headers"] == "":
            h = None
        else:
            h = eval(apiData["headers"])

        if apiData["body"] == "":
            body_data = None
        else:
            body_data = eval(apiData["body"])

        ytype = apiData["ytype"]
        v = False
        if ytype == "json":
            body = json.dumps(body_data)
        if ytype == "data":
            body = body_data
        else:
            body = body_data

        #发送请求
        re = s.request(method=method,url=url,headers=h,params=par,data=body,verify=v)
        return re

if __name__ == '__main__':
    s = requests.session()
    testData = ReadExcel.readExcel("E:\\有棵树测试项目\\yan_个人项目集合\\fukun_apitest\\data\\arm_apiTest.xlsx","Sheet1")
    response = SendRequests().sendRequests(s,testData[0])
    print(response)