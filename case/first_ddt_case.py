# coding=utf-8
import ddt
import unittest
import time
import os
import HTMLTestRunner
from selenium import webdriver
from business.register_business import RegisterBusiness
from util.excel_util import ExcelUtil

# 获取数据
ex = ExcelUtil()
data = ex.get_data()
@ddt.ddt
# 邮箱，用户名，密码，验证码，错误信息定位元素，错误提示信息
class FirstDdtCase(unittest.TestCase):
    # 所有case执行之前的装饰器---前置条件
    '''
    @classmethod
    def setUpClass(cls):
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
        print('所有case执行的后置条件')
    '''

    # 每一条case执行之前的前置条件
    def setUp(self):
        self.register_url = 'http://www.5itest.cn/register'
        self.driver = webdriver.Chrome()
        self.driver.get(self.register_url)
        self.driver.maximize_window()
        self.rb = RegisterBusiness(self.driver)
        #self.file_name = os.path.join(os.path.pardir + "/Image/" + "test_captcha.png")
        # print('每一条case执行前的前置条件')

    # 每一条case执行之后的后置条件
    def tearDown(self):
        # print('每一条case执行之后的后置条件')
        time.sleep(2)
        # case执行失败进行截图
        for method_name, error in self._outcome.errors:
            if error:
                # 获取当前执行的case名字
                case_name = self._testMethodName
                # 设置失败截图存储路径
                file_path = os.path.join(os.path.pardir + "/report/" + case_name + ".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()
    '''
    @ddt.data(
        ['test01', 'test01', 'test01abc', self.file_name,
         'register_email_error', '请输入有效的电子邮件地址'],
        ['test02@163.com', '', 'test02abc', self.file_name,
         'register_nickname_error', '字符长度必须大于等于4，一个中文字算2个字符']

    )
    @ddt.unpack
    '''

    @ddt.data(*data)
    # 邮箱错误用例，判断用例是否执行成功
    def test_register_case(self, data):
        email, username, password, file_name, assertCode, assertText=data
        register_email_error = self.rb.register_function(email, username, password, file_name, assertCode,assertText)
        self.assertTrue(register_email_error, "账号注册成功，该用例执行失败")


if __name__ == "__main__":
    # 报告存放路径
    fire_path = os.path.join(os.path.pardir + "/report/" + "first_ddt_case.html")
    f = open(fire_path, 'wb')

    # 添加测试用例
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)

    # 测试结果以报告显示
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='this is the first ddt report',
                                           description=u'这是我们第一次ddt测试报告',
                                           verbosity=2)
    runner.run(suite)
    unittest.main()
