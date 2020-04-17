# coding=utf-8
import sys

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

sys.path.append('D:/pythonWork/autoTest')
from time import sleep
from case.login_keyword_cases import LoginKeywordCases
import ddt
import unittest
import os
import HTMLTestRunner
from business.examination_place_business import ExaminationPlaceBusiness
from util.excel_util import ExcelUtil
from util.table_util import TableUtil

# 获取数据
ex = ExcelUtil(excel_path=r"D:\pythonWork\autoTest\data\examinationPlaceEditDdtData.xls")
data = ex.get_data()


# 测试类前加修饰@ddt.ddt
@ddt.ddt
# 考点编号，考点名称，考点地址，考点负责人，负责人联系电话
class ExaminationPlaceQueryDdtCase(unittest.TestCase):
    # 所有case执行之前的装饰器---前置条件
    @classmethod
    def setUpClass(cls):
        print('所有case执行的前置条件')
        lkc = LoginKeywordCases()
        lkc.run_keyword_excel_cases()
        cls.driver = getattr(getattr(lkc, 'lk'), 'driver')
        cls.driver.maximize_window()
        cls.Eb = ExaminationPlaceBusiness(cls.driver)
        cls.Tu = TableUtil(cls.driver)

    # 所有case执行之后的后置条件
    @classmethod
    def tearDownClass(cls):
        print('所有case执行的后置条件')

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

    # 判断页面元素是否完整
    def test_examination_place_query_a(self):
        page_complete = self.Eb.judge_page_complete()
        self.assertTrue(page_complete, "页面元素不完整，该用例执行失败")

    # 行政区划一级查询
    def test_examination_place_query_b(self):
        self.Eb.judge_query_place_division_code('fchild')
        result=self.Eb.judge_query_result()
        self.assertTrue(result, "页面元素不完整，该用例执行失败")

    # case前加修饰 @ ddt.data()


if __name__ == "__main__":
    # 报告存放路径
    # fire_path = os.path.join(os.path.pardir + "/report/" + "login_ddt_case.html")
    fire_path = r"D:\pythonWork\autoTest\report\examination_place_edit.html"
    f = open(fire_path, 'wb')

    # 添加测试用例
    suite = unittest.TestLoader().loadTestsFromTestCase(ExaminationPlaceQueryDdtCase)

    # 测试结果以报告显示
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='this is the first ddt report',
                                           description=u'这是我们登录模块数据驱动测试报告',
                                           verbosity=2)
    runner.run(suite)
