# coding=utf-8
#import HTMLTestRunner
#from util.htmltestrunner.HTMLTestRunner import HTMLTestRunner
from util.HTMLTestRunner_PY3.HTMLTestRunner_PY3 import HTMLTestRunner
import sys
import time

sys.path.append('D:/pythonWork/autoTest')
from case.login_keyword_cases import LoginKeywordCases
import ddt
import unittest
import os
from business.examination_place_business import ExaminationPlaceBusiness
from business.examination_room_business import ExaminationRoomBusiness
from util.excel_util import ExcelUtil
from util.table_util import TableUtil


class ExaminationRoomBasicSelectDdtCase(unittest.TestCase):
    # 所有case执行之前的装饰器---前置条件
    @classmethod
    def setUpClass(cls):
        print('所有case执行的前置条件')
        lkc = LoginKeywordCases()
        lkc.run_keyword_excel_cases()
        cls.driver = getattr(getattr(lkc, 'lk'), 'driver')
        cls.driver.maximize_window()
        cls.EPb = ExaminationPlaceBusiness(cls.driver)
        cls.enable_num = cls.EPb.get_enable_num()
        cls.Tu = TableUtil(cls.driver)
        cls.ERb = ExaminationRoomBusiness(cls.driver)
        cls.EPh = getattr(cls.EPb, 'Eh')
        cls.driver.refresh()
        cls.EPh.click_detailed_btn()
        time.sleep(1)

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
        self.driver.refresh()

    # 判断页面元素是否完整
    def test_examination_room_basic_select_a(self):
        page_complete = self.ERb.judge_page_complete()
        self.assertTrue(page_complete, "页面元素不完整，该用例执行失败")

    # 判断启用考点数量是否准确
    def test_examination_room_basic_select_b(self):
        self.ERh = getattr(self.ERb, 'ERh')
        place_num = int(self.ERh.get_place_num_text())
        if place_num == self.enable_num:
            result = True
        else:
            result = False
        self.assertTrue(result, "当前所有启用的考点数量不准确，该用例执行失败")

    # 判断选择考点功能页面元素是否完整
    def test_examination_room_basic_select_c(self):
        result = self.ERb.select_function_complete()
        self.assertTrue(result, "当前选择考点功能元素不完善，该用例执行失败")

    # 判断是否可直接选择“选择框”中的考点信息项
    def test_examination_room_basic_select_d(self):
        result = self.ERb.judge_direct_select_place()
        self.assertTrue(result, "不可直接选择“选择框”中的考点信息项，该用例执行失败")

    # 判断是否可输入考点名称搜索框，支持模糊搜索
    def test_examination_room_basic_select_e(self):
        result = self.ERb.judge_direct_send_place()
        self.assertTrue(result, "不可以在考点名称搜索框进行模糊搜索，该用例执行失败")




if __name__ == "__main__":
    # 报告存放路径
    # fire_path = os.path.join(os.path.pardir + "/report/" + "login_ddt_case.html")
    fire_path = r"D:\pythonWork\autoTest\report\examination_room_basic_select.html"
    f = open(fire_path, 'wb')

    # 添加测试用例
    suite = unittest.TestLoader().loadTestsFromTestCase(ExaminationRoomBasicSelectDdtCase)

    # 测试结果以报告显示
    #runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='this is the first ddt report', description=u'这是我们登录模块数据驱动测试报告',verbosity=2)
    runner = HTMLTestRunner(stream=f, title='考场管理测试报告', description='选择功能测试用例执行结果如下： ')
    #run = HTMLTestRunner()
    runner.run(suite)
