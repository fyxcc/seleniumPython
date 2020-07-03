# coding=utf-8
import win32api
import win32con
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from page.examination_envir_page import ExaminationEnvirPage
import time
from case.login_keyword_cases import LoginKeywordCases
from handle.examination_place_handle import ExaminationPlaceHandle
from handle.examination_room_handle import ExaminationRoomHandle
from util.table_util import TableUtil
from PIL import Image, ImageGrab
from util.excel_util import ExcelUtil
from util.image_match.image_match import ImageMatch
from util.image_match.action_execute import ActionExecute
from util.image_match_sift.image_match_by_sift import ImageMatchBySift
from util.image_match_sift.action_exe import ActionExe


class ExaminationeEnvirHandle(object):
    def __init__(self, driver):
        self.driver = driver
        self.Eep = ExaminationEnvirPage(self.driver)
        self.Tu = TableUtil(self.driver)

    # 点击环境信息按钮
    def click_envir_btn(self):
        return self.Eep.get_envir_btn().click()

    # 点击环境信息编辑按钮
    def click_envir_edit_btn(self):
        return self.Eep.get_envir_edit_btn().click()

    # 点击环境信息编辑保存按钮
    def click_envir_edit_save_btn(self):
        return self.Eep.get_envir_edit_save_btn().click()

    # 点击环境信息编辑保取消按钮
    def click_envir_edit_cancle_btn(self):
        return self.Eep.get_envir_edit_cancle_btn().click()

    # 清空环境信息编辑考点面积
    def clear_envir_edit_place_area(self):
        element = self.Eep.get_envir_edit_place_area()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 输入环境信息编辑考点面积

    def send_envir_edit_place_area(self, envir_edit_place_area):
        if len(envir_edit_place_area) != 0:
            self.Eep.get_envir_edit_place_area().send_keys(envir_edit_place_area)

    # 清空环境信息编辑考场分布情况
    def clear_envir_edit_place_spread(self):
        element = self.Eep.get_envir_edit_place_spread()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 输入环境信息编辑考场分布情况

    def send_envir_edit_place_spread(self, envir_edit_place_spread):
        if len(envir_edit_place_spread) != 0:
            self.Eep.get_envir_edit_place_spread().send_keys(envir_edit_place_spread)

    # 清空环境信息编辑车位数
    def clear_envir_edit_cars_num(self):
        element = self.Eep.get_envir_edit_cars_num()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 输入环境信息编辑车位数

    def send_envir_edit_cars_num(self, envir_edit_cars_num):
        if len(envir_edit_cars_num) != 0:
            self.Eep.get_envir_edit_cars_num().send_keys(envir_edit_cars_num)

    # 清空环境信息编辑卫生间情况
    def clear_envir_edit_toilet_condition(self):
        element = self.Eep.get_envir_edit_toilet_conditio()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 输入环境信息编辑卫生间情况

    def send_envir_edit_toilet_condition(self, envir_edit_toilet_condition):
        if len(envir_edit_toilet_condition) != 0:
            self.Eep.get_envir_edit_cars_num().send_keys(envir_edit_toilet_condition)

    # 编辑考场环境信息有无停车场内容
    def get_envir_edit_paking_condition_text(self):
        return self.Eep.get_envir_edit_paking_condition().text

    # 编辑考场环境信息有无候考室内容
    def get_envir_edit_wating_room_text(self):
        return self.Eep.get_envir_edit_wating_room().text

    # 编辑考场环境信息有无考务办公室内容
    def get_envir_edit_examination_office_text(self):
        return self.Eep.get_envir_edit_examination_office().text

    # 编辑考场环境信息有无监控室内容
    def get_envir_edit_control_room_text(self):
        return self.Eep.get_envir_edit_control_room().text

    # 编辑考场环境信息有无滞留室内容
    def get_envir_edit_detention_chamber_text(self):
        return self.Eep.get_envir_edit_detention_chamber().text

    # 编辑考场环境信息有无保密室内容
    def get_envir_edit_confidential_room_text(self):
        return self.Eep.get_envir_edit_confidential_room().text

    # 编辑考场环境信息有无保险柜内容
    def get_envir_edit_safety_box_text(self):
        return self.Eep.get_envir_edit_safety_box().text

    # 编辑考场环境信息有无独立机房内容
    def get_envir_edit_independent_room_text(self):
        return self.Eep.get_envir_edit_independent_room().text

    # 编辑考场环境信息有无医疗箱内容
    def get_envir_edit_medkit_text(self):
        return self.Eep.get_envir_edit_medkit().text

    # 获取环境信息编辑错误信息

    def get_envir_edit_error_text(self, error_info, assertText):
        try:

            if error_info == 'envir_edit_place_area_error':
                text_content = self.Eep.get_envir_edit_place_area_error().text
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'envir_edit_cars_num_error':
                text_content = self.Eep.get_envir_edit_cars_num_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == '所有输入条件为空':
                time.sleep(1)
                result = self.Eep.get_envir_edit_success()
                resultText = result.text
                if resultText == assertText:
                    text = 'ok'
            return text
        except BaseException as e:
            print(repr(e))
            return None

    # 获取环境信息考点面积字段
    def get_place_area_text(self):
        return self.Eep.get_place_area().text

    # 获取环境信息考场分布情况字段
    def get_place_spread_text(self):
        return self.Eep.get_place_spread().text

    # 获取环境信息卫生间情况字段
    def get_toilet_condition_text(self):
        return self.Eep.get_toilet_condition().text

    # 获取环境信息有无停车场字段
    def get_paking_condition_text(self):
        return self.Eep.get_paking_condition().text

    # 获取环境信息车位数字段
    def get_cars_num_text(self):
        return self.Eep.get_cars_num().text

    # 获取环境信息候选室字段
    def get_wating_room_text(self):
        return self.Eep.get_wating_room().text

    # 获取环境信息考务办公室字段
    def get_examination_office_text(self):
        return self.Eep.get_examination_office().text

    # 获取环境信息监控室字段
    def get_control_room_text(self):
        return self.Eep.get_control_room().text

    # 获取环境信息滞留室字段
    def get_detention_chamber_text(self):
        return self.Eep.get_detention_chamber().text

    # 获取环境信息保密室字段
    def get_confidential_room_text(self):
        return self.Eep.get_confidential_room().text

    # 获取环境信息保险柜字段
    def get_safety_box_text(self):
        return self.Eep.get_safety_box().text

    # 获取环境信息独立机房字段
    def get_independent_room_text(self):
        return self.Eep.get_independent_room().text

    # 获取环境信息医疗箱字段
    def get_medkit_text(self):
        return self.Eep.get_medkit().text

    # 判断环境信息是否完整
    def judge_envir_complete(self):
        area = self.get_place_area_text()
        apread = self.get_place_spread_text()
        toilet_condition = self.get_toilet_condition_text()
        paking_condition = self.get_paking_condition_text()
        cars_num = self.get_cars_num_text()
        wating_room = self.get_wating_room_text()
        examination_office = self.get_examination_office_text()
        control_room = self.get_control_room_text()
        detention_chamber = self.get_detention_chamber_text()
        confidential_room = self.get_confidential_room_text()
        safety_box = self.get_safety_box_text()
        independent_room = self.get_independent_room_text()
        medkit = self.get_medkit_text()
        if area != None and apread != None and toilet_condition != None and paking_condition != None and cars_num != None and wating_room != None and examination_office != None and control_room != None and detention_chamber != None and confidential_room != None and safety_box != None and independent_room != None and medkit != None:
            return True
        else:
            return False

    # 点击机器设备编辑按钮
    def click_machine_edit_btn(self):
        return self.Eep.get_machine_edit_btn().click()

    # 点击机器设备编辑保存按钮
    def click_machine_edit_save_btn(self):
        return self.Eep.get_machine_edit_save_btn().click()

    # 点击机器设备编辑取消按钮
    def click_machine_edit_cancle_btn(self):
        return self.Eep.get_machine_edit_cancle_btn().click()

    # 获取机器设备编辑成功消息内容
    def get_machine_edit_success_text(self):
        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath('/html/body/div[6]/div/div'))
        text_content = self.driver.find_element_by_xpath('/html/body/div[6]/div/div').text
        return text_content

    # 获取环境信息编辑错误信息

    def get_machine_edit_error_text(self, error_info, assertText):
        try:

            if error_info == 'machine_edit_available_examination_error':
                text_content = self.get_machine_edit_available_examination_error_text()
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'machine_edit_processor_error':
                text_content = self.get_machine_edit_processor_error_text()
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'machine_edit_storage_error':
                text_content = self.get_machine_edit_storage_error_text()
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'machine_edit_caliche_error':
                text_content = self.get_machine_edit_caliche_error_text()
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'machine_edit_ups_model_error':
                text_content = self.get_machine_edit_ups_model_error_text()
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'machine_edit_ups_time_error':
                text_content = self.get_machine_edit_ups_time_error_text()
                if text_content == assertText:
                    text = 'ok'


            elif error_info == '所有输入条件为空':
                time.sleep(1)
                result = self.Eep.get_envir_edit_success()
                resultText = result.text
                if resultText == assertText:
                    text = 'ok'
            return text
        except BaseException as e:
            print(repr(e))
            return None

    # 机器设备编辑金属探测仪字段

    def get_machine_edit_metal_detector_text(self):
        return self.Eep.get_machine_edit_metal_detector().text

    # 机器设备编辑信号屏蔽仪字段

    def get_machine_edit_signal_shield_text(self):
        return self.Eep.get_machine_edit_signal_shield().text

    # 机器设备编辑视频监控字段

    def get_machine_edit_video_monitor_text(self):
        return self.Eep.get_machine_edit_video_monitor().text

    # 机器设备编辑发电机字段

    def get_machine_edit_gen_text(self):
        return self.Eep.get_machine_edit_gen().text

    # 机器设备编辑双路电字段

    def get_machine_edit_electricity_text(self):
        return self.Eep.get_machine_edit_electricity().text

    # 机器设备编辑云桌面字段

    def get_machine_edit_cloud_desktop_text(self):
        return self.Eep.get_machine_edit_cloud_desktop().text

    # 机器设备编辑虚拟服务器字段

    def get_machine_edit_virtual_server_text(self):
        return self.Eep.get_machine_edit_virtual_server().text

    # 输入机器设备编辑考试可用服务器数

    def send_machine_edit_available_examination(self, machine_edit_available_examination):
        if len(machine_edit_available_examination) != 0:
            self.Eep.get_machine_edit_available_examination().send_keys(machine_edit_available_examination)

    # 获取机器设备编辑考试可用服务器数错误提示信息

    def get_machine_edit_available_examination_error_text(self):
        return self.Eep.get_machine_edit_available_examination_error().text

    # 清空机器设备编辑考试可用服务器数字段
    def clear_machine_edit_available_examination(self):
        element = self.Eep.get_machine_edit_available_examination()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 点击处理器下拉框
    def click_machine_edit_processor_select(self):
        return self.Eep.get_machine_edit_processor_select().click()

    # 点击处理器下拉框1
    def get_machine_edit_processor_select1_text(self):
        return self.Eep.get_machine_edit_processor_select1().text

    # 点击处理器下拉框2
    def get_machine_edit_processor_select2_text(self):
        return self.Eep.get_machine_edit_processor_select2().text

    # 点击处理器下拉框3
    def get_machine_edit_processor_select3_text(self):
        return self.Eep.get_machine_edit_processor_select3().text

    # 点击处理器下拉框4
    def get_machine_edit_processor_select4_text(self):
        return self.Eep.get_machine_edit_processor_select4().text

    # 点击处理器下拉框5
    def get_machine_edit_processor_select5_text(self):
        return self.Eep.get_machine_edit_processor_select5().text

    # 点击处理器下拉框6
    def get_machine_edit_processor_select6_text(self):
        return self.Eep.get_machine_edit_processor_select6().text

    # 点击处理器下拉框7
    def get_machine_edit_processor_select7_text(self):
        return self.Eep.get_machine_edit_processor_select7().text

    # 输入机器设备编辑处理器字段

    def send_machine_edit_processor(self, machine_edit_processor):
        if len(machine_edit_processor) != 0:
            self.Eep.get_machine_edit_processor().send_keys(machine_edit_processor)

    # 获取机器设备编处理器错误提示信息
    def get_machine_edit_processor_error_text(self):
        return self.Eep.get_machine_edit_processor_error().text

    # 清空机器设备处理器字段

    def clear_machine_edit_processor(self):
        element = self.Eep.get_machine_edit_processor()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 获取网卡1
    def get_machine_edit_internet_card1_text(self):
        return self.Eep.get_machine_edit_internet_card1().text

    # 获取网卡2
    def get_machine_edit_internet_card2_text(self):
        return self.Eep.get_machine_edit_internet_card2().text

    # 获取网卡3
    def get_machine_edit_internet_card3_text(self):
        return self.Eep.get_machine_edit_internet_card3().text

    # 输入机器设备编辑内存

    def send_machine_edit_storage(self, machine_edit_storage):
        if len(machine_edit_storage) != 0:
            self.Eep.get_machine_edit_storage().send_keys(machine_edit_storage)

    # 获取机器设备编辑内存错误提示信息
    def get_machine_edit_storage_error_text(self):
        return self.Eep.get_machine_edit_storage_error().text

    # 清空机器设备编辑内存
    def clear_machine_edit_storage(self):
        element = self.Eep.get_machine_edit_storage()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 输入机器设备编辑硬盘

    def send_machine_edit_caliche(self, machine_edit_caliche):
        if len(machine_edit_caliche) != 0:
            self.Eep.get_machine_edit_caliche().send_keys(machine_edit_caliche)

    # 获取机器设备编辑硬盘错误提示信息
    def get_machine_edit_caliche_error_text(self):
        return self.Eep.get_machine_edit_caliche_error().text

    # 清空机器设备编辑硬盘
    def clear_machine_edit_caliche(self):
        element = self.Eep.get_machine_edit_caliche()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 点击操作系统下拉框
    def click_machine_edit_operating_system(self):
        return self.Eep.get_machine_edit_operating_system().click()

    # 点击操作系统下拉框1
    def get_machine_edit_operating_system1_text(self):
        return self.Eep.get_machine_edit_operating_system1().text

    # 点击操作系统下拉框2
    def get_machine_edit_operating_system2_text(self):
        return self.Eep.get_machine_edit_operating_system2().text

    # 点击操作系统下拉框3
    def get_machine_edit_operating_system3_text(self):
        return self.Eep.get_machine_edit_operating_system3().text

    # 点击操作系统下拉框4
    def get_machine_edit_operating_system4_text(self):
        return self.Eep.get_machine_edit_operating_system4().text

    # 点击操作系统下拉框5
    def get_machine_edit_operating_system5_text(self):
        return self.Eep.get_machine_edit_operating_system5().text

    # 点击操作系统下拉框6
    def get_machine_edit_operating_system6_text(self):
        return self.Eep.get_machine_edit_operating_system6().text

    # 机器设备编辑服务器ups字段

    def get_machine_edit_ups_text(self):
        return self.Eep.get_machine_edit_ups().text

    # 输入机器设备编辑服务器ups型号字段

    def send_machine_edit_ups_model(self, machine_edit_ups_model):
        if len(machine_edit_ups_model) != 0:
            self.Eep.get_machine_edit_ups_model().send_keys(machine_edit_ups_model)

    # 获取机器设备编辑服务器ups型号错误提示信息
    def get_machine_edit_ups_model_error_text(self):
        return self.Eep.get_machine_edit_ups_model_error().text

    # 清空机器设备编辑服务器ups型号字段

    def clear_machine_edit_ups_model(self):
        element = self.Eep.get_machine_edit_ups_model()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 机器设备编辑服务器接入互联网字段

    def get_machine_edit_insert_text(self):
        return self.Eep.get_machine_edit_insert().text

    # 输入机器设备编辑服务器ups供电时间字段

    def send_machine_edit_ups_time(self, machine_edit_ups_time):
        if len(machine_edit_ups_time) != 0:
            self.Eep.get_machine_edit_ups_time().send_keys(machine_edit_ups_time)

    # 获取机器设备编辑服务器ups供电时间错误提示信息
    def get_machine_edit_ups_time_error_text(self):
        return self.Eep.get_machine_edit_ups_time_error().text

    # 清空机器设备编辑服务器ups供电时间字段

    def clear_machine_edit_ups_time(self):
        element = self.Eep.get_machine_edit_ups_time()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 机器设备编辑是否互通字段

    def get_machine_edit_interworking_text(self):
        return self.Eep.get_machine_edit_interworking().text

    # 点击机器设备编辑网络带宽

    def click_machine_edit_tape_width_text(self):
        return self.Eep.get_machine_edit_tape_width().click()

    # 机器设备编辑网络带宽1

    def get_machine_edit_tape_width1_text(self):
        return self.Eep.get_machine_edit_tape_width1().text

    # 机器设备编辑网络带宽2

    def get_machine_edit_tape_width2_text(self):
        return self.Eep.get_machine_edit_tape_width2().text

    # 机器设备编辑网络带宽3

    def get_machine_edit_tape_width3_text(self):
        return self.Eep.get_machine_edit_tape_width3().text

    # 点击机器设备编辑网络运营

    def click_get_machine_motion_select(self):
        return self.Eep.get_machine_motion_select().click()

    # 机器设备编辑网络运营1
    def get_machine_motion_select1_text(self):
        return self.Eep.get_machine_motion_select1().text

    # 机器设备编辑网络运营2

    def get_machine_motion_select2_text(self):
        return self.Eep.get_machine_motion_select2().text
        # 机器设备编辑网络运营1

    def get_machine_motion_select3_text(self):
        return self.Eep.get_machine_motion_select3().text
        # 机器设备编辑网络运营1

    def get_machine_motion_select4_text(self):
        return self.Eep.get_machine_motion_select4().text
        # 机器设备编辑网络运营1

    def get_machine_motion_select5_text(self):
        return self.Eep.get_machine_motion_select5().text
        # 机器设备编辑网络运营1

    def get_machine_motion_select6_text(self):
        return self.Eep.get_machine_motion_select6().text
        # 机器设备编辑网络运营1

    def get_machine_motion_select7_text(self):
        return self.Eep.get_machine_motion_select7().text

    # 输入机器设备编辑核心交换机型号字段

    def send_machine_edit_center_switch_board(self, machine_edit_center_switch_board):
        if len(machine_edit_center_switch_board) != 0:
            self.Eep.get_machine_edit_center_switch_board().send_keys(machine_edit_center_switch_board)

    # 清空机器设备编辑核心交换机型号字段

    def clear_machine_edit_center_switch_board(self):
        element = self.Eep.get_machine_edit_center_switch_board()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 输入机器设备编辑接入层交换机型号字段

    def send_machine_edit_insert_switch_board(self, machine_edit_insert_switch_board):
        if len(machine_edit_insert_switch_board) != 0:
            self.Eep.get_machine_edit_insert_switch_board().send_keys(machine_edit_insert_switch_board)

    # 清空机器设备编辑接入层交换机型号字段

    def clear_machine_edit_insert_switch_board(self):
        element = self.Eep.get_machine_edit_insert_switch_board()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 输入机器设备编辑网络架构字段

    def send_machine_edit_framework(self, machine_edit_framework):
        if len(machine_edit_framework) != 0:
            self.Eep.get_machine_edit_framework().send_keys(machine_edit_framework)

    # 清空机器设备编辑网络架构字段

    def clear_machine_edit_framework(self):
        element = self.Eep.get_machine_edit_framework()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 获取机器设备金属探测仪字段
    def get_machine_metal_detector_text(self):
        return self.Eep.get_machine_metal_detector().text

    # 获取机器设备信号屏蔽仪字段

    def get_machine_signal_shield_text(self):
        return self.Eep.get_machine_signal_shield().text

    # 获取机器设备视频监控字段

    def get_machine_video_monitor_text(self):
        return self.Eep.get_machine_video_monitor().text

    # 获取机器设备发电机字段

    def get_machine_gen_text(self):
        return self.Eep.get_machine_gen().text

    # 获取机器设备双路电字段

    def get_machine_electricity_text(self):
        return self.Eep.get_machine_electricity().text

    # 获取机器设备考试可用服务器数字段

    def get_machine_available_examination_text(self):
        return self.Eep.get_machine_available_examination().text

    # 获取机器设备云桌面字段

    def get_machine_cloud_desktop_text(self):
        return self.Eep.get_machine_cloud_desktop().text

    # 获取 机器设备虚拟服务器字段

    def get_machine_virtual_server_text(self):
        return self.Eep.get_machine_virtual_server().text

    # 获取机器设备处理器字段

    def get_machine_processor_text(self):
        return self.Eep.get_machine_processor().text

    # 获取机器设备cpu型号字段

    def get_machine_cpu_text(self):
        return self.Eep.get_machine_cpu().text

    # 获取机器设备内存字段

    def get_machine_storage_text(self):
        return self.Eep.get_machine_storage().text

    # 获取机器设备硬盘字段

    def get_machine_caliche_text(self):
        return self.Eep.get_machine_caliche().text

    # 获取机器设备网卡字段

    def get_machine_internet_card_text(self):
        return self.Eep.get_machine_internet_card().text

    # 获取机器设备操作系统字段

    def get_machine_operating_system_text(self):
        return self.Eep.get_machine_operating_system().text

    # 获取机器设备服务器ups字段

    def get_machine_ups_text(self):
        return self.Eep.get_machine_ups().text

    # 获取机器设备服务器ups型号字段

    def get_machine_ups_model_text(self):
        return self.Eep.get_machine_ups_model().text

    # 获取机器设备服务器ups供电时间字段

    def get_machine_ups_time_text(self):
        return self.Eep.get_machine_ups_time().text

    # 获取机器设备服务器接入互联网字段

    def get_machine_insert_text(self):
        return self.Eep.get_machine_insert().text

    # 获取机器设备是否互通字段

    def get_machine_interworking_text(self):
        return self.Eep.get_machine_interworking().text

    # 获取机器设备网络带宽字段

    def get_machine_tape_width_text(self):
        return self.Eep.get_machine_tape_width().text

    # 获取机器设备网络运营字段

    def get_machine_motion_text(self):
        return self.Eep.get_machine_motion().text

    # 获取机器设备核心交换机型号字段

    def get_machine_center_switch_board_text(self):
        return self.Eep.get_machine_center_switch_board().text

    # 获取机器设备接入层交换机型号字段
    def get_machine_insert_switch_board_text(self):
        return self.Eep.get_machine_insert_switch_board().text

    # 获取机器设备网络架构字段

    def get_machine_framework_text(self):
        return self.Eep.get_machine_framework().text

    # 判断机器设备信息是否完整
    def judge_machine_complete(self):
        data1 = self.get_machine_metal_detector_text()
        data2 = self.get_machine_signal_shield_text()
        data3 = self.get_machine_video_monitor_text()
        data4 = self.get_machine_gen_text()
        data5 = self.get_machine_electricity_text()
        data6 = self.get_machine_available_examination_text()
        data7 = self.get_machine_cloud_desktop_text()
        data8 = self.get_machine_virtual_server_text()
        data9 = self.get_machine_processor_text()
        data10 = self.get_machine_cpu_text()
        data11 = self.get_machine_storage_text()
        data12 = self.get_machine_caliche_text()
        data13 = self.get_machine_internet_card_text()
        data14 = self.get_machine_operating_system_text()
        data15 = self.get_machine_ups_text()
        data16 = self.get_machine_ups_model_text()
        data17 = self.get_machine_ups_time_text()
        data18 = self.get_machine_insert_text()
        data19 = self.get_machine_interworking_text()
        data20 = self.get_machine_tape_width_text()
        data21 = self.get_machine_motion_text()
        data22 = self.get_machine_center_switch_board_text()
        data23 = self.get_machine_insert_switch_board_text()
        data24 = self.get_machine_framework_text()
        if data1 != None and data2 != None and data3 != None and data4 != None and data5 != None and data6 != None and data7 != None and data8 != None and data9 != None and data10 != None and data11 != None and data12 != None and data13 != None and data14 != None and data15 != None and data16 != None and data17 != None and data18 != None and data19 != None and data20 != None and data21 != None and data22 != None and data23 != None and data23 != None:
            return True
        else:
            return False

    # 获取照片添加成功消息内容
    def get_photo_add_result_text(self):
        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/span'))
        text_content = self.driver.find_element_by_xpath('/html/body/div[6]/div/div').text
        return text_content

    # 获取照片标题字段

    def get_photo_title_text(self):
        if self.Eep.get_photo_title() != None:
            return self.Eep.get_photo_title().text
        else:
            return None

    # 获取照片简介字段

    def get_photo_content_text(self):
        if self.Eep.get_photo_content() != None:
            return self.Eep.get_photo_content().text
        else:
            return None

    # 点击照片编辑按钮
    def click_photo_edit_btn(self):
        return self.Eep.get_photo_edit_btn().click()

    # 获取照片编辑标题内容
    def get_photo_edit_title_text(self):
        return self.Eep.get_photo_edit_title().get_attribute('value')

    # 获取照片编辑简介内容

    def get_photo_edit_content_text(self):
        return self.Eep.get_photo_edit_content().get_attribute('value')

    # 判断照片完整性
    def judge_photo_complete(self):
        data1 = self.Eep.get_photo()
        data2 = self.get_photo_title_text()
        data3 = self.get_photo_content_text()
        data4 = self.Eep.get_upload_photo_btn()
        data5 = self.Eep.get_photo_edit_btn()
        data6 = self.Eep.get_photo_delete_btn()
        if data1 != None and data2 != None and data3 != None and data4 != None and data5 != None and data6 != None:
            return True
        else:
            return False

    # 点击照片添加按钮
    def click_photo_add_btn(self):
        element = self.Eep.get_photo_add_btn()
        if element != None:
            return element.click()

    # 点击照片浏览按钮
    def click_photo_add_browse_btn(self):
        return self.Eep.get_photo_add_browse_btn().click()

    # 获取照片弹框信息内容
    def get_photo_add_frame_text(self):
        element = self.Eep.get_photo_add_frame()
        if element != None:
            return element.text
        else:
            return None

    # 点击照片添加确定按钮
    def click_photo_add_save_btn(self):
        return self.Eep.get_photo_add_save_btn().click()

    # 点击照片添加取消按钮


    def click_add_cancle_btn(self):
        return self.Eep.get_photo_add_cancle_btn().click()

    # 点击照片删除按钮

    def click_photo_dele_btn(self):
        return self.Eep.get_photo_dele_btn().click()

    # 点击照片删除确定按钮
    def click_photo_delete_confirm_btn(self):
        return self.Eep.get_photo_delete_confirm_btn().click()

    # 获取照片添加照片错误信息内容
    def get_photo_add_browse_error_text(self):
        self.Eep.get_photo_add_browse_error().text

    # 浏览上传考点照片文件路径字段(通过模板匹配)

    def browse_photo_add_photo_path(self, photo_path, photo_name, screen_capture):
        # 点击浏览按钮
        self.click_photo_add_browse_btn()
        time.sleep(2)
        # 实例化图像匹配类
        IM = ImageMatch()
        # 实例化控件操作类
        AE = ActionExecute()
        # 截取当前页面
        im = ImageGrab.grab()
        # 保存截取页面到固定路径
        im.save(screen_capture)
        # 读入数据
        ex = ExcelUtil(excel_path=r"D:\pythonWork\autoTest\data\examinationPhotoImageMatchData.xls")
        # 获取excel行数
        rows = ex.get_lines()
        # 循环获取excel模板图数据
        for row in range(0, rows):
            # 获取模板图
            function_photo = ex.get_col_value(row, 2)
            # 获取模板图处执行方法
            operate_method = ex.get_col_value(row, 3)
            # 引入模板匹配模块
            operate_location = IM.ImageMatch(function_photo, screen_capture)
            operate_location_x = int(operate_location[0])
            operate_location_y = int(operate_location[1])
            if operate_location != None:
                # 鼠标定位到识别元素位置
                win32api.SetCursorPos([operate_location_x, operate_location_y])
                # 鼠标左击
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                time.sleep(2)
                # 鼠标右击
                # win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                # 将内容复制到剪切板里
                AE.add_to_clipboard(photo_name)
                # 获取剪切板的内容
                # AE.get_clipboard()
                # 执行ctrl+v
                if row == 0:
                    AE.paste_method()
                time.sleep(3)

    # 浏览上传考点照片文件路径字段(通过sift匹配)

    def  browse_photo_add_photo_path_sift(self, photo_path, photo_name, screen_capture):
        # 点击浏览按钮
        self.click_photo_add_browse_btn()
        time.sleep(2)
        # 实例化图像匹配类
        IM = ImageMatchBySift()
        # 实例化控件操作类
        AE = ActionExe()
        # 截取当前页面
        im = ImageGrab.grab()
        # 保存截取页面到固定路径
        im.save(screen_capture)
        # 读入数据
        ex = ExcelUtil(excel_path=r"D:\pythonWork\autoTest\data\examinationPhotoImageMatchData.xls")
        # 获取excel行数
        rows = ex.get_lines()
        # 循环获取excel模板图数据
        for row in range(0, rows):
            # 获取模板图
            function_photo = ex.get_col_value(row, 2)
            # 获取模板图处执行方法
            operate_method = ex.get_col_value(row, 3)
            # 引入模板匹配模块
            operate_location = IM.image_match_by_sift(function_photo, screen_capture)
            operate_location_x = int(operate_location[0])
            operate_location_y = int(operate_location[1])
            if operate_location != None:
                # 鼠标定位到识别元素位置
                win32api.SetCursorPos([operate_location_x, operate_location_y])
                # 鼠标左击
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                # 鼠标右击
                # win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                time.sleep(3)
                if row == 0:
                    # 将内容复制到剪切板里
                    AE.add_to_clipboard(photo_name)
                    # 获取剪切板的内容
                    yi = AE.get_clipboard()
                    # 执行ctrl+v
                    AE.paste_method()
                    time.sleep(3)
    def  browse_photo_add_photo_path_sift_demo(self, photo_path, photo_name, screen_capture):
        # 点击浏览按钮
        self.click_photo_add_browse_btn()
        time.sleep(2)
        # 实例化图像匹配类
        IM = ImageMatchBySift()
        # 实例化控件操作类
        AE = ActionExe()
        # 读入数据
        ex = ExcelUtil(excel_path=r"D:\pythonWork\autoTest\data\picturedemo.xls")
        # 获取excel行数
        rows = ex.get_lines()
        # 循环获取excel模板图数据
        for row in range(0, rows):
            # 获取模板图
            function_photo = ex.get_col_value(row, 2)
            # 获取模板图处执行方法
            operate_method = ex.get_col_value(row, 3)
            # 截取当前页面
            im = ImageGrab.grab()
            # 保存截取页面到固定路径
            im.save(screen_capture)
            # 引入模板匹配模块
            operate_location = IM.image_match_by_sift(function_photo, screen_capture)
            operate_location_x = int(operate_location[0])
            operate_location_y = int(operate_location[1])
            if operate_location != None:
                # 鼠标定位到识别元素位置
                win32api.SetCursorPos([operate_location_x, operate_location_y])
                # 鼠标左击
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                # 鼠标右击
                # win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                time.sleep(3)
                """if row == 0:
                    # 将内容复制到剪切板里
                    AE.add_to_clipboard(photo_name)
                    # 获取剪切板的内容
                    yi = AE.get_clipboard()
                    # 执行ctrl+v
                    AE.paste_method()
                    time.sleep(3)"""


    # 清空考点照片照片标题字段
    def clear_photo_add_title(self):
        element = self.Eep.get_photo_add_title()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 输入考点照片照片标题字段

    def send_photo_add_title(self, photo_add_title):
        if len(photo_add_title) != 0:
            self.Eep.get_photo_add_title().send_keys(photo_add_title)

    # 清空考点照片照片简介字段
    def clear_photo_add_content(self):
        element = self.Eep.get_photo_add_content()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 获取考点照片照片标题字段错误信息

    def get_photo_add_title_error_text(self):
        return self.Eep.get_photo_add_title_error().text

    # 输入考点照片照片简介字段

    def send_photo_add_content(self, photo_add_content):
        if len(photo_add_content) != 0:
            self.Eep.get_photo_add_content().send_keys(photo_add_content)

    # 获取考点照片照片简介字段错误信息

    def get_photo_add_content_error_text(self):
        return self.Eep.get_photo_add_content_error().text

    # 获取环境信息编辑错误信息

    def get_photo_add_error_text(self, error_info, assertText):
        try:
            if error_info == 'photo_add_browse_error':
                text_content = self.get_photo_add_browse_error_text()
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'photo_add_title_error':
                text_content = self.get_photo_add_title_error_text()
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'photo_add_content_error':
                text_content = self.get_photo_add_content_error_text()
                if text_content == assertText:
                    text = 'ok'
            return text
        except BaseException as e:
            print(repr(e))
            return None


if __name__ == "__main__":
    lkc = LoginKeywordCases()
    lkc.run_keyword_excel_cases()
    driver = getattr(getattr(lkc, 'lk'), 'driver')
    driver.maximize_window()
    EPh = ExaminationPlaceHandle(driver)
    Eeh = ExaminationeEnvirHandle(driver)
    EPh.click_detailed_btn()
    time.sleep(1)
    Eeh.click_envir_btn()
    time.sleep(1)
    Eeh.click_envir_edit_btn()
    time.sleep(1)
    print(Eeh.get_envir_edit_paking_condition_text())
    print(Eeh.get_envir_edit_wating_room_text())
    print(Eeh.get_envir_edit_examination_office_text())
    print(Eeh.get_envir_edit_control_room_text())
    print(Eeh.get_envir_edit_detention_chamber_text())
    print(Eeh.get_envir_edit_confidential_room_text())
    print(Eeh.get_envir_edit_safety_box_text())
    print(Eeh.get_envir_edit_independent_room_text())
    print(Eeh.get_envir_edit_medkit_text())
