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
ex = ExcelUtil(excel_path=r"D:\pythonWork\autoTest\data\examinationRoomBasicInfoEditDdtData.xls")
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
        cls.ERp=getattr(  cls.ERh,'ERp')
        cls.EPb = ExaminationPlaceBusiness(cls.driver)
        cls.EPh = getattr(cls.EPb,'Eh')
        cls.EPh.click_detailed_btn()
        time.sleep(1)
        cls.ERh.click_basic_edit_btn()

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
        if self.ERp.get_basic_code()==None:
            self.ERb.clear_basic_all_edit()
    # 判断编辑考点总机位数、可编排机位数、考场数三字段是否不可编辑
    def test_examination_room_basic_info_edit_a(self):
        result = self.ERb.judge_filed_status()
        self.assertTrue(result, "编辑考点不可编辑字段有误，该用例执行失败")
    # 判断考点性质取字典值是否完整
    def test_examination_room_basic_info_edit_b(self):
        result = self.ERb.judge_place_character_complete()
        self.assertTrue(result, "考点性质取字典值不完整，该用例执行失败")
    # case前加修饰 @ ddt.data()
    @ddt.data(*data)
    #  执行用例，并判断是否执行成功
    def test_examination_room_basic_info_edit_c(self,data):
        basic_edit_code,basic_edit_name,basic_edit_time,basic_edit_duration,basic_edit_post_code,basic_edit_place_person,basic_edit_person_tel,assertCode, assertText=data
        edit_error = self.ERb.edit_function(basic_edit_code, basic_edit_name,basic_edit_time, basic_edit_duration, basic_edit_post_code, basic_edit_place_person,
                                           basic_edit_person_tel,assertCode, assertText)
        if len(assertCode) != 0:
            self.assertTrue(edit_error, "该用例执行失败")
        else:
            self.assertTrue(edit_error, "添加失败，该用例执行失败")
        #self.assertTrue(result, "编辑考点不可编辑字段有误，该用例执行失败")

if __name__ == "__main__":
    # 报告存放路径
    # fire_path = os.path.join(os.path.pardir + "/report/" + "login_ddt_case.html")
    fire_path = r"D:\pythonWork\autoTest\report\examination_room_basic_info_edit.html"
    f = open(fire_path, 'wb')

    # 添加测试用例
    suite = unittest.TestLoader().loadTestsFromTestCase(ExaminationRoomBasicInfoEditDdtCase)

    # 测试结果以报告显示
    #runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='this is the first ddt report',description=u'这是我们登录模块数据驱动测试报告', verbosity=2)
    runner = HTMLTestRunner(stream=f, title='考场管理测试报告', description='考点基本资料编辑测试用例执行结果如下：')
    runner.run(suite)
