# -*-coding:utf-8-*-
from selenium import webdriver
import unittest
import os
import HTMLTestRunner
#用例存放路径
#case_path = os.path.join(os.getcwd(),"D:\\pyse\\baidu")
#报告存放路径
#report_path=os.path.join(os.getcwd(),"D:\\pyse\\report")
#遍历所有用例:
#discover=unittest.defaultTestLoader.discover(case_path,
#                                             pattern="test*.py",
#                                             top_level_dir=None)
#print discover
def all_case():
    # 用例存放路径
    case_path = os.path.join(os.getcwd(), "D:\\pyse\\baidu")
    # 报告存放路径
    #report_path = os.path.join(os.getcwd(), "D:\\pyse\\report\\report01.html")
    discover=unittest.defaultTestLoader.discover(
        case_path,
        pattern="test*.py",
        top_level_dir=None)
    print discover
    return discover
if __name__=="__main__":
    #runner=unittest.TextTestRunner()
    #runner.run(all_case())
    #report_abspath = os.path.join(report_path,"D:\\pyse\\report\\report01.html")
    report_path="D:\\pyse\\report\\report01.html"
    fp=open(report_path,"wb")
    runer=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'自动化测试报告，测试结果如下：',
        description=u'用例执行情况如下：'
    )
    runer.run(all_case())
    fp.close()

