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

# 获取数据
ex = ExcelUtil(excel_path=r"D:\pythonWork\autoTest\data\examinationRoomTrafficInfoEditDdtData.xls")
data = ex.get_data()

# 测试类前加修饰@ddt.ddt
@ddt.ddt
# 考点地址，交通情况，具体线路，地理位置描述，经度，纬度
class ExaminationRoomTrafficInfoEditDdtCase(unittest.TestCase):
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
        cls.ERp=getattr(cls.ERh,'ERp')
        cls.EPb = ExaminationPlaceBusiness(cls.driver)
        cls.EPh = getattr(cls.EPb,'Eh')
        cls.EPh.click_detailed_btn()
        time.sleep(1)
        cls.ERh.click_traffic_edit_btn()

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
        time.sleep(2)
        if self.ERp.get_traffic_address()==None:
            self.ERb.clear_traffic_all_edit()
    # 判断编辑交通信息字段是否完整
    def test_examination_room_basic_info_edit_a(self):
        result = self.ERb.judge_edit_traffic_complete()
        self.assertTrue(result, "编辑交通信息字段不完整，该用例执行失败")
    # case前加修饰 @ ddt.data()
    @ddt.data(*data)
    #  执行用例，并判断是否执行成功
    def test_examination_room_basic_info_edit_c(self,data):
        traffic_edit_address,traffic_edit_condition,traffic_edit_concrete_route,traffic_edit_location,traffic_edit_longitude,traffic_edit_latitude,assertCode, assertText=data
        edit_error = self.ERb.traffic_edit_function(traffic_edit_address,traffic_edit_condition,traffic_edit_concrete_route,traffic_edit_location,traffic_edit_longitude,traffic_edit_latitude,assertCode, assertText)
        if len(assertCode) != 0:
            self.assertTrue(edit_error, "该用例执行失败")
        else:
            self.assertTrue(edit_error, "添加失败，该用例执行失败")
if __name__ == "__main__":
    # 报告存放路径
    # fire_path = os.path.join(os.path.pardir + "/report/" + "login_ddt_case.html")
    fire_path = r"D:\pythonWork\autoTest\report\examination_room_traffic_info_edit.html"
    f = open(fire_path, 'wb')

    # 添加测试用例
    suite = unittest.TestLoader().loadTestsFromTestCase(ExaminationRoomTrafficInfoEditDdtCase)

    # 测试结果以报告显示
    #runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='this is the first ddt report', description=u'这是我们登录模块数据驱动测试报告',verbosity=2)
    runner = HTMLTestRunner(stream=f, title='考场管理测试报告', description='考点基本信息交通路线编辑测试用例执行结果如下： ')
    runner.run(suite)
