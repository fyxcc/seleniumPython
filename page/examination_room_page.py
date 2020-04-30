#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time

from selenium.webdriver.support.wait import WebDriverWait
from basic.find_element import FindElement
from case.login_keyword_cases import LoginKeywordCases
from page.examination_place_page import ExaminationPlacePage


class ExaminationRoomPage(object):
    # 初始化元素查找类，执行该类的时候就会加载
    def __init__(self, driver):
        self.driver = driver
        self.fe = FindElement(driver)

    # 基本资料考点编号
    def get_basic_code(self):
        return self.fe.get_element('basic_code', 'ExaminationPlaceRoom')

    # 基本资料考点名称
    def get_basic_name(self):
        return self.fe.get_element('basic_name', 'ExaminationPlaceRoom')

    # 基本资料考点性质

    def get_basic_character(self):
        return self.fe.get_element('basic_character', 'ExaminationPlaceRoom')

    # 基本资料可用总机位数

    def get_basic_total_computer_num(self):
        return self.fe.get_element('basic_total_computer_num', 'ExaminationPlaceRoom')

    # 基本资料可编排机位数

    def get_basic_use_computer_num(self):
        return self.fe.get_element('basic_use_computer_num', 'ExaminationPlaceRoom')

    # 基本资料考场数

    def get_basic_place_num(self):
        return self.fe.get_element('basic_place_num', 'ExaminationPlaceRoom')

    # 基本资料合同签订时间

    def get_basic_time(self):
        return self.fe.get_element('basic_time', 'ExaminationPlaceRoom')

    # 基本资料合同签订时长

    def get_basic_duration(self):
        return self.fe.get_element('basic_duration', 'ExaminationPlaceRoom')

    # 基本资料邮政编码

    def get_basic_post_code(self):
        return self.fe.get_element('basic_post_code', 'ExaminationPlaceRoom')

    # 基本资料考点负责人

    def get_basic_place_person(self):
        return self.fe.get_element('basic_place_person', 'ExaminationPlaceRoom')

    # 基本资料考点负责人电话
    def get_basic_person_tel(self):
        return self.fe.get_element('basic_person_tel', 'ExaminationPlaceRoom')

    # 基本资料编辑按钮
    def get_basic_edit_btn(self):
        return self.fe.get_element('basic_edit_btn', 'ExaminationPlaceRoom')
        # 基本资料编辑保存按钮

    def get_basic_edit_save_btn(self):
        return self.fe.get_element('basic_edit_save_btn', 'ExaminationPlaceRoom')
        # 基本资料编辑取消按钮

    def get_basic_edit_cancle_btn(self):
        return self.fe.get_element('basic_edit_cancle_btn', 'ExaminationPlaceRoom')
        # 基本资料编辑编号

    def get_basic_edit_code(self):
        return self.fe.get_element('basic_edit_code', 'ExaminationPlaceRoom')
        # 错误基本资料编辑编号提示语

    def get_basic_edit_code_error(self):
        return self.fe.get_element('basic_edit_code_error', 'ExaminationPlaceRoom')
        # 基本资料编辑名称

    def get_basic_edit_name(self):
        return self.fe.get_element('basic_edit_name', 'ExaminationPlaceRoom')
        # 错误基本资料编辑名称提示语

    def get_basic_edit_name_error(self):
        return self.fe.get_element('basic_edit_name_error', 'ExaminationPlaceRoom')
        # 基本资料编辑性质

    def get_basic_edit_character(self):
        return self.fe.get_element('basic_edit_character', 'ExaminationPlaceRoom')
        # 基本资料编辑性质1

    def get_basic_edit_character_1child(self):
        return self.fe.get_element('basic_edit_character_1child', 'ExaminationPlaceRoom')
        # 基本资料编辑性质2

    def get_basic_edit_character_2child(self):
        return self.fe.get_element('basic_edit_character_2child', 'ExaminationPlaceRoom')
        # 基本资料编辑性质3

    def get_basic_edit_character_3child(self):
        return self.fe.get_element('basic_edit_character_3child', 'ExaminationPlaceRoom')
        # 基本资料编辑性质4

    def get_basic_edit_character_4child(self):
        return self.fe.get_element('basic_edit_character_4child', 'ExaminationPlaceRoom')
        # 基本资料编辑性质5

    def get_basic_edit_character_5child(self):
        return self.fe.get_element('basic_edit_character_5child', 'ExaminationPlaceRoom')
        # 基本资料编辑性质6

    def get_basic_edit_character_6child(self):
        return self.fe.get_element('basic_edit_character_6child', 'ExaminationPlaceRoom')
        # 基本资料编辑性质7

    def get_basic_edit_character_7child(self):
        return self.fe.get_element('basic_edit_character_7child', 'ExaminationPlaceRoom')

        # 错误基本资料编辑性质提示语

    """ 
   def get_basic_edit_character_error(self):
        return self.fe.get_element('basic_edit_character', 'ExaminationPlaceRoom')
   """

    # 基本资料编辑可用总机位数

    def get_basic_edit_total_computer_num(self):
        return self.fe.get_element('basic_edit_total_computer_num', 'ExaminationPlaceRoom')

    # 基本资料编辑可编排机位数

    def get_basic_edit_use_computer_num(self):
        return self.fe.get_element('basic_edit_use_computer_num', 'ExaminationPlaceRoom')

    # 基本资料编辑考场数

    def get_basic_edit_place_num(self):
        return self.fe.get_element('basic_edit_place_num', 'ExaminationPlaceRoom')

    # 基本资料编辑合同签订时间

    def get_basic_edit_time(self):
        return self.fe.get_element('basic_edit_time', 'ExaminationPlaceRoom')

    # 错误基本资料编辑合同签订时间提示语

    def get_basic_edit_time_error(self):
        return self.fe.get_element('basic_edit_time_error', 'ExaminationPlaceRoom')

    # 基本资料编辑合同签订时长

    def get_basic_edit_duration(self):
        return self.fe.get_element('basic_edit_duration', 'ExaminationPlaceRoom')

    # 错误基本资料编辑合同签订时长提示语

    def get_basic_edit_duration_error(self):
        return self.fe.get_element('basic_edit_duration_error', 'ExaminationPlaceRoom')

    # 基本资料编辑邮政编码

    def get_basic_edit_post_code(self):
        return self.fe.get_element('basic_edit_post_code', 'ExaminationPlaceRoom')

    # 错误基本资料编辑邮政编码提示语

    def get_basic_edit_post_code_error(self):
        return self.fe.get_element('basic_edit_post_code_error', 'ExaminationPlaceRoom')

    # 基本资料编辑考点负责人

    def get_basic_edit_place_person(self):
        return self.fe.get_element('basic_edit_place_person', 'ExaminationPlaceRoom')

    # 错误基本资料编辑考点负责人提示语

    def get_basic_edit_place_person_error(self):
        return self.fe.get_element('basic_edit_place_person_error', 'ExaminationPlaceRoom')

    # 错误基本资料编辑负责人电话提示语

    def get_basic_edit_person_tel_error(self):
        return self.fe.get_element('basic_edit_person_tel_error', 'ExaminationPlaceRoom')

    # 基本资料编辑负责人电话

    def get_basic_edit_person_tel(self):
        return self.fe.get_element('basic_edit_person_tel', 'ExaminationPlaceRoom')

    # 编辑成功提示语
    def get_basic_edit_success(self):
        return self.fe.get_element('basic_edit_success', 'ExaminationPlaceRoom')

    # 交通路线的考点地址
    def get_traffic_address(self):
        return self.fe.get_element('traffic_address', 'ExaminationPlaceRoom')

    # 交通路线的交通情况

    def get_traffic_condition(self):
        return self.fe.get_element('traffic_condition', 'ExaminationPlaceRoom')

    # 交通路线的具体线路

    def get_traffic_concrete_route(self):
        return self.fe.get_element('traffic_concrete_route', 'ExaminationPlaceRoom')

    # 交通路线的地理位置描述

    def get_traffic_location(self):
        return self.fe.get_element('traffic_location', 'ExaminationPlaceRoom')

    # 交通路线的经度

    def get_traffic_longitude(self):
        return self.fe.get_element('traffic_longitude', 'ExaminationPlaceRoom')

    # 交通路线的纬度

    def get_traffic_latitude(self):
        return self.fe.get_element('traffic_latitude', 'ExaminationPlaceRoom')

    # 交通路线的编辑按钮

    def get_traffic_edit_btn(self):
        return self.fe.get_element('traffic_edit_btn', 'ExaminationPlaceRoom')

    # 交通路线的编辑保存按钮

    def get_traffic_edit_save_btn(self):
        return self.fe.get_element('traffic_edit_save_btn', 'ExaminationPlaceRoom')

    # 交通路线的编辑取消按钮

    def get_traffic_edit_cancle_btn(self):
        return self.fe.get_element('traffic_edit_cancle_btn', 'ExaminationPlaceRoom')

    # 交通路线的编辑考点地址

    def get_traffic_edit_address(self):
        return self.fe.get_element('traffic_edit_address', 'ExaminationPlaceRoom')

    # 错误交通路线的考点地址提示语

    def get_traffic_address_error(self):
        return self.fe.get_element('traffic_edit_address_error', 'ExaminationPlaceRoom')

    # 交通路线的编辑交通情况

    def get_traffic_edit_condition(self):
        return self.fe.get_element('traffic_edit_condition', 'ExaminationPlaceRoom')

    # 错误交通路线的交通情况提示语
    def get_traffic_edit_condition_error(self):
        return self.fe.get_element('traffic_edit_condition_error', 'ExaminationPlaceRoom')

    # 交通路线的编辑具体线路

    def get_traffic_edit_concrete_route(self):
        return self.fe.get_element('traffic_edit_concrete_route', 'ExaminationPlaceRoom')

    # 错误交通路线的具体线路体提示语
    def get_traffic_edit_concrete_route_error(self):
        return self.fe.get_element('traffic_edit_concrete_route_error', 'ExaminationPlaceRoom')

    # 交通路线的编辑地理位置描述

    def get_traffic_edit_location(self):
        return self.fe.get_element('traffic_edit_location', 'ExaminationPlaceRoom')

    # 错误交通路线的地理位置描述提示语
    def get_traffic_edit_location_error(self):
        return self.fe.get_element('traffic_edit_location_error', 'ExaminationPlaceRoom')

    # 交通路线的编辑经度

    def get_traffic_edit_longitude(self):
        return self.fe.get_element('traffic_edit_longitude', 'ExaminationPlaceRoom')

    # 交通路线的编辑纬度

    def get_traffic_edit_latitude(self):
        return self.fe.get_element('traffic_edit_latitude', 'ExaminationPlaceRoom')

    # 通讯录姓名
    def get_book_table_name(self):
        return self.fe.get_element('book_table_name', 'ExaminationPlaceRoom')

    # 通讯录性别

    def get_book_table_sex(self):
        return self.fe.get_element('book_table_sex', 'ExaminationPlaceRoom')

    # 通讯录职位

    def get_book_table_position(self):
        return self.fe.get_element('book_table_position', 'ExaminationPlaceRoom')

    # 通讯录手机

    def get_book_table_tel(self):
        return self.fe.get_element('book_table_tel', 'ExaminationPlaceRoom')

    # 通讯录固定电话

    def get_book_table_fixed_phone(self):
        return self.fe.get_element('book_table_fixed_phone', 'ExaminationPlaceRoom')

    # 通讯录邮寄地址

    def get_book_table_post_address(self):
        return self.fe.get_element('book_table_post_address', 'ExaminationPlaceRoom')

    # 通讯录电子邮箱

    def get_book_table_email(self):
        return self.fe.get_element('book_table_email', 'ExaminationPlaceRoom')

    # 通讯录qq

    def get_book_table_qq(self):
        return self.fe.get_element('book_table_qq', 'ExaminationPlaceRoom')

    # 考点数

    def get_place_num(self):
        return self.fe.get_element('place_num', 'ExaminationPlaceRoom')

    # 通讯录添加按钮

    def get_book_add_btn(self):
        return self.fe.get_element('book_add_btn', 'ExaminationPlaceRoom')

    # 通讯录添加确定按钮

    def get_book_add_confirm_btn(self):
        return self.fe.get_element('book_add_confirm_btn', 'ExaminationPlaceRoom')

    # 通讯录添加取消按钮

    def get_book_add_cancle_btn(self):
        return self.fe.get_element('book_add_cancle_btn', 'ExaminationPlaceRoom')

    # 获取添加通讯录弹框
    def get_book_add_frame(self):
        return self.fe.get_element('book_add_frame', 'ExaminationPlaceRoom')

    # 添加通讯录姓名
    def get_book_add_name(self):
        return self.fe.get_element('book_add_name', 'ExaminationPlaceRoom')

    # 错误添加通讯录姓名提示语
    def get_book_add_name_error(self):
        return self.fe.get_element('book_add_name_error', 'ExaminationPlaceRoom')

    # 添加通讯录性别

    def get_book_add_sex(self):
        return self.fe.get_element('book_add_sex', 'ExaminationPlaceRoom')

    # 添加通讯录性别男
    def get_book_add_male(self):
        return self.fe.get_element('book_add_male', 'ExaminationPlaceRoom')

    # 添加通讯录性别女
    def get_book_add_female(self):
        return self.fe.get_element('book_add_female', 'ExaminationPlaceRoom')

    # 添加通讯录职位

    def get_book_add_position(self):
        return self.fe.get_element('book_add_position', 'ExaminationPlaceRoom')

    # 错误添加通讯录职位提示语

    def get_book_add_position_error(self):
        return self.fe.get_element('book_add_position_error', 'ExaminationPlaceRoom')
    # 添加通讯录职位1

    def get_book_add_position_1child(self):
        return self.fe.get_element('book_add_position_1child', 'ExaminationPlaceRoom')
    # 添加通讯录职位2

    def get_book_add_position_2child(self):
        return self.fe.get_element('book_add_position_2child', 'ExaminationPlaceRoom')
    # 添加通讯录职位3

    def get_book_add_position_3child(self):
        return self.fe.get_element('book_add_position_3child', 'ExaminationPlaceRoom')
    # 添加通讯录职位4

    def get_book_add_position_4child(self):
        return self.fe.get_element('book_add_position_4child', 'ExaminationPlaceRoom')

    # 添加通讯录手机
    def get_book_add_phone(self):
        return self.fe.get_element('book_add_phone', 'ExaminationPlaceRoom')

    # 错误添加通讯录手机提示语
    def get_book_add_phone_error(self):
        return self.fe.get_element('book_add_phone_error', 'ExaminationPlaceRoom')

    # 添加通讯录固定电话
    def get_book_add_tel(self):
        return self.fe.get_element('book_add_tel', 'ExaminationPlaceRoom')

    # 错误添加通讯录固定电话提示语
    def get_book_add_tel_error(self):
        return self.fe.get_element('book_add_tel_error', 'ExaminationPlaceRoom')

    # 添加通讯录邮寄地址
    def get_book_add_post_address(self):
        return self.fe.get_element('book_add_post_address', 'ExaminationPlaceRoom')

    # 错误添加通讯录邮寄地址提示语
    def get_book_add_post_address_error(self):
        return self.fe.get_element('book_add_post_address_error', 'ExaminationPlaceRoom')

    # 添加通讯录电子邮箱
    def get_book_add_mail(self):
        return self.fe.get_element('book_add_mail', 'ExaminationPlaceRoom')

    # 错误添加通讯录电子邮箱提示语

    def get_book_add_mail_error(self):
        return self.fe.get_element('book_add_mail_error', 'ExaminationPlaceRoom')

    # 添加通讯录qq
    def get_book_add_qq(self):
        return self.fe.get_element('book_add_qq', 'ExaminationPlaceRoom')

    # 错误添加通讯录qq提示语

    def get_book_add_qq(self):
        return self.fe.get_element('book_add_qq', 'ExaminationPlaceRoom')
    #添加失败结果提示信息
    def get_book_add_result_fail(self):
        return self.fe.get_element('book_add_result_fail', 'ExaminationPlaceRoom')
    # 添加成功结果提示信息

    def get_book_add_result_success(self):
        return self.fe.get_element('book_add_result_success', 'ExaminationPlaceRoom')
    #通讯录表格
    def get_book_table(self):
        return self.fe.get_element('book_table', 'ExaminationPlaceRoom')
    #空通讯录表格提醒字段
    def get_book_table_empty(self):
        return self.fe.get_element('book_table_empty', 'ExaminationPlaceRoom')
    #通讯录编辑按钮
    def get_book_edit_btn(self):
        return self.fe.get_element('book_edit_btn', 'ExaminationPlaceRoom')
    #通讯录编辑保存按钮
    def get_book_edit_save_btn(self):
        return self.fe.get_element('book_edit_save_btn', 'ExaminationPlaceRoom')
    #通讯录编辑取消按钮
    def get_book_edit_cancle_btn(self):
        return self.fe.get_element('book_edit_cancle_btn', 'ExaminationPlaceRoom')
    #通讯录编辑弹框
    def get_book_edit_frame(self):
        return self.fe.get_element('book_edit_frame', 'ExaminationPlaceRoom')
    #通讯录编辑姓名
    def get_book_edit_name(self):
        return self.fe.get_element('book_edit_name', 'ExaminationPlaceRoom')
    # 错误通讯录编辑姓名提示语

    def get_book_edit_name_error(self):
        return self.fe.get_element('book_edit_name_error', 'ExaminationPlaceRoom')

    # 通讯录编辑职位
    def get_book_edit_position(self):
        return self.fe.get_element('book_edit_position', 'ExaminationPlaceRoom')
    # 错误通讯录编辑职位提示语

    def get_book_edit_position_error(self):
        return self.fe.get_element('book_edit_position_error', 'ExaminationPlaceRoom')
    # 编辑通讯录职位1

    def get_book_edit_position_1child(self):
        return self.fe.get_element('book_edit_position_1child', 'ExaminationPlaceRoom')
    # 编辑通讯录职位2

    def get_book_edit_position_2child(self):
        return self.fe.get_element('book_edit_position_2child', 'ExaminationPlaceRoom')
    # 编辑通讯录职位3

    def get_book_edit_position_3child(self):
        return self.fe.get_element('book_edit_position_3child', 'ExaminationPlaceRoom')
    # 编辑通讯录职位4

    def get_book_edit_position_4child(self):
        return self.fe.get_element('book_edit_position_4child', 'ExaminationPlaceRoom')
    # 通讯录编辑手机
    def get_book_edit_phone(self):
        return self.fe.get_element('book_edit_phone', 'ExaminationPlaceRoom')
    # 错误通讯录编辑手机提示语
    def get_book_edit_phone_error(self):
        return self.fe.get_element('book_edit_phone_error', 'ExaminationPlaceRoom')
    # 通讯录编辑固定电话
    def get_book_edit_tel(self):
        return self.fe.get_element('book_edit_tel', 'ExaminationPlaceRoom')
    # 错误通讯录编辑固定电话提示语

    def get_book_edit_tel_error(self):
        return self.fe.get_element('book_edit_tel_error', 'ExaminationPlaceRoom')
    # 通讯录编辑邮寄地址
    def get_book_edit_post_address(self):
        return self.fe.get_element('book_edit_post_address', 'ExaminationPlaceRoom')
    # 错误通讯录编辑邮寄地址提示语

    def get_book_edit_post_address_error(self):
        return self.fe.get_element('book_edit_post_address_error', 'ExaminationPlaceRoom')
    # 通讯录编辑电子邮箱
    def get_book_edit_mail(self):
        return self.fe.get_element('book_edit_mail', 'ExaminationPlaceRoom')
    # 错误讯录编辑电子邮箱提示语
    def get_book_edit_mail_error(self):
        return self.fe.get_element('book_edit_mail_error', 'ExaminationPlaceRoom')
    # 通讯录编辑qq
    def get_book_edit_qq(self):
        return self.fe.get_element('book_edit_qq', 'ExaminationPlaceRoom')
    # 删除通讯录按钮

    def get_book_delete_btn(self):
        return self.fe.get_element('book_delete_btn', 'ExaminationPlaceRoom')
    #确定删除按钮
    def get_book_confirm_delete_btn(self):
        return self.fe.get_element('book_confirm_delete_btn', 'ExaminationPlaceRoom')
    # 定位删除通讯录结果提示信息

    def get_delete_book_result(self):
        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div/span'))
        result=self.driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div/span')
        if result!=None:
            return result
        else:
            return None
    # 选择考点按钮
    def get_select_btn(self):
        return self.fe.get_element('select_btn', 'ExaminationPlaceRoom')

    # 获取选择考点框
    def get_select_text(self):
        return self.fe.get_element('select_text', 'ExaminationPlaceRoom')

    # 按照行政区划选择考点
    def get_select_place_by_divi(self):
        return self.fe.get_element('select_place_by_divi', 'ExaminationPlaceRoom')

    # 按照考点名称选择考点
    def get_select_place_by_name(self):
        return self.fe.get_element('select_place_by_name', 'ExaminationPlaceRoom')

    # 按照搜索条件选择考点
    def get_select_place_by_search(self):
        return self.fe.get_element('select_place_by_search', 'ExaminationPlaceRoom')

    # 按照搜索条件选择考点下拉框
    def get_select_place_by_search_btn(self):
        return self.fe.get_element('select_place_by_search_btn', 'ExaminationPlaceRoom')

    # 获取搜索条件选择考点下拉框第一个选项
    def select_place_by_search_fchild(self):
        return self.fe.get_element('select_place_by_search_fchild', 'ExaminationPlaceRoom')

    # 按照搜索条件选择考点下拉框第二个选项
    def select_place_by_search_schild(self):
        return self.fe.get_element('select_place_by_search_schild', 'ExaminationPlaceRoom')

    # 首字母导航
    def get_select_letter(self):
        return self.fe.get_element('select_letter', 'ExaminationPlaceRoom')


if __name__ == "__main__":
    lkc = LoginKeywordCases()
    lkc.run_keyword_excel_cases()
    driver = getattr(getattr(lkc, 'lk'), 'driver')
    Ep = ExaminationRoomPage(driver)
    EPp = ExaminationPlacePage(driver)
    driver.maximize_window()
    time.sleep(1)
    EPp.get_detailed_btn().click()
    time.sleep(1)
    print(Ep.get_basic_code().text)
