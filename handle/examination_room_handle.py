# coding=utf-8
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from page.examination_room_page import ExaminationRoomPage
import time
from case.login_keyword_cases import LoginKeywordCases
from handle.examination_place_handle import ExaminationPlaceHandle
from util.table_util import TableUtil


class ExaminationRoomHandle(object):
    def __init__(self, driver):
        self.driver = driver
        self.ERp = ExaminationRoomPage(self.driver)
        self.Tu = TableUtil(self.driver)

    # 获取基本资料考点编号字段
    def get_basic_code_text(self):
        return self.ERp.get_basic_code().text

    # 获取基本资料考点名称字段
    def get_basic_name_text(self):
        return self.ERp.get_basic_name().text

    # 获取基本资料考点性质字段
    def get_basic_character_text(self):
        return self.ERp.get_basic_character().text

    # 获取基本资料可用总机位数字段
    def get_basic_total_computer_num_text(self):
        return self.ERp.get_basic_total_computer_num().text

    # 获取基本资料可编排机位数字段
    def get_basic_use_computer_num_text(self):
        return self.ERp.get_basic_use_computer_num().text

    # 获取基本资料考场数字段
    def get_basic_place_num_text(self):
        return self.ERp.get_basic_place_num().text

    # 获取基本资料合同签订时间字段
    def get_basic_time_text(self):
        return self.ERp.get_basic_time().text

    # 获取基本资料合同签订时长字段

    def get_basic_duration_text(self):
        return self.ERp.get_basic_duration().text

    # 获取基本资料邮政编码字段

    def get_basic_post_code_text(self):
        return self.ERp.get_basic_post_code().text

    # 获取基本资料考点负责人字段

    def get_basic_place_person_text(self):
        return self.ERp.get_basic_place_person().text

    # 获取基本资料考点负责人电话字段

    def get_basic_person_tel_text(self):
        return self.ERp.get_basic_person_tel().text

    # 点击基本资料编辑按钮
    def click_basic_edit_btn(self):
        return self.ERp.get_basic_edit_btn().click()

    # 获取基本资料编辑按钮字段

    def get_basic_edit_btn_text(self):
        return self.ERp.get_basic_edit_btn().text

    # 获取交通路线的考点地址字段
    def get_traffic_address_text(self):
        return self.ERp.get_traffic_address().text

    # 获取交通路线的交通情况字段

    def get_traffic_condition_text(self):
        return self.ERp.get_traffic_condition().text

    # 获取交通路线的具体线路字段
    def get_traffic_concrete_route_text(self):
        return self.ERp.get_traffic_concrete_route().text

    # 获取交通路线的地理位置描述字段
    def get_traffic_location_text(self):
        return self.ERp.get_traffic_location().text

    # 获取交通路线的经度字段
    def get_traffic_longitude_text(self):
        return self.ERp.get_traffic_longitude().text

    # 获取交通路线的纬度字段
    def get_traffic_latitude_text(self):
        return self.ERp.get_traffic_latitude().text

    # 获取交通路线编辑按钮段
    def get_traffic_edit_btn_text(self):
        return self.ERp.get_traffic_edit_btn().text

    # 获取通讯录姓名字段
    def get_book_table_name_text(self):
        return self.ERp.get_book_table_name().text

    # 获取通讯录性别字段

    def get_book_table_sex_text(self):
        return self.ERp.get_book_table_sex().text

    # 通讯录职位字段

    def get_book_table_position_text(self):
        return self.ERp.get_book_table_position().text

    # 获取通讯录手机字段

    def get_book_table_tel_text(self):
        return self.ERp.get_book_table_tel().text

    # 获取通讯录固定电话字段

    def get_book_table_fixed_phone_text(self):
        return self.ERp.get_book_table_fixed_phone().text

    # 获取通讯录邮寄地址字段

    def get_book_table_post_address_text(self):
        return self.ERp.get_book_table_post_address().text

    # 获取通讯录电子邮箱字段

    def get_book_table_email_text(self):
        return self.ERp.get_book_table_email().text

    # 获取qq字段
    def get_book_table_text(self):
        return self.ERp.get_book_table_qq().text

    # 获取通讯录添加按钮字段
    def get_book_add_btn_text(self):
        return self.ERp.get_book_add_btn().text

    # 获取考点数字段
    def get_place_num_text(self):
        text_string = self.ERp.get_place_num().text
        text_list = text_string.split('：')
        return text_list[1]

    # 点击选择考点按钮
    def click_select_btn(self):
        return self.ERp.get_select_btn().click()

    # 获取选择考点框内容
    def get_select_text(self):
        return self.ERp.get_select_text().text

    # 获取按照行政区划选择考点字段
    def get_select_place_by_divi_text(self):
        return self.ERp.get_select_place_by_divi().text

    # 获取按照考点名称选择考点字段
    def get_select_place_by_name_text(self):
        return self.ERp.get_select_place_by_name().text

    # 获取按照搜索条件选择考点字段
    def get_select_place_by_search_text(self):
        return self.ERp.get_select_place_by_search().get_attribute('placeholder')

    # 获取按照搜索条件选择考点输入框
    def send_select_place_by_search_text(self, placeName):
        element = self.ERp.get_select_place_by_search()
        if element != None:
            element.send_keys(Keys.CONTROL, 'a')
            element.send_keys(Keys.BACK_SPACE)
        return self.ERp.get_select_place_by_search().send_keys(placeName)

    # 点击按照搜索条件选择考点下拉框
    def click_select_place_by_search_btn(self):
        return self.ERp.get_select_place_by_search_btn().click()

    # 获取按照搜索条件选择考点下拉框第一个选项内容

    def get_place_by_search_fchild_text(self):
        return self.ERp.select_place_by_search_fchild().text

    # 点击按照搜索条件选择考点下拉框第二个选项
    def click_select_place_by_search_schild(self):
        return self.ERp.select_place_by_search_schild().click()

    # 获取首字母导航字段
    def get_select_letter_text(self):
        return self.ERp.get_select_letter().text

    # 获取基本资料编辑考点性质子选项
    def get_basic_edit_character_child(self, child_lever):
        if child_lever == 'basic_edit_character_1child':
            return self.ERp.get_basic_edit_character_1child().text
        elif child_lever == 'basic_edit_character_2child':
            return self.ERp.get_basic_edit_character_2child().text
        elif child_lever == 'basic_edit_character_3child':
            return self.ERp.get_basic_edit_character_3child().text
        elif child_lever == 'basic_edit_character_4child':
            return self.ERp.get_basic_edit_character_4child().text
        elif child_lever == 'basic_edit_character_5child':
            return self.ERp.get_basic_edit_character_5child().text
        elif child_lever == 'basic_edit_character_6child':
            return self.ERp.get_basic_edit_character_6child().text
        elif child_lever == 'basic_edit_character_7child':
            return self.ERp.get_basic_edit_character_7child().text

    # 获取基本资料编辑可用总机位数字段状态
    def get_basic_edit_total_computer_num_status(self):
        element = self.ERp.get_basic_edit_total_computer_num()
        return element.is_enabled()

    # 获取基本资料编辑可用编排机位数字段状态
    def get_basic_edit_use_computer_num_status(self):
        element = self.ERp.get_basic_edit_use_computer_num()
        return element.is_enabled()

    # 获取基本资料编辑考场数字段状态
    def get_basic_edit_place_num_status(self):
        element = self.ERp.get_basic_edit_place_num()
        return element.is_enabled()

    # 点击基本资料编辑保存按钮
    def click_get_basic_edit_save_btn(self):
        return self.ERp.get_basic_edit_save_btn().click()

    # 点击基本资料编辑取消按钮
    def click_basic_edit_cancle_btn(self):
        return self.ERp.get_basic_edit_cancle_btn().click()

    # 清空基本资料编辑编号字段
    def clear_basic_edit_code_text(self):
        element = self.ERp.get_basic_edit_code()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 清空基本资料编辑名称字段

    def clear_basic_edit_name_text(self):
        element = self.ERp.get_basic_edit_name()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 清空基本资料编辑性质字段

    def clear_basic_edit_character_text(self):
        element = self.ERp.get_basic_edit_character()
        time.sleep(1)
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 清空基本资料编辑合同签订时间字段

    def clear_basic_edit_time_text(self):
        element = self.ERp.get_basic_edit_time()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 清空基本资料编辑合同签订时长字段

    def clear_basic_edit_duration_text(self):
        element = self.ERp.get_basic_edit_duration()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 清空基本资料编辑邮政编码字段

    def clear_basic_edit_post_code_text(self):
        element = self.ERp.get_basic_edit_post_code()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 清空基本资料编辑考点负责人字段

    def clear_basic_edit_place_person_text(self):
        element = self.ERp.get_basic_edit_place_person()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 清空基本资料编辑考点负责人电话字段

    def clear_basic_edit_person_tel_text(self):
        element = self.ERp.get_basic_edit_person_tel()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 判断基本信息部分元素是否完整
    def judge_basic_info(self):

        code = self.get_basic_code_text()
        name = self.get_basic_name_text
        character = self.get_basic_character_text()
        total_computer = self.get_basic_total_computer_num_text()
        use_computer = self.get_basic_use_computer_num_text()
        place_num = self.get_basic_place_num_text()
        basic_time = self.get_basic_time_text()
        basic_duration = self.get_basic_duration_text()
        post_code = self.get_basic_post_code_text()
        place_person = self.get_basic_place_person_text()
        person_tel = self.get_basic_person_tel_text()
        if code != None and name != None and character != None and total_computer != None and use_computer != None and place_num != None and basic_time != None and basic_duration != None and post_code != None and place_person != None and person_tel != None:
            return True
        else:
            return False

    # 判断交通信息是否完整
    def judge_traffic_info(self):
        traffic_address = self.get_traffic_address_text()
        traffic_condition = self.get_traffic_condition_text()
        traffic_concrete_route = self.get_traffic_concrete_route_text()
        traffic_location = self.get_traffic_location_text()
        traffic_longitude = self.get_traffic_longitude_text()
        traffic_latitude = self.get_traffic_latitude_text()
        if traffic_address != None and traffic_condition != None and traffic_concrete_route != None and traffic_location != None and traffic_longitude != None and traffic_latitude != None:
            return True
        else:
            return False

    # 判断通讯录信息是否完整
    def judge_book_info(self):
        book_table_name = self.get_book_table_name_text()
        book_table_sex = self.get_book_table_sex_text()
        book_table_position = self.get_book_table_position_text()
        book_table_tel = self.get_book_table_tel_text()
        book_table_fixed_phone = self.get_book_table_fixed_phone_text()
        book_table_post_address = self.get_book_table_post_address_text()
        book_table_email = self.get_book_table_email_text()
        book_table_text = self.get_book_table_text()
        if book_table_name != None and book_table_sex != None and book_table_position != None and book_table_tel != None and book_table_fixed_phone != None and book_table_post_address != None and book_table_email != None and book_table_text != None:
            return True
        else:
            return False

    # 判断按钮完整性
    def judge_btn_complete(self):
        btn1 = self.get_basic_edit_btn_text()
        btn2 = self.get_traffic_edit_btn_text()
        btn3 = self.get_book_add_btn_text()
        if btn1 == '编辑' and btn2 == '编辑' and btn3 == '添加':
            return True
        else:
            return False

    # 判断选择考点功能页面元素是否完整
    def select_place_complete(self):
        select_place_by_divi_text = self.get_select_place_by_divi_text()
        select_place_by_name_text = self.get_select_place_by_name_text()
        select_place_by_search_text = self.get_select_place_by_search_text()
        select_letter_text = self.get_select_letter_text()
        if select_place_by_divi_text == '按行政区划' and select_place_by_name_text == '按考点名称' and select_place_by_search_text == '请输入考点名称搜索' and self.get_select_letter_text() != None:
            return True
        else:
            return False

    # 输入编辑基本考点编号
    def send_basic_edit_code(self, basic_edit_code):
        if len(basic_edit_code) != 0:
            self.ERp.get_basic_edit_code().send_keys(basic_edit_code)

    # 输入编辑基本考点名称
    def send_basic_edit_name(self, basic_edit_name):
        if len(basic_edit_name) != 0:
            self.ERp.get_basic_edit_name().send_keys(basic_edit_name)

    # 输入编辑基本合同签订时间

    def send_basic_edit_time(self, basic_edit_time):
        if len(basic_edit_time) != 0:
            self.ERp.get_basic_edit_time().send_keys(basic_edit_time)

    # 输入编辑基本合同签订时长

    def send_basic_edit_duration(self, basic_edit_duration):
        if len(basic_edit_duration) != 0:
            self.ERp.get_basic_edit_duration().send_keys(basic_edit_duration)

    # 输入编辑基本邮政编码

    def send_basic_edit_post_code(self, basic_edit_post_code):
        if len(basic_edit_post_code) != 0:
            self.ERp.get_basic_edit_post_code().send_keys(basic_edit_post_code)

    # 输入编辑基本考点负责人

    def send_basic_edit_place_person(self, basic_edit_place_person):
        if len(basic_edit_place_person) != 0:
            self.ERp.get_basic_edit_place_person().send_keys(basic_edit_place_person)

    # 输入编辑基本考点负责人电话

    def send_basic_edit_person_tel(self, basic_edit_person_tel):
        if len(basic_edit_person_tel) != 0:
            self.ERp.get_basic_edit_person_tel().send_keys(basic_edit_person_tel)

    # 获取编辑成功提示语
    def get_basic_edit_success_text(self):
        self.ERp.get_basic_edit_success().text

    # 获取基本资料编辑错误信息

    def get_edit_user_text(self, error_info, assertText):
        try:

            if error_info == 'basic_edit_code_error':
                text_content = self.ERp.get_basic_edit_code_error().text
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'basic_edit_name_error':
                # text = self.Ep.get_edit_place_name_error().text
                text_content = self.ERp.get_basic_edit_name_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'edit_place_division_code_error':
                '''
                WebDriverWait(self.driver, 10).until(
                    lambda x: x.find_element_by_xpath('/html/body/div[3]/div/div'))
                text = self.driver.find_element_by_xpath('/html/body/div[3]/div/div').text
                '''
                # text = self.Ep.get_place_division_code_error().text
                text_content = self.Ep.get_edit_place_division_code_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'basic_edit_duration_error':
                # text = self.Ep.get_place_address_error().text
                text_content = self.ERp.get_basic_edit_duration_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'basic_edit_place_person_error':
                # text = self.Ep.get_edit_place_person_error().text
                text_content = self.ERp.get_basic_edit_place_person_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'basic_edit_person_tel_error':
                # text = self.Ep.get_edit_place_person_tel_error().text
                text_content = self.ERp.get_basic_edit_person_tel_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'basic_edit_post_code_error':
                # text = self.Ep.get_edit_place_person_tel_error().text
                text_content = self.ERp.get_basic_edit_post_code_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'repeat_place_code_error':
                WebDriverWait(self.driver, 10).until(
                    lambda x: x.find_element_by_xpath('/html/body/div[14]/div/div'))
                text_content = self.driver.find_element_by_xpath('/html/body/div[14]/div/div').text
                # text_content = self.Ep.get_edit_repeat_code_error().text
                if text_content == assertText:
                    text = 'ok'
            else:
                text1 = self.ERp.get_basic_edit_code_error().get_attribute("innerHTML")
                text2 = self.ERp.get_basic_edit_name_error().get_attribute("innerHTML")
                # text3=self.ERP.get_basic_edit_time_error().get_attribute("innerHTML")
                text4 = self.ERp.get_basic_edit_duration_error().get_attribute("innerHTML")
                text5 = self.ERp.get_basic_edit_post_code_error().get_attribute("innerHTML")
                text6 = self.ERp.get_basic_edit_place_person_error().get_attribute("innerHTML")
                text7 = self.ERp.get_basic_edit_person_tel_error().get_attribute("innerHTML")
                if text1 and text2 and text4 and text5 and text6 and text7:
                    text = 'ok'

            return text
        except BaseException as e:
            print(repr(e))
            return None

    # 点击编辑交通信息按钮
    def click_traffic_edit_btn(self):
        return self.ERp.get_traffic_edit_btn().click()

    # 点击编辑交通信息保存按钮
    def click_traffic_edit_save_btn(self):
        return self.ERp.get_traffic_edit_save_btn().click()

    # 点击编辑交通信息取消按钮
    def click_traffic_edit_cancle_btn(self):
        return self.ERp.get_traffic_edit_cancle_btn().click()

    # 获取编辑交通信息考点地址提示语
    def get_traffic_edit_address_info(self):
        return self.ERp.get_traffic_edit_address().get_attribute("placeholder")

    # 获取编辑交通信息交通状况提示语

    def get_traffic_edit_condition_info(self):
        return self.ERp.get_traffic_edit_condition().get_attribute("placeholder")

    # 交通路线的编辑具体线路提示语

    def get_traffic_edit_concrete_route_info(self):
        return self.ERp.get_traffic_edit_concrete_route().get_attribute("placeholder")

    # 交通路线的编辑地理位置描述提示语

    def get_traffic_edit_location_info(self):
        return self.ERp.get_traffic_edit_location().get_attribute("placeholder")

    # 交通路线的编辑经度提示语

    def get_traffic_edit_longitude_info(self):
        return self.ERp.get_traffic_edit_longitude().get_attribute("placeholder")

    # 交通路线的编辑纬度提示语

    def get_traffic_edit_latitude_info(self):
        return self.ERp.get_traffic_edit_latitude().get_attribute("placeholder")

    # 清空交通信息编辑地址字段
    def clear_traffic_edit_address_text(self):
        element = self.ERp.get_traffic_edit_address()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 清空交通信息编辑情况字段

    def clear_traffic_edit_condition_text(self):
        element = self.ERp.get_traffic_edit_condition()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 清空交通信息编辑具体线路字段

    def clear_traffic_edit_concrete_route_text(self):
        element = self.ERp.get_traffic_edit_concrete_route()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 清空交通信息编辑地理位置字段

    def clear_traffic_edit_location_text(self):
        element = self.ERp.get_traffic_edit_location()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 清空交通信息编辑经度字段

    def clear_traffic_edit_longitude_text(self):
        element = self.ERp.get_traffic_edit_longitude()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 清空交通信息编辑地址字段

    def clear_traffic_edit_latitude_text(self):
        element = self.ERp.get_traffic_edit_latitude()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 输入编辑交通信息考点地址

    def send_traffic_edit_address(self, traffic_edit_address):
        if len(traffic_edit_address) != 0:
            self.ERp.get_traffic_edit_address().send_keys(traffic_edit_address)

    # 输入编辑交通信息考交通情况

    def send_traffic_edit_condition(self, traffic_edit_condition):
        if len(traffic_edit_condition) != 0:
            self.ERp.get_traffic_edit_condition().send_keys(traffic_edit_condition)

    # 输入编辑交通信息具体线路

    def send_traffic_edit_concrete_route(self, traffic_edit_concrete_route):
        if len(traffic_edit_concrete_route) != 0:
            self.ERp.get_traffic_edit_concrete_route().send_keys(traffic_edit_concrete_route)

    # 输入编辑交通信息考地理位置描述

    def send_traffic_edit_location(self, traffic_edit_location):
        if len(traffic_edit_location) != 0:
            self.ERp.get_traffic_edit_location().send_keys(traffic_edit_location)

    # 输入编辑交通信息经度

    def send_traffic_edit_longitude(self, traffic_edit_longitude):
        if len(traffic_edit_longitude) != 0:
            self.ERp.get_traffic_edit_longitude().send_keys(traffic_edit_longitude)

    # 输入编辑交通信息纬度

    def send_traffic_edit_latitude(self, traffic_edit_latitude):
        if len(traffic_edit_latitude) != 0:
            self.ERp.get_traffic_edit_latitude().send_keys(traffic_edit_latitude)

    # 获取交通信息编辑错误信息

    def get_edit_traffic_user_text(self, error_info, assertText):
        try:

            if error_info == 'traffic_edit_address_error':
                text_content = self.ERp.get_traffic_address_error().text
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'traffic_edit_condition_error':
                # text = self.Ep.get_edit_place_name_error().text
                text_content = self.ERp.get_traffic_edit_condition_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'traffic_edit_concrete_route_error':
                '''
                WebDriverWait(self.driver, 10).until(
                    lambda x: x.find_element_by_xpath('/html/body/div[3]/div/div'))
                text = self.driver.find_element_by_xpath('/html/body/div[3]/div/div').text
                '''
                # text = self.Ep.get_place_division_code_error().text
                text_content = self.ERp.get_traffic_edit_concrete_route_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'traffic_edit_location_error':
                # text = self.Ep.get_place_address_error().text
                text_content = self.ERp.get_traffic_edit_location_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'repeat_place_code_error':
                WebDriverWait(self.driver, 10).until(
                    lambda x: x.find_element_by_xpath('/html/body/div[14]/div/div'))
                text_content = self.driver.find_element_by_xpath('/html/body/div[14]/div/div').text
                # text_content = self.Ep.get_edit_repeat_code_error().text
                if text_content == assertText:
                    text = 'ok'
            else:
                text1 = self.ERp.get_traffic_address_error().get_attribute("innerHTML")
                text2 = self.ERp.get_traffic_edit_condition_error().get_attribute("innerHTML")
                text3 = self.ERp.get_traffic_edit_concrete_route_error().get_attribute("innerHTML")
                text4 = self.ERp.get_traffic_edit_location_error().get_attribute("innerHTML")
                if text1 and text2 and text3 and text4:
                    text = 'ok'

            return text
        except BaseException as e:
            print(repr(e))
            return None

    # 点击通讯录添加按钮
    def click_book_add_btn(self):
        return self.ERp.get_book_add_btn().click()

    # 点击通讯录添加确定按钮
    def click_book_add_confirm_btn(self):
        return self.ERp.get_book_add_confirm_btn().click()

    # 点击通讯录添加取消按钮
    def click_book_add_cancle_btn(self):
        return self.ERp.get_book_add_cancle_btn().click()

    # 判断添加通讯录弹框是否打开
    def judge_book_add_frame(self):
        if self.ERp.get_book_add_frame() is not None:
            if self.ERp.get_book_add_frame().text == '添加通讯录':
                return True
            else:
                return False
        else:
            return False

    # 添加通讯录姓名提示语
    def get_book_add_name_info(self):
        return self.ERp.get_book_add_name().get_attribute("placeholder")

    # 添加通讯录性别提示语
    def get_book_add_sex_text(self):
        return self.ERp.get_book_add_sex().text

    # 添加通讯录职位提示语
    def get_book_add_position_info(self):
        return self.ERp.get_book_add_position().text

    # 添加通讯录手机提示语
    def get_book_add_phone_info(self):
        return self.ERp.get_book_add_phone().get_attribute("placeholder")

    # 添加通讯录固定电话提示语

    def get_book_add_tel_info(self):
        return self.ERp.get_book_add_tel().get_attribute("placeholder")

    # 添加通讯录邮寄地址提示语

    def get_book_add_post_address_info(self):
        return self.ERp.get_book_add_post_address().get_attribute("placeholder")

    # 添加通讯录电子邮箱提示语

    def get_book_add_mail_info(self):
        return self.ERp.get_book_add_mail().get_attribute("placeholder")

    # 添加通讯录qq提示语

    def get_book_add_qq_info(self):
        return self.ERp.get_book_add_qq().get_attribute("placeholder")

    # 清空通讯录添加姓名字段
    def clear_book_add_name_text(self):
        element = self.ERp.get_book_add_name()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)
    # 清空通讯录添加职位字段
    def clear_book_add_position_text(self):
        element = self.ERp.get_book_add_position()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 清空通讯录添加手机字段
    def clear_book_add_phone_text(self):
        element = self.ERp.get_book_add_phone()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)
    # 清空通讯录添加固定电话字段
    def clear_book_add_tel_text(self):
        element = self.ERp.get_book_add_tel()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 清空通讯录添加邮寄地址字段
    def clear_book_add_post_address_text(self):
        element = self.ERp.get_book_add_post_address()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)
    # 清空通讯录添加电子邮箱字段
    def clear_book_add_mail_text(self):
        element = self.ERp.get_book_add_mail()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)
    # 清空通讯录添加qq字段
    def clear_book_add_qq_text(self):
        element = self.ERp.get_book_add_qq()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)
    # 输入添加通讯录姓名

    def send_book_add_name(self, book_add_name):
        if len(book_add_name) != 0:
            self.ERp.get_book_add_name().send_keys(book_add_name)
    # 输入添加通讯录手机

    def send_book_add_phone(self, book_add_phone):
        if len(book_add_phone) != 0:
            self.ERp.get_book_add_phone().send_keys(book_add_phone)
    # 输入添加通讯录固定电话

    def send_book_add_tel(self, book_add_tel):
        if len(book_add_tel) != 0:
            self.ERp.get_book_add_tel().send_keys(book_add_tel)
    # 输入添加通讯录邮寄地址

    def send_book_add_post_address(self, book_add_post_address):
        if len(book_add_post_address) != 0:
            self.ERp.get_book_add_post_address().send_keys(book_add_post_address)
    # 输入添加通讯录电子邮箱

    def send_book_add_mail(self, book_add_mail):
        if len(book_add_mail) != 0:
            self.ERp.get_book_add_mail().send_keys(book_add_mail)
    # 输入添加通讯录qq

    def send_book_add_qq(self, book_add_qq):
        if len(book_add_qq) != 0:
            self.ERp.get_book_add_qq().send_keys(book_add_qq)
    #添加通讯录失败结果提示信息
    def get_book_add_result_fail_text(self):
        return self.ERp.get_book_add_result_fail().text
    # 添加通讯录成功结果提示信息

    def get_book_add_result_success_text(self):
        return self.ERp.get_book_add_result_success().text
    # 获取通讯录添加错误信息

    def get_book_error_text(self, error_info, assertText):
        try:

            if error_info == 'book_add_phone_error':
                text_content = self.ERp.get_book_add_phone_error().text
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'book_add_tel_error':
                # text = self.Ep.get_place_name_error().text
                text_content = self.ERp.get_book_add_tel_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'book_add_mail_error':
                # text = self.Ep.get_place_address_error().text
                text_content = self.ERp.get_book_add_mail_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'book_add_post_address_error':
                # text = self.Ep.get_place_person_error().text
                text_content = self.ERp.get_book_add_post_address_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'book_add_name_error':
                # text = self.Ep.get_place_person_tel_error().text
                text_content = self.ERp.get_book_add_name_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'

            else:
                text1 = self.ERp.get_book_add_name_error().get_attribute("innerHTML")
                text2 = self.ERp.get_book_add_position_error().get_attribute("innerHTML")
                #text3 = self.ERp.get_book_add_phone_error().get_attribute("innerHTML")
                #text4 = self.ERp.get_book_add_tel_error().get_attribute("innerHTML")
                #text5 = self.ERp.get_book_add_post_address_error().get_attribute("innerHTML")
                #text6 = self.ERp.get_book_add_mail_error().get_attribute("innerHTML")
                if text1!=None and text2!=None:
                    text = 'ok'
            return text
        except BaseException as e:
            print(repr(e))
            return None
    # 点击添加通讯录职位

    def click_book_add_position(self):
        self.ERp.get_book_add_position().click()
    # 获取通讯录添加职位子选项

    def get_book_add_position_child(self, child_lever):
        if child_lever == 'book_add_position_1child':
            return self.ERp.get_book_add_position_1child().text
        elif child_lever == 'book_add_position_2child':
            return self.ERp.get_book_add_position_2child().text
        elif child_lever == 'book_add_position_3child':
            return self.ERp.get_book_add_position_3child().text
        elif child_lever == 'book_add_position_4child':
            return self.ERp.get_book_add_position_4child().text
    # 点击通讯录添加职位子选项

    def click_book_add_position_child(self, child_lever):
        if child_lever == 'book_add_position_1child':
            return self.ERp.get_book_add_position_1child().click()
        elif child_lever == 'book_add_position_2child':
            return self.ERp.get_book_add_position_2child().click()
        elif child_lever == 'book_add_position_3child':
            return self.ERp.get_book_add_position_3child().click()
        elif child_lever == 'book_add_position_4child':
            return self.ERp.get_book_add_position_4child().click()
    #获取空通讯录提示信息
    def get_book_table_empty_text(self):
        if self.ERp.get_book_table_empty()!=None:
            return self.ERp.get_book_table_empty().text
        else:
            return None
    #点击通讯录编辑按钮
    def click_book_edit_btn(self):
        return self.ERp.get_book_edit_btn().click()

    # 点击通讯录编辑保存按钮
    def click_book_edit_save_btn(self):
        return self.ERp.get_book_edit_save_btn().click()

    # 点击通讯录编辑取消按钮
    def click_book_edit_cancle_btn(self):
        return self.ERp.get_book_edit_cancle_btn().click()
    #点击编辑通讯录职位
    def click_book_edit_position(self):
        return self.ERp.get_book_edit_position().click()
    # 判断编辑通讯录弹框是否打开

    def judge_book_edit_frame(self):
        if self.ERp.get_book_edit_frame() is not None:
            if self.ERp.get_book_edit_frame().text == '编辑通讯录':
                return True
            else:
                return False
        else:
            return False

    # 获取回填数据
    def get_book_edit_backfill_data(self):
        data1 = self.ERp.get_book_edit_name().get_attribute('value')
        data2 = self.ERp.get_book_edit_position().text
        if data1 and data2 :
            result = '回填信息数据完整'
        else:
            result = '回填信息数据不完整'
        return result
    #输入通讯录编辑姓名

    def send_book_edit_name(self, book_edit_name):
        if len(book_edit_name) != 0:
            self.ERp.get_book_edit_name().send_keys(book_edit_name)

    #输入通讯录编辑手机

    def send_book_edit_phone(self, book_edit_phone):
        if len(book_edit_phone) != 0:
            self.ERp.get_book_edit_phone().send_keys(book_edit_phone)
    #输入通讯录编辑固定电话

    def send_book_edit_tel(self, book_edit_tel):
        if len(book_edit_tel) != 0:
            self.ERp.get_book_edit_tel().send_keys(book_edit_tel)
    #输入通讯录编辑邮寄地址

    def send_book_edit_post_address(self, book_edit_post_address):
        if len(book_edit_post_address) != 0:
            self.ERp.get_book_edit_post_address().send_keys(book_edit_post_address)

    #输入通讯录编辑电子邮箱

    def send_book_edit_mail(self, book_edit_mail):
        if len(book_edit_mail) != 0:
            self.ERp.get_book_edit_mail().send_keys(book_edit_mail)
    #输入通讯录编辑qq

    def send_book_edit_qq(self, book_edit_qq):
        if len(book_edit_qq) != 0:
            self.ERp.get_book_edit_qq().send_keys(book_edit_qq)
    # 清空通讯录编辑姓名字段
    def clear_book_edit_name_text(self):
        element = self.ERp.get_book_edit_name()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)
    # 清空通讯录编辑手机字段

    def clear_book_edit_phone_text(self):
        element = self.ERp.get_book_edit_phone()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)
    # 清空通讯录编辑固定电话字段

    def clear_book_edit_tel_text(self):
        element = self.ERp.get_book_edit_tel()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)
    # 清空通讯录编辑邮寄地址字段

    def clear_book_edit_post_address_text(self):
        element = self.ERp.get_book_edit_post_address()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)
    # 清空通讯录编辑邮箱字段

    def clear_book_edit_mail_text(self):
        element = self.ERp.get_book_edit_mail()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)
    # 清空通讯录编辑qq字段

    def clear_book_edit_qq_text(self):
        element = self.ERp.get_book_edit_qq()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACK_SPACE)

    # 获取通讯录编辑错误信息

    def get_book_edit_error_text(self, error_info, assertText):
        try:

            if error_info == 'book_edit_phone_error':
                text_content = self.ERp.get_book_edit_phone_error().text
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'book_edit_tel_error':
                text_content = self.ERp.get_book_edit_tel_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'book_edit_mail_error':
                text_content = self.ERp.get_book_edit_mail_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'book_edit_post_address_error':
                # text = self.Ep.get_place_person_error().text
                text_content = self.ERp.get_book_edit_post_address_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'book_edit_name_error':
                text_content = self.ERp.get_book_edit_name_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            else:
                text1 = self.ERp.get_book_edit_name_error().get_attribute("innerHTML")
                text2 = self.ERp.get_book_edit_position_error().get_attribute("innerHTML")
                # text3 = self.ERp.get_book_add_phone_error().get_attribute("innerHTML")
                # text4 = self.ERp.get_book_add_tel_error().get_attribute("innerHTML")
                # text5 = self.ERp.get_book_add_post_address_error().get_attribute("innerHTML")
                # text6 = self.ERp.get_book_add_mail_error().get_attribute("innerHTML")
                if text1 != None and text2 != None:
                    text = 'ok'
            return text
        except BaseException as e:
            print(repr(e))
            return None
    # 获取通讯录编辑职位子选项

    def get_book_edit_position_child(self, child_lever):
        if child_lever == 'book_edit_position_1child':
            return self.ERp.get_book_edit_position_1child().text
        elif child_lever == 'book_edit_position_2child':
            return self.ERp.get_book_edit_position_2child().text
        elif child_lever == 'book_edit_position_3child':
            return self.ERp.get_book_edit_position_3child().text
        elif child_lever == 'book_edit_position_4child':
            return self.ERp.get_book_edit_position_4child().text
    # 点击通讯录编辑职位子选项

    def click_book_edit_position_child(self, child_lever):
        if child_lever == 'book_edit_position_1child':
            return self.ERp.get_book_edit_position_1child().click()
        elif child_lever == 'book_edit_position_2child':
            return self.ERp.get_book_edit_position_2child().click()
        elif child_lever == 'book_edit_position_3child':
            return self.ERp.get_book_edit_position_3child().click()
        elif child_lever == 'book_edit_position_4child':
            return self.ERp.get_book_edit_position_4child().click()
    #点击删除通讯录按钮
    def click_book_delete_btn(self):
        return self.ERp.get_book_delete_btn().click()
    # 点击确定删除通讯录按钮

    def click_book_confirm_delete_btn(self):
        return self.ERp.get_book_confirm_delete_btn().click()

    # 获得删除通讯录结果内容
    def get_delete_book_result_text(self):
        result=self.ERp.get_delete_book_result()
        if result!=None:
            result_text=result.text
            if result_text=='删除成功！':
                return True
            else:
                return  False
        else:
            return False



if __name__ == "__main__":
    lkc = LoginKeywordCases()
    lkc.run_keyword_excel_cases()
    driver = getattr(getattr(lkc, 'lk'), 'driver')
    driver.maximize_window()
    EPh = ExaminationPlaceHandle(driver)
    ERh = ExaminationRoomHandle(getattr(getattr(lkc, 'lk'), 'driver'))
    EPh.click_detailed_btn()
    time.sleep(2)
    ERh.click_basic_edit_btn()
    time.sleep(2)

    print(ERh.clear_basic_edit_character_text())
