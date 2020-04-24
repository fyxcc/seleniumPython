# coding=utf-8
import HTMLTestRunner
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

# 获取数据
ex = ExcelUtil(excel_path=r"D:\pythonWork\autoTest\data\examinationPlaceQueryDdtData.xls")
data = ex.get_data()

# 测试类前加修饰@ddt.ddt
@ddt.ddt
# 考点编号，考点名称，合同签订时间，合同签订时长，邮政编码，考点负责人，负责人联系电话
class ExaminationRoomBasicInfoEditDdtCase(unittest.TestCase):
    # 所有case执行之前的装饰器---前置条件
    @classmethod
    def setUpClass(cls):
        print('所有case执行的前置条件')
        lkc = LoginKeywordCases()
        lkc.run_keyword_excel_cases()
        cls.driver = getattr(getattr(lkc, 'lk'), 'driver')
        cls.driver.maximize_window()
        cls.Tu = TableUtil(cls.driver)
        cls.ERb=ExaminationRoomBusiness(cls.driver)
        cls.ERh=getattr(cls.ERb,'ERh')
        cls.EPb = ExaminationPlaceBusiness(cls.driver)
        cls.EPh = getattr(cls.EPb,'Eh')
        cls.driver.refresh()
        cls.EPh.click_detailed_btn()
        time.sleep(1)
        cls.ERh.click_basic_edit_btn()

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
        self.ERb.clear_basic_all_edit()
    # 判断编辑考点总机位数、可编排机位数、考场数三字段是否不可编辑
    def test_examination_room_basic_info_edit_a(self):
        result = self.ERb.judge_filed_status()
        self.assertTrue(result, "编辑考点不可编辑字段有误，该用例执行失败")
    #
if __name__ == "__main__":
    # 报告存放路径
    # fire_path = os.path.join(os.path.pardir + "/report/" + "login_ddt_case.html")
    fire_path = r"D:\pythonWork\autoTest\report\examination_room.html"
    f = open(fire_path, 'wb')

    # 添加测试用例
    suite = unittest.TestLoader().loadTestsFromTestCase(ExaminationRoomBasicInfoEditDdtCase)

    # 测试结果以报告显示
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='this is the first ddt report',
                                           description=u'这是我们登录模块数据驱动测试报告',
                                           verbosity=2)
    runner.run(suite)
