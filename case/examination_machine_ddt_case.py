# coding=utf-8
#import HTMLTestRunner
from util.htmltestrunner.HTMLTestRunner import HTMLTestRunner
import sys
import time

from handle.examination_envir_handle import ExaminationeEnvirHandle

sys.path.append('D:/pythonWork/autoTest')
from case.login_keyword_cases import LoginKeywordCases
import ddt
import unittest
import os
from business.examination_place_business import ExaminationPlaceBusiness
from business.examination_room_business import ExaminationRoomBusiness
from business.examination_envir_business import ExaminationEnvirBusiness
from util.excel_util import ExcelUtil
from util.table_util import TableUtil


# 获取数据
ex = ExcelUtil(excel_path=r"D:\pythonWork\autoTest\data\examinationMachineDdtCase.xls")
data = ex.get_data()


# 测试类前加修饰@ddt.ddt
@ddt.ddt
class ExaminationMachineDdtCase(unittest.TestCase):
    # 所有case执行之前的装饰器---前置条件
    @classmethod
    def setUpClass(cls):
        print('所有case执行的前置条件')
        lkc = LoginKeywordCases()
        lkc.run_keyword_excel_cases()
        cls.driver = getattr(getattr(lkc, 'lk'), 'driver')
        cls.driver.maximize_window()
        cls.EPb = ExaminationPlaceBusiness(cls.driver)
        cls.Tu = TableUtil(cls.driver)
        cls.ERb = ExaminationRoomBusiness(cls.driver)
        cls.Eeb=ExaminationEnvirBusiness(cls.driver)
        cls.EPh = getattr(cls.EPb, 'Eh')
        cls.driver.refresh()
        cls.EPh.click_detailed_btn()
        cls.Eeh = ExaminationeEnvirHandle(cls.driver)
        cls.Eep=getattr(cls.Eeh, 'Eep')
        cls.Eeh.click_envir_btn()
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
        if self.Eep.get_machine_edit_storage()!=None:
            self.Eeb.clear_all_machine()

    #判断开关键是否默认为否
    def test_examination_machine_a(self):
        page_complete = self.Eeb.judge_machine_default_value()
        self.assertTrue(page_complete, "开关选项未默认未否，该用例执行失败")

    # case前加修饰 @ ddt.data()

    @ddt.data(*data)
   # 执行用例，并判断是否执行成功
    def test_examination_machine_g(self, data):
        machine_edit_available_examination, machine_edit_processor, machine_edit_storage,machine_edit_caliche,machine_edit_ups_model, machine_edit_ups_time,assertCode, assertText = data
        add_error = self.Eeb.machine_edit_function(machine_edit_available_examination, machine_edit_processor, machine_edit_storage,machine_edit_caliche,machine_edit_ups_model,machine_edit_ups_time,assertCode, assertText)
        if len(assertCode) != 0 and assertText != '添加成功':
            self.assertTrue(add_error, "添加考点成功，该用例执行失败")
        elif assertText == '添加失败!':
            self.assertTrue(add_error, "输入重复考点编号，添加成功，该用例执行失败")
        else:
            self.assertTrue(add_error, "添加考点失败，该用例执行失败")
    #判断机器设备编辑处理器内容完整性
    def test_examination_machine_b(self):
        page_complete1 = self.Eeb.judge_machine_processor_select()
        self.assertTrue(page_complete1, "机器设备编辑处理器内容不完整，该用例执行失败")
    #判断机器设备编辑网卡内容完整性
    def test_examination_machine_c(self):
        page_complete2 = self.Eeb.judge_internet_card_complete()
        self.assertTrue(page_complete2, "机器设备编辑网卡内容不完整，该用例执行失败")

    # 判断机器设备编辑操作系统内容完整性
    def test_examination_machine_e(self):
        page_complete3 = self.Eeb.judge_machine_operating_system_select()
        self.assertTrue(page_complete3, "机器设备编辑操作系统内容不完整，该用例执行失败")

    # 判断机器设备编辑网络带宽内容完整性
    def test_examination_machine_d(self):
        page_complete4 = self.Eeb.judge_machine_tape_width_select()
        self.assertTrue(page_complete4, "机器设备编辑网络带宽内容不完整，该用例执行失败")
      # 判断机器设备编辑网络运营内容完整性

    def test_examination_machine_f(self):
        page_complete5 = self.Eeb.judge_machine_motion_select()
        self.assertTrue(page_complete5, "机器设备编辑网络运营内容不完整，该用例执行失败")





if __name__ == "__main__":
    # 报告存放路径
    # fire_path = os.path.join(os.path.pardir + "/report/" + "login_ddt_case.html")
    fire_path = r"D:\pythonWork\autoTest\report\examination_machine.html"
    f = open(fire_path, 'wb')

    # 添加测试用例
    suite = unittest.TestLoader().loadTestsFromTestCase(ExaminationMachineDdtCase)

    # 测试结果以报告显示
    #runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='this is the first ddt report',description=u'这是我们机器设备数据驱动测试报告',verbosity=2)
    runner = HTMLTestRunner(stream=f,title='考场管理测试报告',description='考点环境机器设备编辑测试用例执行结果如下：' )
    run = HTMLTestRunner()
    runner.run(suite)
