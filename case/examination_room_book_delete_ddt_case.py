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
#import HTMLTestRunner
from util.htmltestrunner.HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from business.examination_room_business import ExaminationRoomBusiness
from util.excel_util import ExcelUtil


class ExaminationRoomBookDeleteDdtCase(unittest.TestCase):
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
        cls.book_table_num = cls.ERh.get_book_table_empty_text()

    # 所有case执行之后的后置条件
    @classmethod
    def tearDownClass(cls):
        print('所有case执行的后置条件')
        cls.driver.close()

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
        # self.driver.refresh()

    # 执行用例，并判断是否执行成功
    def test_examination_room_delete_case(self):
        if self.book_table_num!='暂无数据':
            delete_error = self.ERb.delete_examination_room_book()
            self.assertTrue(delete_error, "删除考点用例成功，该用例执行失败")
        else:
            print('无数据删除，此用例不执行')


if __name__ == "__main__":
    # 报告存放路径
    # fire_path = os.path.join(os.path.pardir + "/report/" + "login_ddt_case.html")
    fire_path = r"D:\pythonWork\autoTest\report\examination_room_book_delete.html"
    f = open(fire_path, 'wb')

    # 添加测试用例
    suite = unittest.TestLoader().loadTestsFromTestCase(ExaminationRoomBookDeleteDdtCase)

    # 测试结果以报告显示
    #runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='this is the first ddt report',description=u'这是我们登录模块数据驱动测试报告',verbosity=2)
    runner = HTMLTestRunner(stream=f, title='考场管理测试报告', description='考点基本信息通讯录删除测试用例执行结果如下： ')
    run = HTMLTestRunner()
    runner.run(suite)
