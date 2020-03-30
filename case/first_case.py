#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys

sys.path.append('D:/pythonWork/autoTest')
import time
from business.register_business import RegisterBusiness
from selenium import webdriver
from log.user_log import UserLog
import unittest
import HTMLTestRunner
import os


class FirstCase(unittest.TestCase):

    # 所有case执行之前的装饰器---前置条件
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        cls.register_url = 'http://www.5itest.cn/register'
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.register_url)
        cls.driver.maximize_window()
        cls.rb = RegisterBusiness(cls.driver)
        cls.file_name = os.path.join(os.path.pardir + "/Image/" + "test_captcha.png")
        print('所有case执行的前置条件')

    # 所有case执行之后的后置条件
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.log.close_handle()
        print('所有case执行的后置条件')

    # 每一条case执行之前的前置条件
    def setUp(self):
        print('每一条case执行前的前置条件')
        self.logger.info('this is chrome')

    # 每一条case执行之后的后置条件
    def tearDown(self):
        print('每一条case执行之后的后置条件')
        time.sleep(2)
        # case执行失败进行截图
        for method_name, error in self._outcome.errors:
            if error:
                # 获取当前执行的case名字
                case_name = self._testMethodName
                # 设置失败截图存储路径
                file_path = os.path.join(os.path.pardir + "/report/" + case_name + ".png")
                self.driver.save_screenshot(file_path)

    # 邮箱错误用例，判断用例是否执行成功
    def test_register_email_error(self):
        register_email_error = self.rb.register_email_error('test01', 'test01', 'test01abc', self.file_name)
        # self.assertFalse(register_email_error, "账号注册失败，该用例执行成功")
        self.assertTrue(register_email_error, "账号注册成功，该用例执行失败")
        # if register_email_error is True:
        # print("账号注册失败，该用例执行成功")
        # else:
        # print("账号注册成功，该用例执行失败")

    # 用户名错误用例，判断用例是否执行成功
    def test_register_nickname_error(self):
        register_nickname_error = self.rb.register_nickname_error('test02@163.com', '', 'test02abc', self.file_name)
        # self.assertFalse(register_nickname_error, "账号注册失败，该用例执行成功")
        self.assertTrue(register_nickname_error, "账号注册成功，该用例执行失败")

    # 密码错误用例，判断用例是否执行成功
    def test_register_password_error(self):
        register_password_error = self.rb.register_password_error('test03@163.com', 'test03', 'test03abc',
                                                                  self.file_name)
        # self.assertFalse(register_password_error, "账号注册失败，该用例执行成功")
        self.assertTrue(register_password_error, "账号注册成功，该用例执行失败")

    # @unittest.skip('不执行第一条')
    # 验证码错误用例，判断用例是否执行成功
    def test_captcha_code_error(self):
        captcha_code_error = self.rb.captcha_code_error('test04@163.com', 'test04', 'test04abc', self.file_name)
        # self.assertFalse(captcha_code_error, "账号注册失败，该用例执行成功")
        self.assertTrue(captcha_code_error, "账号注册成功，该用例执行失败")

    # 注册成功用例
    def test_login_success(self):
        success = self.rb.common_register('test03@163.com', 'test03', 'test03aaa', self.file_name)
        if self.rb.success_or_fail():
            print('注册成功，此条用例执行成功')


if __name__ == "__main__":
    # 报告存放路径
    # fire_path = os.path.join(os.path.pardir + "/report/" + "first_case.html")
    fire_path = r"D:\pythonWork\autoTest/report/first_case.html"
    f = open(fire_path, 'wb')

    # 把需要运行的case加载在容器中，达到选择性运行
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_register_email_error'))
    # suite.addTest(FirstCase('test_register_nickname_error'))
    # suite.addTest(FirstCase('test_register_password_error'))
    # suite.addTest(FirstCase('test_captcha_code_error'))

    # 测试结果以报告显示
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='this is the first report', description=u'这是我们第一次测试报告',
                                           verbosity=2)
    runner.run(suite)

    # 测试结果在控制台显示
    # unittest.TextTestRunner().run(suite)
    # 执行所有case
    # unittest.main()
