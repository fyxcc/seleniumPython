# coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from basic.find_element import FindElement
from time import sleep

from case.login_keyword_cases import LoginKeywordCases


class ExaminationPlaceKeyword(object):
    def __init__(self):
        lkc = LoginKeywordCases()
        lkc.run_keyword_excel_cases()
        driver = getattr(getattr(lkc, 'lk'), 'driver')
        driver.maximize_window()
        self.driver = driver

    # 定位元素
    def get_element(self, key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key, 'ExaminationPlacePage')
        return element

    # 输入元素
    def send_element_key(self, key, value):
        get_element = self.get_element(key)
        get_element.send_keys(str(value))

    # 点击元素
    def click_element(self, key):
        find_element = FindElement(self.driver)
        find_element.get_element(key, 'ExaminationPlacePage').click()

    # 页面等待
    @staticmethod
    def wait_loading():
        sleep(2)

    # 获取title
    def get_title(self):
        return self.driver.title

    # 获取添加结果信息
    def get_info(self):
        # self.wait_loading()
        # Eh=ExaminationPlaceHandle(self.driver)
        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath('/html/body/div[17]/div/div'))
        text = self.driver.find_element_by_xpath('/html/body/div[17]/div/div').text
        return text
        # Eh.get_add_success_text()

    # 关闭浏览器
    def close_browser(self):
        self.driver.close()


if __name__ == "__main__":
    Ek = ExaminationPlaceAddKeyword()
    sleep(3)
