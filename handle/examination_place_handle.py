# coding=utf-8
import os

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from page.examination_place_page import ExaminationPlacePage
from selenium import webdriver
import time
from case.login_keyword_cases import LoginKeywordCases


class ExaminationPlaceHandle(object):
    def __init__(self, driver):
        self.driver = driver
        self.Ep = ExaminationPlacePage(self.driver)

    # 输入考点编号
    def send_place_code(self, place_code):
        if place_code is not None:
            value = str(place_code)
            self.Ep.get_place_code().send_keys(value)

    # 输入考点名称
    def send_place_name(self, place_name):
        if place_name is not None:
            self.Ep.get_place_name().send_keys(place_name)

    # 输入行政区划
    def send_place_division_code(self):
        self.Ep.get_place_division_code().click()
        self.Ep.get_place_division_code_fchild().click()
        time.sleep(1)
        self.Ep.get_place_division_code_schild().click()
        time.sleep(1)
        self.Ep.get_place_division_code_tchild().click()

    # 输入考点地址
    def send_place_address(self, place_address):
        if place_address is not None:
            self.Ep.get_place_address().send_keys(place_address)

    # 输入考点负责人
    def send_place_person(self, place_person):
        if place_person is not None:
            self.Ep.get_place_person().send_keys(place_person)

    # 输入负责人联系电话
    def send_place_person_tel(self, place_person_tel):
        if place_person_tel is not None:
            self.Ep.get_place_person_tel().send_keys(place_person_tel)

    # 选择状态
    def select_place_status(self):
        self.Ep.get_place_status().click()

    # 获取开关选择状态
    def get_place_status(self):
        # self.Ep.get_place_status_value().get_attribute('value')
        self.Ep.get_place_status_value()

    # 获取错误信息
    def get_user_text(self, error_info, assertText):
        try:

            if error_info == 'place_code_error':
                text_content = self.Ep.get_place_code_error().text
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'place_name_error':
                # text = self.Ep.get_place_name_error().text
                text_content = self.Ep.get_place_name_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'place_division_code_error':
                '''
                WebDriverWait(self.driver, 10).until(
                    lambda x: x.find_element_by_xpath('/html/body/div[3]/div/div'))
                text = self.driver.find_element_by_xpath('/html/body/div[3]/div/div').text
                '''
                # text = self.Ep.get_place_division_code_error().text
                text_content = self.Ep.get_place_division_code_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'place_address_error':
                # text = self.Ep.get_place_address_error().text
                text_content = self.Ep.get_place_address_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'place_person_error':
                # text = self.Ep.get_place_person_error().text
                text_content = self.Ep.get_place_person_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'place_person_tel_error':
                # text = self.Ep.get_place_person_tel_error().text
                text_content = self.Ep.get_place_person_tel_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            else:
                text1 = self.Ep.get_place_code_error().get_attribute("innerHTML")
                text2 = self.Ep.get_place_name_error().get_attribute("innerHTML")
                text3 = self.Ep.get_place_division_code_error().get_attribute("innerHTML")
                text4 = self.Ep.get_place_address_error().get_attribute("innerHTML")
                text5 = self.Ep.get_place_person_error().get_attribute("innerHTML")
                text6 = self.Ep.get_place_person_tel_error().get_attribute("innerHTML")
                if text1 and text2 and text3 and text4 and text5 and text6:
                    text = 'ok'

            return text
        except BaseException as e:
            print(repr(e))
            return None

    # 点击确定添加按钮
    def click_confirm_add_btn(self):
        self.Ep.get_confirm_add_btn().click()

    # 点击取消添加按钮
    def click_cancle_add_btn(self):
        self.Ep.get_cancle_add_btn().click()

    # 点击添加按钮
    def click_add_btn(self):
        self.Ep.get_add_btn().click()

    # 获取添加成功提示语
    def get_add_success_text(self):
        return self.Ep.add_success().text


if __name__ == "__main__":
    lkc = LoginKeywordCases()
    lkc.run_keyword_excel_cases()
    driver = getattr(getattr(lkc, 'lk'), 'driver')
    driver.maximize_window()
    Eh = ExaminationPlaceHandle(getattr(getattr(lkc, 'lk'), 'driver'))
    time.sleep(1)
    Eh.click_add_btn()
    # Eh.send_place_code('123456')
    # Eh.send_place_name('西北')
    # Eh.send_place_division_code()
    # Eh.send_place_address('西北税务学校')
    # Eh.send_place_person('小冯')
    # Eh.send_place_person_tel('15002933333')
    # Eh.select_place_status()
    # Eh.click_confirm_add_btn()
    # Eh.click_cancle_add_btn()
    # print(Eh.get_user_text('place_code_error', '1212'))
    # print(Eh.get_user_text('place_name_error', '1212'))
    print(Eh.get_place_status())
    time.sleep(10)
