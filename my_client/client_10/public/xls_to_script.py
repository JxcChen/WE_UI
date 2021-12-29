import time

import xlrd
import os
import unittest
import platform
import sys

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

operation = platform.system()
if operation == 'Windows':
    file_path = str(__file__).split("\\")[-3]
else:
    file_path = str(__file__).split("/")[-3]

try:
    from public.utils import *
    from public.auto_get_element import auto_get_element
except Exception as e:
    exec("from my_client.%s.public.utils import *" % file_path)
    exec("from my_client.%s.public.auto_get_element import *" % file_path)


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        util_get_index_page(self, host)

    def tearDown(self, method_name):
        if env == 'local':
            picture_name = "../report/picture/%s-%s.png" % (case_name, method_name)
        else:
            picture_name = "uiApp/static/res_picture/%s-%s.png" % (case_name, method_name)
        self.driver.get_screenshot_as_file(picture_name)

    def begin_test(self, case_date):
        '这里是用例描述'
        # 获取用例步骤 遍历判断
        steps = case_date['case_steps']
        assert_content = {}
        for step in steps:
            action = step['action']
            content = step['content']
            variable = step['variable']

            res = util_get_locator(self, step['locator'])
            locator = ()
            element = ''

            if res is not None:
                locator = res['locator']
                index = res['index']
                if 'assert_exist' in action or '断言相等' in action:
                    is_exist = True
                    try:
                        self.driver.find_elements(*locator)[index]
                    except:
                        is_exist = False
                    self.assertTrue(is_exist)
                    continue
                try:
                    element = self.driver.find_elements(*locator)[index]
                except Exception as e:
                    element = auto_get_element(self.driver, res)

            if 'send_key' == action or '输入' == action:
                element.send_keys(content)
            elif 'click' in action or '点击' in action:
                element.click()
            elif 'get_text' in action or '获取文本' in action:
                assert_content[variable] = element.get_attribute('innerText')
            elif 'get_attr' in action or '获取属性' in action:
                assert_content[variable] = element.get_attribute(content)
            elif 'assert_contains' in action or '断言包含' in action:
                print('进行断言')
                assert_list = str(content).split(',')
                self.assertIn(assert_list[0], assert_content[assert_list[1]])
            elif 'assert_equal' in action or '断言相等' in action:
                print('进行断言')
                assert_list = str(content).split(',')
                self.assertEqual(assert_list[0], assert_content[assert_list[1]])
            elif 'sleep' == action or '等待' == action:
                time.sleep(content)


def to_demo(case_date):
    # 调入测试数据 执行用例
    def demo(self):
        Test.begin_test(self, case_date)

    setattr(demo, '__doc__', str(case_date['case_name'] + ':' + case_date['case_des']))
    return demo


def to_test(excel_data):
    """
    将读取到的excel内容 转换成测试用例
    """
    # 遍历表格内容
    for i in range(len(excel_data)):
        # 动态生成用例
        setattr(Test, 'test_%s' % str(i + 1), to_demo(excel_data[i]))


def read_excel(file_name):
    file = os.path.dirname(os.path.dirname(__file__)) + "/case/%s" % file_name
    # 打开excel表格
    excel_file = xlrd.open_workbook_xls(filename=file)
    # 获取到对应的sheet
    sheet = excel_file.sheet_by_index(0)
    # 声明变量储存excel中的内容  datas格式：[{},{}....]
    datas = []
    # 获取行总行数
    rows = sheet.nrows
    case_content = {}
    # 遍历表格获取内容
    for i in range(0, rows):
        if 'case' == sheet.cell_value(i, 0):
            case_content = {'case_name': sheet.cell_value(i, 1), 'case_des': sheet.cell_value(i, 2),
                            'case_steps': []}
            datas.append(case_content)
        else:
            # 具体步骤
            step_tmp = {'step': sheet.cell_value(i, 0), 'locator': sheet.cell_value(i, 3),
                        'action': sheet.cell_value(i, 1), 'content': sheet.cell_value(i, 2),
                        'variable': sheet.cell_value(i, 4)}
            case_content['case_steps'].append(step_tmp)

    return datas


if __name__ == '__main__':
    data = read_excel('关键字驱动.xls')
    to_test(data)

    param = {}
    try:
        # 获取第二个系统参数
        host = sys.argv[1]
        script_name = sys.argv[2]
        case_name = sys.argv[3]
        env = "online"
    except:
        # ====================== 本地调试需要手动输入以下内容 ======================
        # ======================       host:调试地址      ======================
        # ====================== script_name:当前脚本文件名称 ====================
        # ======================    case_name:用例名称  =========================
        host = "https://www.baidu.com"
        script_name = "test_py.py"
        case_name = "本地调试"
        env = "local"
    param["script_name"] = script_name
    param["case_name"] = case_name
    param["env"] = env
    # unittest.main()
    util_run_with_report(self=Test, param=param)
