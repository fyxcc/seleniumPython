# coding=utf-8
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


class ExaminationeEnvirHandle(object):
    def __init__(self, driver):
        self.driver = driver
        self.Eep = ExaminationEnvirPage(self.driver)
        self.Tu = TableUtil(self.driver)
    #点击环境信息按钮
    def click_envir_btn(self):
        return self.Eep.get_envir_btn().click()
    #点击环境信息编辑按钮
    def click_envir_edit_btn(self):
        return self.Eep.get_envir_edit_btn().click()
    #点击环境信息编辑保存按钮
    def click_envir_edit_save_btn(self):
        return self.Eep.get_envir_edit_save_btn().click()
    #点击环境信息编辑保取消按钮
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
    #编辑考场环境信息有无停车场内容
    def get_envir_edit_paking_condition_text(self):
        return self.Eep.get_envir_edit_paking_condition().text
    #编辑考场环境信息有无候考室内容
    def get_envir_edit_wating_room_text(self):
        return self.Eep.get_envir_edit_wating_room().text
    #编辑考场环境信息有无考务办公室内容
    def get_envir_edit_examination_office_text(self):
        return self.Eep.get_envir_edit_examination_office().text
    #编辑考场环境信息有无监控室内容
    def get_envir_edit_control_room_text(self):
        return self.Eep.get_envir_edit_control_room().text
    #编辑考场环境信息有无滞留室内容
    def get_envir_edit_detention_chamber_text(self):
        return self.Eep.get_envir_edit_detention_chamber().text
    # 编辑考场环境信息有无保密室内容
    def get_envir_edit_confidential_room_text(self):
        return self.Eep.get_envir_edit_confidential_room().text
    #编辑考场环境信息有无保险柜内容
    def get_envir_edit_safety_box_text(self):
        return self.Eep.get_envir_edit_safety_box().text
    #编辑考场环境信息有无独立机房内容
    def get_envir_edit_independent_room_text(self):
        return self.Eep.get_envir_edit_independent_room().text
    #编辑考场环境信息有无医疗箱内容
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
                resultText=result.text
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
    #判断环境信息是否完整
    def judge_envir_complete(self):
        area=self.get_place_area_text()
        apread=self.get_place_spread_text()
        toilet_condition=self.get_toilet_condition_text()
        paking_condition=self.get_paking_condition_text()
        cars_num=self.get_cars_num_text()
        wating_room=self.get_wating_room_text()
        examination_office=self.get_examination_office_text()
        control_room=self.get_control_room_text()
        detention_chamber=self.get_detention_chamber_text()
        confidential_room=self.get_confidential_room_text()
        safety_box=self.get_safety_box_text()
        independent_room=self.get_independent_room_text()
        medkit=self.get_medkit_text()
        if area!=None and apread!=None and toilet_condition!=None and paking_condition!=None and cars_num!=None and wating_room!=None and examination_office!=None and control_room!=None and  detention_chamber!=None and  confidential_room!=None and  safety_box!=None and  independent_room!=None and medkit!=None:
            return True
        else:
            return False
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
        data2= self.get_machine_signal_shield_text()
        data3 = self.get_machine_video_monitor_text()
        data4 = self.get_machine_gen_text()
        data5 = self.get_machine_electricity_text()
        data6= self.get_machine_available_examination_text()
        data7 = self.get_machine_cloud_desktop_text()
        data8 = self.get_machine_virtual_server_text()
        data9 = self.get_machine_processor_text()
        data10 = self.get_machine_cpu_text()
        data11 = self.get_machine_storage_text()
        data12 = self.get_machine_caliche_text()
        data13= self.get_machine_internet_card_text()
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
        if data1 != None and data2 != None and data3 != None and data4 != None and data5 != None and data6 != None and data7 != None and data8 != None and data9 != None and data10 != None and data11 != None and data12 != None and data13 != None and data14!=None and data15!=None and data16!=None and data17!=None and data18!=None and data19!=None and data20!=None  and data21!=None and data22!=None and data23!=None and data23!=None:
            return True
        else:
            return False
    # 获取照片标题字段

    def get_photo_title_text(self):
        return self.Eep.get_photo_title().text
    # 获取照片简介字段

    def get_photo_content_text(self):
        return self.Eep.get_photo_content().text
    #判断照片完整性
    def judge_photo_complete(self):
        data1=self.Eep.get_photo()
        data2=self.get_photo_title_text()
        data3=self.get_photo_content_text()
        if data1!=None and data2!=None and data3!=None:
            return True
        else:
            return False

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




