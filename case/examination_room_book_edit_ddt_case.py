# coding=utf-8
import sys
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from business.examination_place_business import ExaminationPlaceBusiness
from util.table_util import TableUtil

sys.path.append('D:/pythonWork/autoTest')
from case.login_keyword_cases import LoginKeywordCases
import ddt
import unittest
import os
#import HTMLTestRunner
#from util.htmltestrunner.HTMLTestRunner import HTMLTestRunner
from util.HTMLTestRunner_PY3.HTMLTestRunner_PY3 import HTMLTestRunner
from business.examination_room_business import ExaminationRoomBusiness
from util.excel_util import ExcelUtil

# 获取数据
ex = ExcelUtil(excel_path=r"D:\pythonWork\autoTest\data\examinationRoomBookEditDdtData.xls")
data = ex.get_data()


# 测试类前加修饰@ddt.ddt
@ddt.ddt
# 姓名，性别，职位，手机，固定电话，邮寄地址，电子邮箱，qq
class ExaminationRoomBookEditDdtCase(unittest.TestCase):
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
        time.sleep(2)
        cls.EPh.click_detailed_btn()
        time.sleep(2)
        cls.book_table_num = cls.ERh.get_book_table_empty_text()
        if cls.book_table_num != '暂无数据':
            cls.Tu = TableUtil(cls.driver, 'book_table')
            cls.dataName = cls.Tu.get_data_book_edit(row=2,col=1)
            cls.position = cls.Tu.get_data_book_edit(row=2,col=3)
            cls.ERh.click_book_edit_btn()



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
        if self.ERh.judge_book_edit_frame():
            self.ERb.clear_book_all_edit()
        else:
            time.sleep(3)
            self.ERh.click_book_edit_btn()
            self.ERb.clear_book_all_edit()
    # 判断编辑通讯录回填数据是否完整
    def test_examination_room_edit_a(self):
        info_complete = self.ERb.book_edit_complete()
        self.assertTrue(info_complete, "编辑通讯录不完整，该用例执行失败")
    # case前加修饰 @ ddt.data()
    @ddt.data(*data)
    # 执行用例，并判断是否执行成功
    def test_examination_room_edit_b(self, data):
        if self.book_table_num != '暂无数据':
            book_add_name, book_add_phone, book_add_tel, book_add_post_address, book_add_mail, book_add_qq, assertCode, assertText = data
            edit_error = self.ERb.book_edit_function(book_add_name, book_add_phone, book_add_tel, book_add_post_address, book_add_mail,book_add_qq,assertCode,assertText)
            if len(assertCode) != 0:
                    self.assertTrue(edit_error, "该用例执行失败")
            else:
                self.assertTrue(edit_error, "添加失败，该用例执行失败")
        else:
            print('无数据可编辑，此用例不执行')
    # 判断编辑通讯录取字典值是否完整

    def test_examination_room_edit_c(self):
        result = self.ERb.judge_book_edit_position_complete()
        self.assertTrue(result, "通讯录取字典值不完整，该用例执行失败")

    # 成功编辑通讯录信息
    def test_examination_room_edit_d(self):
        self.ERh.send_book_edit_name(' 小周 ')
        self.ERh.click_book_edit_position()
        self.ERh.click_book_edit_position_child('book_edit_position_4child')
        self.ERh.click_book_edit_save_btn()
        time.sleep(1)
        result_text = self.ERh.judge_book_edit_frame()
        if result_text == False:
            result = True
        else:
            result = False

        self.assertTrue(result, "添加通讯录信息失败，该用例执行失败")
    # 判断编辑通讯录重复联系人结果

    def test_examination_room_edit_e(self):
        if self.dataName == None or self.book_table_num=='暂无数据':
            print('此用例不执行')
        else:
            self.ERh.send_book_edit_name(self.dataName)
            self.ERh.click_book_edit_position()
            if self.position == '考点负责人':
                self.ERh.click_book_edit_position_child('book_edit_position_1child')
            elif self.position == '考务负责人':
                self.ERh.click_book_edit_position_child('book_edit_position_2child')
            elif self.position == '机房管理员':
                self.ERh.click_book_edit_position_child('book_edit_position_3child')
            elif self.position == '财务负责人':
                self.ERh.click_book_edit_position_child('book_edit_position_4child')
            self.ERh.click_book_edit_save_btn()
            if self.ERh.judge_book_edit_frame() == True:
                result = True
            else:
                result = False
        self.assertTrue(result, "可编辑通讯录重复联系人，该用例执行失败")
    #判断点击取消按钮是否取消
    def test_examination_room_edit_f(self):
        self.ERh.click_book_edit_cancle_btn()
        time.sleep(1)
        if self.ERh.judge_book_edit_frame()==False:
            result=True
        else:
            result=False
        self.assertTrue(result, "点击取消按钮无法取消编辑，该用例执行失败")
if __name__ == "__main__":
    # 报告存放路径
    # fire_path = os.path.join(os.path.pardir + "/report/" + "login_ddt_case.html")
    fire_path = r"D:\pythonWork\autoTest\report\examination_room_book_edit.html"
    f = open(fire_path, 'wb')

    # 添加测试用例
    suite = unittest.TestLoader().loadTestsFromTestCase(ExaminationRoomBookEditDdtCase)

    # 测试结果以报告显示
    #runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='this is the first ddt report',description=u'这是我们登录模块数据驱动测试报告',verbosity=2)
    runner = HTMLTestRunner(stream=f, title='考场管理测试报告', description='考点基本信息通讯录编辑测试用例执行结果如下： ')
    runner.run(suite)
