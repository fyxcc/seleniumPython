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
    #清空基本资料编辑编号字段
    def clear_basic_edit_code_text(self):
        element=self.ERp.get_basic_edit_code()
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

    print(ERh.clear_basic_edit_code_text())

