#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from case.login_keyword_cases import LoginKeywordCases
from handle.examination_place_handle import ExaminationPlaceHandle
from selenium import webdriver
from time import sleep


class ExaminationPlaceBusiness(object):
    def __init__(self, driver):
        self.driver = driver
        self.Eh = ExaminationPlaceHandle(driver)

    # 成功添加
    def success_add(self, place_code, place_name, place_address, place_person, place_person_tel):
        #self.Eh.click_add_btn()
        #sleep(3)
        self.Eh.send_place_code(place_code)
        self.Eh.send_place_name(place_name)
        #self.Eh.send_place_division_code()
        self.Eh.send_place_address(place_address)
        self.Eh.send_place_person(place_person)
        self.Eh.send_place_person_tel(place_person_tel)
        #self.Eh.select_place_status()
        self.Eh.click_confirm_add_btn()
        sleep(3)

    # 数据驱动整合代码
    def add_function(self, place_code, place_name, place_address, place_person, place_person_tel, assertCode,
                     assertText):
        self.success_add(place_code, place_name, place_address, place_person, place_person_tel)
        if len(assertCode) != 0:
            if self.Eh.get_user_text(assertCode, assertText) is None:
                return False
            else:
                print("用例通过")
                return True
        else:
            if assertText == '添加成功':
                if self.Eh.get_add_success_text() == assertText:
                    print('添加成功，用例通过')
                    return True

    # 未完成，判断是否添加成功
    def success_or_fail(self):
        if self.Eh.get_login_btn_text() is None:
            return True
        else:
            return False


if __name__ == "__main__":
    lkc = LoginKeywordCases()
    lkc.run_keyword_excel_cases()
    driver = getattr(getattr(lkc, 'lk'), 'driver')
    driver.maximize_window()
    Eb = ExaminationPlaceBusiness(driver)

    Eb.success_add('1212', '西北税务学校', '电子一路', '小冯', '15002933333')
    #driver.refresh()
    sleep(3)
