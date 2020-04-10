#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import unittest
from time import sleep

from basic.find_element import FindElement
from selenium import webdriver

from case.login_keyword_cases import LoginKeywordCases
import HTMLTestRunner


class ExaminationPlacePage(object):
    # 初始化元素查找类，执行该类的时候就会加载
    def __init__(self, driver):
        self.driver=driver
        self.fe = FindElement(driver)

    # 考点编号
    def get_place_code(self):
        return self.fe.get_element('place_code', 'ExaminationPlacePage')

    # 考点名称
    def get_place_name(self):
        return self.fe.get_element('place_name', 'ExaminationPlacePage')

    # 行政区划
    def get_place_division_code(self):
        return self.fe.get_element('place_division_code', 'ExaminationPlacePage')
    #行政区划市级子菜单
    def get_place_division_code_fchild(self):
        return self.fe.get_element('place_division_code_fchild', 'ExaminationPlacePage')
        # 行政区划市级子菜单

    def get_place_division_code_schild(self):
        return self.fe.get_element('place_division_code_schild', 'ExaminationPlacePage')
        # 行政区划市级子菜单

    def get_place_division_code_tchild(self):
        return self.fe.get_element('place_division_code_tchild', 'ExaminationPlacePage')
    # 考点地址
    def get_place_address(self):

        return self.fe.get_element('place_address', 'ExaminationPlacePage')

    # 考点负责人
    def get_place_person(self):
        return self.fe.get_element('place_person', 'ExaminationPlacePage')

    # 负责人联系电话
    def get_place_person_tel(self):
        return self.fe.get_element('place_person_tel', 'ExaminationPlacePage')

    # 状态
    def get_place_status(self):
        return self.fe.get_element('place_status', 'ExaminationPlacePage')
    # 状态值

    def get_place_status_value(self):
        return self.fe.get_element('place_status_value', 'ExaminationPlacePage')

    # 考点编号提示语
    def get_place_code_placeholder(self):
        print(self.fe.get_element('place_code', 'ExaminationPlacePage').get_attribute('placeholder'))
        return self.fe.get_element('place_code', 'ExaminationPlacePage').get_attribute('placeholder')

    # 考点名称提示语
    def get_place_name_placeholder(self):
        print(self.fe.get_element('place_name', 'ExaminationPlacePage').get_attribute('placeholder'))
        return self.fe.get_element('place_name', 'ExaminationPlacePage').get_attribute('placeholder')

    # 行政区划提示语
    def get_place_division_code_placeholder(self):
        print(self.fe.get_element('place_division_code', 'ExaminationPlacePage').get_attribute('placeholder'))
        return self.fe.get_element('place_division_code', 'ExaminationPlacePage').get_attribute('placeholder')

    # 考点地址提示语
    def get_place_address_placeholder(self):
        print(self.fe.get_element('place_address', 'ExaminationPlacePage').get_attribute('placeholder'))
        return self.fe.get_element('place_address', 'ExaminationPlacePage').get_attribute('placeholder')

    # 考点负责人提示语
    def get_place_person_placeholder(self):
        print(self.fe.get_element('place_person', 'ExaminationPlacePage').get_attribute('placeholder'))
        return self.fe.get_element('place_person', 'ExaminationPlacePage').get_attribute('placeholder')

    # 考点负责人联系电话提示语
    def get_place_person_tel_placeholder(self):
        print(self.fe.get_element('place_person_tel', 'ExaminationPlacePage').get_attribute('placeholder'))
        return self.fe.get_element('place_person_tel', 'ExaminationPlacePage').get_attribute('placeholder')

    # 确定添加按钮
    def get_confirm_add_btn(self):
        return self.fe.get_element('confirm_add_btn', 'ExaminationPlacePage')

    # 取消添加按钮
    def get_cancle_add_btn(self):
        return self.fe.get_element('cancle_add_btn', 'ExaminationPlacePage')

    # 添加按钮
    def get_add_btn(self):
        return self.fe.get_element('add_btn', 'ExaminationPlacePage')

    # 不合法考点编号提示语
    def get_place_code_error(self):
        return self.fe.get_element('place_code_error', 'ExaminationPlacePage')

    # 不合法考点名称示语
    def get_place_name_error(self):
        return self.fe.get_element('place_name_error', 'ExaminationPlacePage')

    # 不合法行政区划提示语
    def get_place_division_code_error(self):
        return self.fe.get_element('place_division_code_error', 'ExaminationPlacePage')

    # 不合法考点地址提示语
    def get_place_address_error(self):
        return self.fe.get_element('place_address_error', 'ExaminationPlacePage')

    # 不合法考点负责人划提示语
    def get_place_person_error(self):
        return self.fe.get_element('place_person_error', 'ExaminationPlacePage')

    # 不合法负责人联系电话提示语
    def get_place_person_tel_error(self):
        return self.fe.get_element('place_person_tel_error', 'ExaminationPlacePage')

    # 添加验证通过提示语
    def get_verify_login_error(self):
        return self.fe.get_element('verify_login_error', 'ExaminationPlacePage')

    # 添加验证不通过提示语
    def get_verify_login_error(self):
        return self.fe.get_element('verify_login_error', 'ExaminationPlacePage')
    #添加成功提示语
    def add_success(self):
        return self.fe.get_element('add_success','ExaminationPlacePage')


if __name__ == "__main__":
    lkc = LoginKeywordCases()
    lkc.run_keyword_excel_cases()

    Ep = ExaminationPlacePage(getattr(getattr(lkc, 'lk'), 'driver'))
    sleep(3)
    Ep.get_add_btn().click()
    sleep(3)

    Ep.get_confirm_add_btn().click()
    print(Ep.get_place_address_error().text)
'''
    Ep.get_place_code_placeholder()
    Ep.get_place_address_placeholder()
    Ep.get_place_name_placeholder()
    Ep.get_place_person_placeholder()
    Ep.get_place_person_tel_placeholder()'''
    # Ep.get_place_address_placeholder()
