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
        # self.ERp=getattr(self.ERh,'ERp')

    # 判断详情页面元素是否完整
    def judge_page_complete(self):
        if self.Eeh.judge_envir_complete() and self.Eeh.judge_machine_complete() and self.Eeh.judge_photo_complete():
            return True
        else:
            return False

    # 判断开关键是否默认为否
    def judge_default_value(self):
        time.sleep(1)
        self.Eeh.click_envir_edit_btn()
        time.sleep(1)
        data1 = self.Eeh.get_envir_edit_paking_condition_text()
        data2 = self.Eeh.get_envir_edit_wating_room_text()
        data3 = self.Eeh.get_envir_edit_examination_office_text()
        data4 = self.Eeh.get_envir_edit_control_room_text()
        data5 = self.Eeh.get_envir_edit_detention_chamber_text()
        data6 = self.Eeh.get_envir_edit_confidential_room_text()
        data7 = self.Eeh.get_envir_edit_safety_box_text()
        data8 = self.Eeh.get_envir_edit_independent_room_text()
        data9 = self.Eeh.get_envir_edit_medkit_text()
        if data1 == '有' or data2 == '有' or data3 == '有' or data4 == '有' or data5 == '有' or data6 == '有' or data7 == '有' or data8 == '有' or data9 == '有':
            return False
        else:
            return True

    # 清空编辑考场环境输入框
    def clear_all_envir(self):
        self.Eeh.clear_envir_edit_place_area()
        self.Eeh.clear_envir_edit_place_spread()
        self.Eeh.clear_envir_edit_cars_num()
        self.Eeh.clear_envir_edit_toilet_condition()

    # 环境信息成功编辑

    def envir_success_edit(self, envir_edit_place_area, envir_edit_place_spread, envir_edit_toilet_condition,
                           envir_edit_cars_num):
        self.Eeh.send_envir_edit_place_area(envir_edit_place_area)
        self.Eeh.send_envir_edit_place_spread(envir_edit_place_spread)
        self.Eeh.send_envir_edit_toilet_condition(envir_edit_toilet_condition)
        self.Eeh.send_envir_edit_cars_num(envir_edit_cars_num)
        self.Eeh.click_envir_edit_save_btn()

    # 环境信息数据驱动整合代码

    def envir_edit_function(self, envir_edit_place_area, envir_edit_place_spread, envir_edit_toilet_condition,
                            envir_edit_cars_num,
                            assertCode, assertText):
        self.envir_success_edit(envir_edit_place_area, envir_edit_place_spread, envir_edit_toilet_condition,
                                envir_edit_cars_num)
        if assertText == '正确的电话格式':
            if self.ERp.get_book_add_tel_error() == None:
                return True
        elif len(assertCode) != 0:
            if self.Eeh.get_envir_edit_error_text(assertCode, assertText) is None:
                return False
            else:
                print("用例通过")
                return True

    # 判断机器设备编辑开关键是否默认为否
    def judge_machine_default_value(self):
        time.sleep(1)
        self.Eeh.click_machine_edit_btn()
        time.sleep(1)
        data1 = self.Eeh.get_machine_edit_metal_detector_text()
        data2 = self.Eeh.get_machine_edit_signal_shield_text()
        data3 = self.Eeh.get_machine_edit_video_monitor_text()
        data4 = self.Eeh.get_machine_edit_gen_text()
        data5 = self.Eeh.get_machine_edit_electricity_text()
        data6 = self.Eeh.get_machine_edit_cloud_desktop_text()
        data7 = self.Eeh.get_machine_edit_virtual_server_text()
        data8 = self.Eeh.get_machine_edit_ups_text()
        data9 = self.Eeh.get_machine_edit_insert_text()
        data10 = self.Eeh.get_machine_edit_interworking_text()
        if data1 == '有' or data2 == '有' or data3 == '有' or data4 == '有' or data5 == '有' or data6 == '有' or data7 == '有' or data8 == '有' or data9 == '有' or data10 == '有':
            return False
        else:
            return True

    # 清空机器设备输入框

    def clear_all_machine(self):
        self.Eeh.clear_machine_edit_available_examination()
        self.Eeh.clear_machine_edit_processor()
        self.Eeh.clear_machine_edit_storage()
        self.Eeh.clear_machine_edit_caliche()
        self.Eeh.clear_machine_edit_ups_model()
        self.Eeh.clear_machine_edit_ups_time()

    # 机器设备成功编辑

    def machine_success_edit(self, machine_edit_available_examination, machine_edit_processor, machine_edit_storage,
                             machine_edit_caliche, machine_edit_ups_model, machine_edit_ups_time):
        self.Eeh.send_machine_edit_available_examination(machine_edit_available_examination)
        self.Eeh.send_machine_edit_processor(machine_edit_processor)
        self.Eeh.send_machine_edit_storage(machine_edit_storage)
        self.Eeh.send_machine_edit_caliche(machine_edit_caliche)
        self.Eeh.send_machine_edit_ups_model(machine_edit_ups_model)
        self.Eeh.send_machine_edit_ups_time(machine_edit_ups_time)
        time.sleep(1)
        self.Eeh.click_machine_edit_save_btn()

    # 机器设备数据驱动整合代码

    def machine_edit_function(self, machine_edit_available_examination, machine_edit_processor, machine_edit_storage,
                              machine_edit_caliche, machine_edit_ups_model, machine_edit_ups_time, assertCode,
                              assertText):
        self.machine_success_edit(machine_edit_available_examination, machine_edit_processor, machine_edit_storage,
                                  machine_edit_caliche, machine_edit_ups_model, machine_edit_ups_time)
        if assertText == '编辑成功':
            time.sleep(1)
            result = self.Eeh.get_machine_edit_success_text()
            if result == assertText:
                return True
        elif len(assertCode) != 0:
            if self.Eeh.get_machine_edit_error_text(assertCode, assertText) is None:
                return False
            else:
                print("用例通过")
                return True

    # 判断机器设备编辑处理器下拉框内容
    def judge_machine_processor_select(self):
        self.Eeh.click_machine_edit_processor_select()
        time.sleep(1)
        child1 = self.Eeh.get_machine_edit_processor_select1_text()
        child2 = self.Eeh.get_machine_edit_processor_select2_text()
        child3 = self.Eeh.get_machine_edit_processor_select3_text()
        child4 = self.Eeh.get_machine_edit_processor_select4_text()
        child5 = self.Eeh.get_machine_edit_processor_select5_text()
        child6 = self.Eeh.get_machine_edit_processor_select6_text()
        child7 = self.Eeh.get_machine_edit_processor_select7_text()
        if child1 == '1核' and child2 == '2核' and child3 == '4核' and child4 == '8核' and child5 == '12核' and child6 == '16核' and child7 == '24核及以上':
            return True
        else:
            return False

    # 判断机器设备编辑网卡字段
    def judge_internet_card_complete(self):
        data1 = self.Eeh.get_machine_edit_internet_card1_text()
        data2 = self.Eeh.get_machine_edit_internet_card2_text()
        data3 = self.Eeh.get_machine_edit_internet_card3_text()
        if data1 == '百兆' and data2 == '千兆' and data3 == '万兆':
            return True
        else:
            return False

    # 判断机器设备编辑操作系统下拉框内容

    def judge_machine_operating_system_select(self):
        self.Eeh.click_machine_edit_operating_system()
        time.sleep(1)
        child1 = self.Eeh.get_machine_edit_operating_system1_text()
        child2 = self.Eeh.get_machine_edit_operating_system2_text()
        child3 = self.Eeh.get_machine_edit_operating_system3_text()
        child4 = self.Eeh.get_machine_edit_operating_system4_text()
        child5 = self.Eeh.get_machine_edit_operating_system5_text()
        child6 = self.Eeh.get_machine_edit_operating_system6_text()
        if child1 == 'Windows server 2000' and child2 == 'Windows server 2003' and child3 == 'Windows server 2008' and child4 == 'Windows server 2012' and child5 == 'Windows server 2016' and child6 == 'Windows server 2019':
            return True
        else:
            return False

    # 判断机器设备编辑网络带宽下拉框内容

    def judge_machine_tape_width_select(self):
        self.Eeh.click_machine_edit_tape_width_text()
        time.sleep(1)
        child1 = self.Eeh.get_machine_edit_tape_width1_text()
        child2 = self.Eeh.get_machine_edit_tape_width2_text()
        child3 = self.Eeh.get_machine_edit_tape_width3_text()
        if child1 == '50mbps' and child2 == '100mbps' and child3 == '1000mbps':
            return True
        else:
            return False

    # 判断机器设备编辑网络运营下拉框内容

    def judge_machine_motion_select(self):
        self.Eeh.click_get_machine_motion_select()
        time.sleep(1)
        child1 = self.Eeh.get_machine_motion_select1_text()
        child2 = self.Eeh.get_machine_motion_select2_text()
        child3 = self.Eeh.get_machine_motion_select3_text()
        child4 = self.Eeh.get_machine_motion_select4_text()
        child5 = self.Eeh.get_machine_motion_select5_text()
        child6 = self.Eeh.get_machine_motion_select6_text()
        child7 = self.Eeh.get_machine_motion_select7_text()
        if child1 == '电信' and child2 == '移动' and child3 == '联通' and child4 == '网通' and child5 == '铁通' and child6 == '拨号' and child7 == '教育网':
            return True
        else:
            return False
    # 清空机器设备输入框

    def clear_all_photo_add(self):
        self.Eeh.clear_photo_add_title()
        self.Eeh.clear_photo_add_content()

    # 考点照片成功添加

    def machine_success_add_photo(self, photo_path,photo_name,screen_capture,photo_add_title, photo_add_content):
        self.Eeh.browse_photo_add_photo_path(photo_path,photo_name,screen_capture)
        self.Eeh.send_photo_add_title(photo_add_title)
        self.Eeh.send_photo_add_content(photo_add_content)
        time.sleep(1)
        self.Eeh.click_photo_add_save_btn()

    # 考点照片数据驱动整合代码

    def machine_photo_add_function(self, photo_path,photo_name,screen_capture,photo_add_title, photo_add_content, assertCode, assertText):
        self.machine_success_add_photo(photo_path,photo_name,screen_capture,photo_add_title, photo_add_content)
        time.sleep(1)
        if assertText == '添加成功':
            time.sleep(1)
            result = self.Eeh.get_photo_add_result_text()
            if result == assertText:
                return True
        elif len(assertCode) != 0:
            if self.Eeh.get_photo_add_error_text(assertCode, assertText) is None:
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
    time, sleep(1)
    Eeh = ExaminationeEnvirHandle(driver)
    Eeh.click_envir_btn()
    Eeh.click_machine_edit_btn()
    time.sleep(1)
    Eeb = ExaminationEnvirBusiness(driver)
    print(Eeb.judge_machine_operating_system_select())
