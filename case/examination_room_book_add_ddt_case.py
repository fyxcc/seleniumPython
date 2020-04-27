# coding=utf-8
import sys
import time

from business.examination_place_business import ExaminationPlaceBusiness

sys.path.append('D:/pythonWork/autoTest')
from time import sleep
from case.login_keyword_cases import LoginKeywordCases
import ddt
import unittest
import os
import HTMLTestRunner
from selenium import webdriver
from business.examination_room_business import ExaminationRoomBusiness
from util.excel_util import ExcelUtil

# 获取数据
ex = ExcelUtil(excel_path=r"D:\pythonWork\autoTest\data\examinationRoomBookAddDdtData.xls")
data = ex.get_data()


# 测试类前加修饰@ddt.ddt
@ddt.ddt
# 姓名，性别，职位，手机，固定电话，邮寄地址，电子邮箱，qq
class ExaminationPlaceAddDdtCase(unittest.TestCase):
    # 所有case执行之前的装饰器---前置条件
    @classmethod
    def setUpClass(cls):
        print('所有case执行的前置条件')
        lkc = LoginKeywordCases()
        lkc.run_keyword_excel_cases()
        cls.driver = getattr(getattr(lkc, 'lk'), 'driver')
        cls.driver.maximize_window()
        cls.ERb = ExaminationRoomBusiness(cls.driver)
        cls.ERh = getattr(cls.ERb, 'ERh')
        cls.ERp = getattr(cls.ERh, 'ERp')
        cls.EPb = ExaminationPlaceBusiness(cls.driver)
        cls.EPh = getattr(cls.EPb, 'Eh')
        cls.EPh.click_detailed_btn()
        time.sleep(1)
        cls.ERh.click_book_add_btn()

    # 所有case执行之后的后置条件
    @classmethod
    def tearDownClass(cls):
        print('所有case执行的后置条件')
        # cls.driver.close()

    # 每一条case执行之前的前置条件
    def setUp(self):
        # print('每一条case执行前的前置条件')
        pass

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
        if self.ERh.judge_book_add_frame():
            self.ERb.clear_book_all_add()


    #判断添加通讯录字段是否完整
    def test_examination_room_book_add_a(self):
        result = self.ERb.judge_add_book_complete()
        self.assertTrue(result, "添加交通信息字段不完整，该用例执行失败")
    # case前加修饰 @ ddt.data()
    @ddt.data(*data)
    # 执行用例，并判断是否执行成功
    def test_examination_room_book_add_b(self, data):
        book_add_name, book_add_phone, book_add_tel, book_add_post_address, book_add_mail,book_add_qq,assertCode,assertText = data
        add_error = self.ERb.book_add_function(book_add_name, book_add_phone, book_add_tel, book_add_post_address, book_add_mail,book_add_qq,
                                         assertCode, assertText)
        if len(assertCode) != 0 and assertText != '添加成功':
            self.assertTrue(add_error, "添加考点成功，该用例执行失败")
        elif assertText == '添加失败!':
            self.assertTrue(add_error, "输入重复考点编号，添加成功，该用例执行失败")
        else:
            self.assertTrue(add_error, "添加考点失败，该用例执行失败")


if __name__ == "__main__":
    # 报告存放路径
    # fire_path = os.path.join(os.path.pardir + "/report/" + "login_ddt_case.html")
    fire_path = r"D:\pythonWork\autoTest\report\examination_room_book_add.html"
    f = open(fire_path, 'wb')

    # 添加测试用例
    suite = unittest.TestLoader().loadTestsFromTestCase(ExaminationPlaceAddDdtCase)

    # 测试结果以报告显示
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='this is the first ddt report',
                                           description=u'这是我们登录模块数据驱动测试报告',
                                           verbosity=2)
    runner.run(suite)
