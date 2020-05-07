#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time

from selenium.webdriver.support.wait import WebDriverWait
from basic.find_element import FindElement
from case.login_keyword_cases import LoginKeywordCases
from page.examination_place_page import ExaminationPlacePage


class ExaminationEnvirPage(object):
    # 初始化元素查找类，执行该类的时候就会加载
    def __init__(self, driver):
        self.driver = driver
        self.fe = FindElement(driver)

    # 环境信息按钮
    def get_envir_btn(self):
        return self.fe.get_element('envir_btn', 'ExaminationEnvironment')

    # 环境信息编辑按钮
    def get_envir_edit_btn(self):
        return self.fe.get_element('envir_edit_btn', 'ExaminationEnvironment')
    # 环境信息编辑保存按钮
    def get_envir_edit_save_btn(self):
        return self.fe.get_element('envir_edit_save_btn', 'ExaminationEnvironment')
    # 环境信息编辑取消按钮
    def get_envir_edit_cancle_btn(self):
        return self.fe.get_element('envir_edit_cancle_btn', 'ExaminationEnvironment')
    #环境信息编辑成功信息
    def get_envir_edit_success(self):
        return self.fe.get_element('envir_edit_success', 'ExaminationEnvironment')

    # 环境信息编辑考点面积
    def get_envir_edit_place_area(self):
        return self.fe.get_element('envir_edit_place_area', 'ExaminationEnvironment')

    # 环境信息编辑考点面积错提示信息
    def get_envir_edit_place_area_error(self):
        return self.fe.get_element('envir_edit_place_area_error', 'ExaminationEnvironment')

    # 环境信息编辑考场分布情况
    def get_envir_edit_place_spread(self):
        return self.fe.get_element('envir_edit_place_spread', 'ExaminationEnvironment')

    # 环境信息编辑卫生间情况
    def get_envir_edit_toilet_conditio(self):
        return self.fe.get_element('envir_edit_toilet_condition', 'ExaminationEnvironment')

    # 环境信息编辑车位数
    def get_envir_edit_cars_num(self):
        return self.fe.get_element('envir_edit_cars_num', 'ExaminationEnvironment')
    # 环境信息编辑车位数错误信息
    def get_envir_edit_cars_num_error(self):
        return self.fe.get_element('envir_edit_cars_num_error', 'ExaminationEnvironment')
    # 环境编辑有无考场
    def get_envir_edit_paking_condition(self):
        return self.fe.get_element('envir_edit_paking_condition', 'ExaminationEnvironment')

    # 环境编辑有无候考室
    def get_envir_edit_wating_room(self):
        return self.fe.get_element('envir_edit_wating_room', 'ExaminationEnvironment')

    # 环境编辑有无考务办公室
    def get_envir_edit_examination_office(self):
        return self.fe.get_element('envir_edit_examination_office', 'ExaminationEnvironment')

    # 环境编辑有无监控室
    def get_envir_edit_control_room(self):
        return self.fe.get_element('envir_edit_control_room', 'ExaminationEnvironment')
    # 环境编辑有无滞留室
    def get_envir_edit_detention_chamber(self):
        return self.fe.get_element('envir_edit_detention_chamber', 'ExaminationEnvironment')
    # 环境编辑有无保密室
    def get_envir_edit_confidential_room(self):
        return self.fe.get_element('envir_edit_confidential_room', 'ExaminationEnvironment')
    # 环境编辑有无保险柜
    def get_envir_edit_safety_box(self):
        return self.fe.get_element('envir_edit_safety_box', 'ExaminationEnvironment')
    # 环境编辑有无独立机房
    def get_envir_edit_independent_room(self):
        return self.fe.get_element('envir_edit_independent_room', 'ExaminationEnvironment')
    # 环境编辑有无医疗箱
    def get_envir_edit_medkit(self):
        return self.fe.get_element('envir_edit_medkit', 'ExaminationEnvironment')
    # 环境信息考点面积
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

    # 机器设备金属探测仪
    def get_machine_metal_detector(self):
        return self.fe.get_element('machine_metal_detector', 'ExaminationEnvironment')

    # 机器设备信号屏蔽仪

    def get_machine_signal_shield(self):
        return self.fe.get_element('machine_signal_shield', 'ExaminationEnvironment')

    # 机器设备视频监控

    def get_machine_video_monitor(self):
        return self.fe.get_element('machine_video_monitor', 'ExaminationEnvironment')

    # 机器设备发电机

    def get_machine_gen(self):
        return self.fe.get_element('machine_gen', 'ExaminationEnvironment')

    # 机器设备双路电

    def get_machine_electricity(self):
        return self.fe.get_element('machine_electricity', 'ExaminationEnvironment')

    # 机器设备考试可用服务器数

    def get_machine_available_examination(self):
        return self.fe.get_element('machine_available_examination', 'ExaminationEnvironment')

    # 机器设备云桌面

    def get_machine_cloud_desktop(self):
        return self.fe.get_element('machine_cloud_desktop', 'ExaminationEnvironment')

    # 机器设备虚拟服务器

    def get_machine_virtual_server(self):
        return self.fe.get_element('machine_virtual_server', 'ExaminationEnvironment')

    # 机器设备处理器

    def get_machine_processor(self):
        return self.fe.get_element('machine_processor', 'ExaminationEnvironment')

    # 机器设备cpu型号

    def get_machine_cpu(self):
        return self.fe.get_element('machine_cpu', 'ExaminationEnvironment')

    # 机器设备内存

    def get_machine_storage(self):
        return self.fe.get_element('machine_storage', 'ExaminationEnvironment')

    # 机器设备硬盘

    def get_machine_caliche(self):
        return self.fe.get_element('machine_caliche', 'ExaminationEnvironment')

    # 机器设备网卡

    def get_machine_internet_card(self):
        return self.fe.get_element('machine_internet_card', 'ExaminationEnvironment')

    # 机器设备操作系统

    def get_machine_operating_system(self):
        return self.fe.get_element('machine_operating_system', 'ExaminationEnvironment')

    # 机器设备服务器ups

    def get_machine_ups(self):
        return self.fe.get_element('machine_ups', 'ExaminationEnvironment')

    # 机器设备服务器ups型号

    def get_machine_ups_model(self):
        return self.fe.get_element('machine_ups_model', 'ExaminationEnvironment')

    # 机器设备服务器ups供电时间

    def get_machine_ups_time(self):
        return self.fe.get_element('machine_ups_time', 'ExaminationEnvironment')

    # 机器设备服务器接入互联网

    def get_machine_insert(self):
        return self.fe.get_element('machine_insert', 'ExaminationEnvironment')

    # 机器设备是否互通

    def get_machine_interworking(self):
        return self.fe.get_element('machine_interworking', 'ExaminationEnvironment')

    # 机器设备网络带宽

    def get_machine_tape_width(self):
        return self.fe.get_element('machine_tape_width', 'ExaminationEnvironment')

    # 机器设备网络运营

    def get_machine_motion(self):
        return self.fe.get_element('machine_motion', 'ExaminationEnvironment')

    # 机器设备核心交换机型号

    def get_machine_center_switch_board(self):
        return self.fe.get_element('machine_center_switch_board', 'ExaminationEnvironment')

    # 机器设备接入层交换机型号

    def get_machine_insert_switch_board(self):
        return self.fe.get_element('machine_insert_switch_board', 'ExaminationEnvironment')

    # 机器设备网络架构

    def get_machine_framework(self):
        return self.fe.get_element('machine_framework', 'ExaminationEnvironment')

    # 照片
    def get_photo(self):
        return self.fe.get_element('photo', 'ExaminationEnvironment')

    # 照片标题
    def get_photo_title(self):
        return self.fe.get_element('photo_title', 'ExaminationEnvironment')

    # 照片简介
    def get_photo_content(self):
        return self.fe.get_element('photo_content', 'ExaminationEnvironment')


if __name__ == "__main__":
    lkc = LoginKeywordCases()
    lkc.run_keyword_excel_cases()
    driver = getattr(getattr(lkc, 'lk'), 'driver')
    Ep = ExaminationPlacePage(driver)
    driver.maximize_window()
