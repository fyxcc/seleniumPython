#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time

from selenium.webdriver.support.wait import WebDriverWait
from basic.find_element import FindElement
from case.login_keyword_cases import LoginKeywordCases
from page.examination_place_page import ExaminationPlacePage


class ExaminationEnvironmentPage(object):
    # 初始化元素查找类，执行该类的时候就会加载
    def __init__(self, driver):
        self.driver = driver
        self.fe = FindElement(driver)

    #环境信息考点面积
    def get_place_area(self):
        return self.fe.get_element('place_area', 'ExaminationEnvironment')

    # 环境信息考场分布情况

    def get_place_spread(self):
        return self.fe.get_element('place_spread', 'ExaminationEnvironment')
    # 环境信息卫生间情况

    def get_toilet_condition(self):
        return self.fe.get_element('toilet_condition', 'ExaminationEnvironment')
    # 环境信息有无停车场

    def get_paking_condition(self):
        return self.fe.get_element('paking_condition', 'ExaminationEnvironment')
    # 环境信息车位数

    def get_cars_num(self):
        return self.fe.get_element('cars_num', 'ExaminationEnvironment')
    # 环境信息候选室

    def get_wating_room(self):
        return self.fe.get_element('wating_room', 'ExaminationEnvironment')
    # 环境信息考务办公室

    def get_examination_office(self):
        return self.fe.get_element('examination_office', 'ExaminationEnvironment')
    # 环境信息监控室

    def get_control_room(self):
        return self.fe.get_element('control_room', 'ExaminationEnvironment')
    # 环境信息滞留室

    def get_detention_chamber(self):
        return self.fe.get_element('detention_chamber', 'ExaminationEnvironment')
    # 环境信息保密室

    def get_confidential_room(self):
        return self.fe.get_element('confidential_room', 'ExaminationEnvironment')
    # 环境信息保险柜

    def get_safety_box(self):
        return self.fe.get_element('safety_box', 'ExaminationEnvironment')
    # 环境信息独立机房

    def get_independent_room(self):
        return self.fe.get_element('independent_room', 'ExaminationEnvironment')
    # 环境信息医疗箱

    def get_medkit(self):
        return self.fe.get_element('medkit', 'ExaminationEnvironment')