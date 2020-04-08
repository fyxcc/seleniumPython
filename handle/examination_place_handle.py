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
    def send_place_code(self,place_code):
        self.Ep.get_place_code().send_keys(place_code)

    # 输入考点名称
    def send_place_name(self, place_name):
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
        self.Ep.get_place_address().send_keys(place_address)

    # 输入考点负责人
    def send_place_person(self,place_person):
        self.Ep.get_place_person().send_keys(place_person)
    # 输入负责人联系电话
    def send_place_person_tel(self, place_person_tel):
        self.Ep.get_place_person_tel().send_keys(place_person_tel)

    # 选择状态
    def select_place_status(self):
        self.Ep.get_place_status().click()

    # 获取错误信息
    def get_user_text(self, error_info, assertText):
        try:

            if error_info == 'place_code_error':
                text = self.Ep.get_place_code_error().text
            elif error_info == 'place_name_error':
                text = self.Ep.get_place_name_error().text
            elif error_info == 'place_division_code_error':
                '''
                WebDriverWait(self.driver, 10).until(
                    lambda x: x.find_element_by_xpath('/html/body/div[3]/div/div'))
                text = self.driver.find_element_by_xpath('/html/body/div[3]/div/div').text
                '''
                text = self.Ep.get_place_division_code_error().text
            elif error_info == 'place_address_error':
                text = self.Ep.get_place_address_error().text
            elif error_info == 'place_person_error':
                text = self.Ep.get_place_person_error().text
            else:
                text = self.Ep.get_place_person_tel_error().text
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

    # 获取添加按钮文字
    def get_login_btn_text(self):
        return self.lp.get_login_btn().text


if __name__ == "__main__":
    lkc = LoginKeywordCases()
    lkc.run_keyword_excel_cases()
    driver=getattr(getattr(lkc, 'lk'), 'driver')
    driver.maximize_window()
    Eh = ExaminationPlaceHandle(getattr(getattr(lkc, 'lk'), 'driver'))
    time.sleep(1)
    Eh.click_add_btn()
    Eh.send_place_code('123456')
    Eh.send_place_name('西北')
    Eh.send_place_division_code()
    Eh.send_place_address('西北税务学校')
    #Eh.send_place_person('小冯')
    #Eh.send_place_person_tel('15002933333')
    #Eh.select_place_status()
    #Eh.click_confirm_add_btn()
    #Eh.click_cancle_add_btn()
    time.sleep(10)
