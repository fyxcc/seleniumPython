#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time
from case.login_keyword_cases import LoginKeywordCases
from handle.examination_place_handle import ExaminationPlaceHandle
from handle.examination_envir_handle import ExaminationeEnvirHandle
from util.table_util import TableUtil
from time import sleep


class ExaminationEnvirBusiness(object):
    def __init__(self, driver):
        self.driver = driver
        self.Eeh = ExaminationeEnvirHandle(self.driver)
        self.Tu = TableUtil(self.driver)
        #self.ERp=getattr(self.ERh,'ERp')

    # 判断详情页面元素是否完整
    def judge_page_complete(self):
        if self.Eeh.judge_envir_complete() and self.Eeh.judge_machine_complete() and self.Eeh.judge_photo_complete() :
            return True
        else:
            return False
    #判断开关键是否默认为否
    def judge_default_value(self):
        time.sleep(1)
        self.Eeh.click_envir_edit_btn()
        time.sleep(1)
        data1=self.Eeh.get_envir_edit_paking_condition_text()
        data2=self.Eeh.get_envir_edit_wating_room_text()
        data3=self.Eeh.get_envir_edit_examination_office_text()
        data4=self.Eeh.get_envir_edit_control_room_text()
        data5=self.Eeh.get_envir_edit_detention_chamber_text()
        data6=self.Eeh.get_envir_edit_confidential_room_text()
        data7=self.Eeh.get_envir_edit_safety_box_text()
        data8=self.Eeh.get_envir_edit_independent_room_text()
        data9=self.Eeh.get_envir_edit_medkit_text()
        if data1=='有' or data2=='有' or data3=='有' or data4=='有' or data5=='有' or data6=='有' or data7=='有' or data8=='有' or data9=='有':
            return False
        else:
            return True
    #清空编辑考场环境输入框
    def clear_all_envir(self):
        self.Eeh.clear_envir_edit_place_area()
        self.Eeh.clear_envir_edit_place_spread()
        self.Eeh.clear_envir_edit_cars_num()
        self.Eeh.clear_envir_edit_toilet_condition()

    # 环境信息成功编辑

    def book_success_edit(self,  envir_edit_place_area, envir_edit_place_spread, envir_edit_toilet_condition, envir_edit_cars_num):
        self.Eeh.send_envir_edit_place_area(envir_edit_place_area)
        self.Eeh.send_envir_edit_place_spread(envir_edit_place_spread)
        self.Eeh.send_envir_edit_toilet_condition(envir_edit_toilet_condition)
        self.Eeh.send_envir_edit_cars_num(envir_edit_cars_num)
        self.Eeh.click_envir_edit_save_btn()


    # 环境信息数据驱动整合代码

    def envir_edit_function(self,  envir_edit_place_area, envir_edit_place_spread, envir_edit_toilet_condition, envir_edit_cars_num,
                          assertCode, assertText):
        self.book_success_edit( envir_edit_place_area, envir_edit_place_spread, envir_edit_toilet_condition, envir_edit_cars_num)
        if assertText == '正确的电话格式':
            if self.ERp.get_book_add_tel_error() == None:
                return True
        elif len(assertCode) != 0:
            if self.Eeh.get_envir_edit_error_text(assertCode, assertText) is None:
                return False
            else:
                print("用例通过")
                return True

if __name__ == "__main__":
    lkc = LoginKeywordCases()
    lkc.run_keyword_excel_cases()
    driver = getattr(getattr(lkc, 'lk'), 'driver')
    driver.maximize_window()
    EPh = ExaminationPlaceHandle(driver)
    EPh.click_detailed_btn()
    time,sleep(1)
    Eeh=ExaminationeEnvirHandle(driver)
    Eeh.click_envir_btn()
    time.sleep(1)
    Eeb = ExaminationEnvirBusiness(driver)
    Eeh.click_envir_edit_btn()
    print(Eeb.judge_default_value())