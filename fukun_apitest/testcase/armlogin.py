#! /usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json
from common.readExcel import ReadExcel

class Armlogin():
    data_login = {"userName": "yanfukun", "pwd": "yYKS1234"}

    def login(self):
        url = "http://10.90.1.204:8000/urc/motan/service/api/IUrcService/login"
        headers = {"Content-Type": "application/x-www-form-urlencoded",
                   "paramType": "2",
                   "group": "rpc-service-group-test",
                   "prefix": "com.yks",
                   "version": "1.0"
                   }
        re = requests.session().request(url=url, method='post', headers=headers, data=self.data_login)
        json_data = re.json()
        ticket = json_data["data"]["ticket"]
        userName = json_data["data"]["userName"]
        return ticket,userName

    def funVersion(self):
        url1 = "http://10.90.1.204:8000/urc/motan/service/api/IUrcService/getAllFuncPermit"
        headers1 = {"Content-Type": "application/json",
                    "paramType": "1",
                    "group": "rpc-service-group-test",
                    "prefix": "com.yks",
                    "version": "1.0"
                    }
        ticket,userName = self.login()
        data_funVersion = {"operator": userName, "ticket": ticket}
        data = json.dumps(data_funVersion)
        re1 = requests.session().request(url=url1, method='post', headers=headers1, data=data)
        json_data = re1.json()
        funVersion = json_data["data"]["funcVersion"]
        return funVersion

    def readExcel_new(self):
        testData = ReadExcel.readExcel("E:\\有课树测试项目\\yan_个人项目集合\\fukun_apitest\\data\\arm_apiTest.xlsx", "Sheet1")
        print(testData)
        st1 = testData[0]["body"]
        st = eval(st1)
        keys = st.keys()
        ticket,userName = Armlogin().login()
        funVersion = rt.funVersion()

        for key in keys:
            if st[key] == "${operator}":
                st[key] = userName

            if st[key] == "${ticket}":
                st[key] = ticket

            if st[key] == "${funVersion}":
                st[key] = funVersion
        return st



if __name__ == "__main__":

    rt = Armlogin()
    data =rt.readExcel_new()
    print(data)


