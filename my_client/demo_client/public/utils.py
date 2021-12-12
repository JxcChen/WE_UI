import os
import platform
import unittest
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

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


def util_get_element(self, loc):
    """
    查找元素方法
    :param self: 携带driver的测试类
    :param loc: 定位符  type:元祖
    :return: 目标元素
    """
    try:
        element = self.driver.find_element(*loc)
    except Exception as e:
        raise e
    return element


def util_switch_frame(self, frame):
    """
    切换iframe
    :param self:
    :param frame: frame的id或name  也可以是整个frame元素
    :return:
    """
    self.driver.switch_to.frame(frame)


def util_element_is_exist(self, *args):
    """
    使用不同的定位方式查看元素在页面是否存在
    :param self: 携带driver的测试类
    :param args: 元素定位列表
    :return: 是否存在  type：boolean
    """
    for loc in args:
        id_len = len(self.driver.find_elements(by=By.Id, value=loc))
        xpath_len = len(self.driver.find_elements(by=By.XPATH, value=loc))
        cs_len = len(self.driver.find_elements(by=By.CSS_SELECTOR, value=loc))
        class_len = len(self.driver.find_elements(by=By.CLASS_NAME, value=loc))
        if id_len + xpath_len + cs_len + class_len == 0:
            return False
    return True
