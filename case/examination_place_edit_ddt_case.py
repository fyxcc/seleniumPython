# coding=utf-8
import sys

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

sys.path.append('D:/pythonWork/autoTest')
from case.login_keyword_cases import LoginKeywordCases
import ddt
import unittest
import os
#import HTMLTestRunner
from util.htmltestrunner.HTMLTestRunner import HTMLTestRunner
from business.examination_place_business import ExaminationPlaceBusiness
from util.excel_util import ExcelUtil

# 获取数据
ex = ExcelUtil(excel_path=r"D:\pythonWork\autoTest\data\examinationPlaceEditDdtData.xls")
data = ex.get_data()


# 测试类前加修饰@ddt.ddt
@ddt.ddt
# 考点编号，考点名称，考点地址，考点负责人，负责人联系电话
class ExaminationPlaceEditDdtCase(unittest.TestCase):
    # 所有case执行之前的装饰器---前置条件
    @classmethod
    def setUpClass(cls):
        print('所有case执行的前置条件')
        lkc = LoginKeywordCases()
        lkc.run_keyword_excel_cases()
        cls.driver = getattr(getattr(lkc, 'lk'), 'driver')
        cls.driver.maximize_window()
        cls.Eb = ExaminationPlaceBusiness(cls.driver)
        Eh = getattr(cls.Eb, 'Eh')
        Eh.click_edit_btn()

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
        Ep = getattr(getattr(self.Eb, 'Eh'), 'Ep')
        Eh = getattr(self.Eb, 'Eh')
        if Eh.judge_edit_frame():
            #Ep.get_edit_place_code().clear()
            if Ep.get_edit_place_code().get_attribute('value') is not None:
                edit_place_code=Ep.get_edit_place_code()
                edit_place_code.send_keys(Keys.CONTROL, 'a')
                edit_place_code.send_keys(Keys.BACK_SPACE)
            else:
                Ep.get_edit_place_code().clear()
            if Ep.get_edit_place_name().get_attribute('value') is not None:
                edit_place_name = Ep.get_edit_place_name()
                edit_place_name.send_keys(Keys.CONTROL, 'a')
                edit_place_name.send_keys(Keys.BACK_SPACE)
            else:
                Ep.get_edit_place_name().clear()
            # Ep.get_edit_place_division_code().clear()
            # clear_btn=Ep.clear_place_division_code()
            # ActionChains(self.driver).move_to_element(clear_btn).click(clear_btn).perform()
            # ctionChains(self.driver).click(clear_btn).perform()
            if Ep.get_edit_place_address().get_attribute('value') is not None:
                edit_place_address = Ep.get_edit_place_address()
                edit_place_address.send_keys(Keys.CONTROL, 'a')
                edit_place_address.send_keys(Keys.BACK_SPACE)
            else:
               Ep.get_edit_place_address().clear()
            if  Ep.get_edit_place_person().get_attribute('value') is not None:
                edit_place_person =  Ep.get_edit_place_person()
                edit_place_person.send_keys(Keys.CONTROL, 'a')
                edit_place_person.send_keys(Keys.BACK_SPACE)
            else:
                Ep.get_edit_place_person().clear()
            if Ep.get_edit_place_person_tel().get_attribute('value') is not None:
                edit_place_person_tel = Ep.get_edit_place_person_tel()
                edit_place_person_tel.send_keys(Keys.CONTROL, 'a')
                edit_place_person_tel.send_keys(Keys.BACK_SPACE)
            else:
                Ep.get_edit_place_person_tel().clear()

    def test_examination_place_edit_a(self):
        info_complete = self.Eb.edit_complete()
        self.assertTrue(info_complete, "编辑考点信息不完整，该用例执行失败")

    # case前加修饰 @ ddt.data()
    @ddt.data(*data)
    # 执行用例，并判断是否执行成功
    def test_examination_place_edit_b(self, data):
        place_code, place_name, place_address, place_person, place_person_tel, assertCode, assertText = data
        edit_error = self.Eb.edit_function(place_code, place_name, place_address, place_person, place_person_tel,
                                           assertCode, assertText)
        if len(assertCode) != 0:
                self.assertTrue(edit_error, "该用例执行失败")
        else:
            self.assertTrue(edit_error, "添加失败，该用例执行失败")


if __name__ == "__main__":
    # 报告存放路径
    # fire_path = os.path.join(os.path.pardir + "/report/" + "login_ddt_case.html")
    fire_path = r"D:\pythonWork\autoTest\report\examination_place_edit.html"
    f = open(fire_path, 'wb')

    # 添加测试用例
    suite = unittest.TestLoader().loadTestsFromTestCase(ExaminationPlaceEditDdtCase)

    # 测试结果以报告显示
    #runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='this is the first ddt report', description=u'这是我们登录模块数据驱动测试报告',verbosity=2)
    runner = HTMLTestRunner(stream=f, title='考点管理测试报告', description='考点编辑测试用例执行结果如下：')
    run = HTMLTestRunner()
    runner.run(suite)
