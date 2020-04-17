# coding=utf-8
import sys

sys.path.append('D:/pythonWork/autoTest')
import ddt
import unittest
import time
import os
import HTMLTestRunner
from selenium import webdriver
from business.login_business import LoginBusiness
from util.excel_util import ExcelUtil


# 获取数据
ex = ExcelUtil(excel_path=r"D:\pythonWork\autoTest\data\loginDdtData.xls")
data = ex.get_data()


# 测试类前加修饰@ddt.ddt
@ddt.ddt
# 用户名，密码，验证码，错误信息定位元素，错误提示信息
class LoginDdtCase(unittest.TestCase):
    # 所有case执行之前的装饰器---前置条件

    @classmethod
    def setUpClass(cls):
        print('所有case执行的前置条件')
        cls.login_url = 'http://localhost:9090/exam-place/login'
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.login_url)
        cls.driver.maximize_window()
        cls.lb = LoginBusiness(cls.driver)

    # 所有case执行之后的后置条件
    @classmethod
    def tearDownClass(cls):
        print('所有case执行的后置条件')
        cls.driver.close()

    # 每一条case执行之前的前置条件
    def setUp(self):
        print('每一条case执行前的前置条件')
        # self.login_url = 'http://localhost:9090/exam-place/login'
        # self.driver = webdriver.Chrome()
        # self.driver.get(self.login_url)
        # self.driver.maximize_window()
        # self.lb = LoginBusiness(self.driver)

    # 每一条case执行之后的后置条件
    def tearDown(self):
        print('每一条case执行之后的后置条件')
        # case执行失败进行截图
        for method_name, error in self._outcome.errors:
            if error:
                # 获取当前执行的case名字
                case_name = self._testMethodName
                # 设置失败截图存储路径
                file_path = os.path.join(os.path.pardir + "/report/" + case_name + ".png")
                self.driver.save_screenshot(file_path)
        self.driver.refresh()
        # self.driver.close()

    # case前加修饰 @ ddt.data()
    @ddt.data(*data)
    # 执行用例，并判断是否执行成功
    def test_login_case(self, data):
        username, password, file_name, assertCode, assertText = data
        login_error = self.lb.login_function(username, password, file_name, assertCode, assertText)
        if len(assertCode) != 0:
            self.assertTrue(login_error, "账号登录成功，该用例执行失败")



if __name__ == "__main__":
    # 报告存放路径
    # fire_path = os.path.join(os.path.pardir + "/report/" + "login_ddt_case.html")
    fire_path = r"D:\pythonWork\autoTest/report/first_case.html"
    f = open(fire_path, 'wb')

    # 添加测试用例
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginDdtCase)

    # 测试结果以报告显示
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='this is the first ddt report',
                                           description=u'这是我们登录模块数据驱动测试报告',
                                           verbosity=2)
    runner.run(suite)
