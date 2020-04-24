#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time
from case.login_keyword_cases import LoginKeywordCases
from handle.examination_place_handle import ExaminationPlaceHandle
from handle.examination_room_handle import ExaminationRoomHandle
from util.table_util import TableUtil
from time import sleep


class ExaminationRoomBusiness(object):
    def __init__(self, driver):
        self.driver = driver
        self.ERh = ExaminationRoomHandle(self.driver)
        self.Tu = TableUtil(self.driver)

    # 判断详情页面元素是否完整
    def judge_page_complete(self):
        if self.ERh.judge_basic_info() and self.ERh.judge_traffic_info() and self.ERh.judge_book_info() and self.ERh.judge_btn_complete():
            return True
        else:
            return False
    #判断选择考点功能页面元素是否完整
    def select_function_complete(self):
        self.ERh.click_select_btn()
        if self.ERh.select_place_complete():
            return True
        else:
            return False
    #判断是否可直接选择“选择框”中的考点信息项
    def judge_direct_select_place(self):
        self.ERh.click_select_btn()
        self.ERh.click_select_place_by_search_btn()
        self.ERh.click_select_place_by_search_schild()
        select_text=self.ERh.get_select_text()
        basic_name_string=self.ERh.get_basic_name_text()
        basic_name_list=basic_name_string.split('：')
        if select_text==basic_name_list[1].strip():
            return True
        else:
            return False
    #判断是否可输入考点名称搜索框，支持模糊搜索
    def judge_direct_send_place(self):
        self.ERh.click_select_btn()
        key='财经'
        self.ERh.send_select_place_by_search_text(key)
        if key in self.ERh.get_place_by_search_fchild_text():
            return True
        else:
            return False
    #判断编辑考点总机位数、可编排机位数、考场数三字段是否不可编辑
    def judge_filed_status(self):
        status1=self.ERh.get_basic_edit_total_computer_num_status()
        status2=self.ERh.get_basic_edit_use_computer_num_status()
        status3=self.ERh.get_basic_edit_place_num_status()
        if status1==False and status2==False and status3==False:
            return True
        else:
            return False
    #编辑考点基本信息编辑框清空
    def clear_basic_all_edit(self):
        self.ERh.clear_basic_edit_code_text()
        self.ERh.clear_basic_edit_name_text()
        self.ERh.clear_basic_edit_time_text()
        self.ERh.clear_basic_edit_duration_text()
        self.ERh.clear_basic_edit_post_code_text()
        self.ERh.clear_basic_edit_place_person_text()
        self.ERh.clear_basic_edit_person_tel_text()
        #self.ERh.click_get_basic_edit_save_btn()








if __name__ == "__main__":
    lkc = LoginKeywordCases()
    lkc.run_keyword_excel_cases()
    driver = getattr(getattr(lkc, 'lk'), 'driver')
    driver.maximize_window()
    EPh = ExaminationPlaceHandle(driver)
    EPh.click_detailed_btn()
    ERb = ExaminationRoomBusiness(driver)
