# coding=utf-8

from selenium import webdriver
from basic.find_element import FindElement
from time import sleep


class LoginKeyword(object):
    # 打开浏览器
    def open_browser(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()

    # 获取driver
    def get_driver(self):
        return self.driver

    # 输入测试地址
    def get_url(self, url):
        self.driver.get(url)

    # 定位元素
    def get_element(self, key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key, 'LoginElemnet')
        return element

    # 输入元素
    def send_element_key(self, key, value):
        get_element = self.get_element(key)
        get_element.send_keys(str(value))

    # 点击元素
    def click_element(self, key):
        find_element = FindElement(self.driver)
        find_element.get_element(key, 'LoginElemnet').click()

    # 页面等待
    @staticmethod
    def wait_loading():
        sleep(1)

    # 关闭浏览器
    def close_browser(self):
        self.driver.close()

    # 获取title
    def get_title(self):
        return self.driver.title


if __name__ == "__main__":
    login_url = 'http://localhost:9090/exam-place/login'
    driver = webdriver.Chrome()
    driver.get(login_url)
    lk = LoginKeyword(driver)
    lk.send_element_key('login_password', '123')
    sleep(3)
    driver.close()
