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
