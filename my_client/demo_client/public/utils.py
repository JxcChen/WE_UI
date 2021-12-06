import os
import platform
import unittest
from selenium import webdriver

operation = platform.system()

try:
    from public.HTMLTestRunner import HTMLTestRunner
except:
    if operation == 'Windows':
        file_path = str(__file__).split("\\")[-3]
    else:
        file_path = str(__file__).split("/")[-3]
    exec('from my_client.%s.public.HTMLTestRunner import HTMLTestRunner' % file_path)


# 获取测试首页
def util_get_index_page(self, host):
    self.driver.get(host)


# 启动测试并获取报告
def util_run_with_report(self, param: dict):
    base_path = os.path.dirname(os.path.dirname(__file__))
    case_name = param['case_name']
    if operation == 'Windows':
        file_path = base_path + "\\report\\" + case_name + '.html'
    else:
        file_path = base_path + "/report/" + case_name + '.html'

    with open(file_path, 'wb') as f:
        runner = HTMLTestRunner(f, title=case_name + "测试报告",
                                description="用例名称：" + case_name + " 脚本名称：" + param['script_name'])
        runner.run(unittest.makeSuite(self))
