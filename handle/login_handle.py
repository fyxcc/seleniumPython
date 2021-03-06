# coding=utf-8
import os
from threading import Thread

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page.login_page import LoginPage
from selenium import webdriver
from time import sleep
from util.get_code import GetCode
from selenium.webdriver.common.action_chains import ActionChains
import time


class LoginHandle(object):
    def __init__(self, driver):
        self.driver = driver
        self.lp = LoginPage(self.driver)

    # 输入用户名
    def send_login_name(self, name):
        self.lp.get_login_name().send_keys(name)

    # 输入登录密码
    def send_login_password(self, password):
        self.lp.get_login_password().send_keys(password)

    # 输入验证码
    def send_login_captcha(self, file_name):
        get_code_text = GetCode(self.driver)
        #captcha = get_code_text.discern_captcha_image(file_name)
        self.lp.get_login_captcha_code().send_keys('1212')

    # 获取错误信息
    def get_user_text(self, error_info,assertText):
        try:

            if error_info == 'login_name_error':
                text = self.lp.get_login_name_error().text
            elif error_info == 'login_password_error':
                text = self.lp.get_login_password_error().text
            elif error_info == 'verify_login_error':
                WebDriverWait(self.driver, 10).until(
                    lambda x: x.find_element_by_xpath('/html/body/div[3]/div/div'))
                text = self.driver.find_element_by_xpath('/html/body/div[3]/div/div').text
                #text = self.lp.get_verify_login_error().text
            else:
                text = self.lp.get_captcha_code_error().text

            return text
        except BaseException as e:
            print(repr(e))
            return None

    # 点击自动登录按钮
    def click_login_auto_btn(self):
        self.lp.get_login_auto_btn().click()

    # 点击登录按钮
    def click_login_btn(self):
        self.lp.get_login_btn().click()

    # 获取登录按钮文字
    def get_login_btn_text(self):
        return self.lp.get_login_btn().text


if __name__ == "__main__":
    register_url = 'http://localhost:9090/exam-place/login'
    file_name = os.path.join(os.path.pardir + "/Image/" + "test_captcha0330.png")
    driver = webdriver.Chrome()
    driver.get(register_url)
    lh = LoginHandle(driver)
    lh.send_login_name('fyx')
    lh.send_login_password('121212')
    lh.send_login_captcha(file_name)
    # lh.click_login_auto_btn()
    lh.click_login_btn()
    print(lh.get_user_text('verify_login_error','1212'))
    time.sleep(2)
    driver.close()
