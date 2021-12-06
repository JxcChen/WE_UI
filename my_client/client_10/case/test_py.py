import os
import platform
import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

# 导入utils包
# from my_client.client_10.public.utils import *

operation = platform.system()
if operation == 'Windows':
    file_path = str(__file__).split("\\")[-3]
else:
    file_path = str(__file__).split("/")[-3]


try:
    from public.utils import *
except:
    exec("from my_client.%s.public.utils import *" % file_path)


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass

    def setUp(self):
        util_get_index_page(self, host)

    def test_01(self):
        '这里是用例描述'
        search_input = (By.ID,"kw")
        self.driver.find_element(*search_input).send_keys("hello world")

    def test_02(self):
        '这里是用例描述'
        search_input = (By.ID,"kw")
        self.driver.find_element(*search_input).send_keys("自动化")


if __name__ == '__main__':
    # 获取第一个系统参数
    param = {}
    try:
        host = sys.argv[1]
        script_name = sys.argv[2]
        case_name = sys.argv[3]
        param["script_name"] = script_name
        param["case_name"] = case_name
        util_run_with_report(Test, param)
    except:
        util_run_with_report(Test, param)


