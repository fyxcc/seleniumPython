#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from basic.find_element import FindElement
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage(object):
    # 初始化元素查找类，执行该类的时候就会加载
    def __init__(self, driver):
        self.fe = FindElement(driver)

    # 用户昵称
    def get_login_name(self):
        return self.fe.get_element('login_name')

    # 密码
    def get_login_password(self):
        return self.fe.get_element('login_password')

    # 验证码输入框
    def get_login_captcha_code(self):
        return self.fe.get_element('login_captcha_code')

    # 验证码图片
    def get_login_getcode_num(self):
        return self.fe.get_element('login_getcode_num ')

    # 登录按钮
    def get_login_btn(self):
        return self.fe.get_element('login_btn')

    # 用户框文本提示语
    def get_login_name_placeholder(self):
        print(self.fe.get_element('login_name').get_attribute('placeholder'))
        return self.fe.get_element('login_name').get_attribute('placeholder')

    # 密码框文本提示语
    def get_login_password_placeholder(self):
        print(self.fe.get_element('login_password').get_attribute('placeholder'))
        return self.fe.get_element('login_password').get_attribute('placeholder')

    # 验证码框文本提示语
    def get_captcha_code_placeholder(self):
        print(self.fe.get_element('login_captcha_code').get_attribute('placeholder'))
        return self.fe.get_element('login_captcha_code').get_attribute('placeholder')

    # 自动登录按钮
    def get_login_auto_btn(self):
        return self.fe.get_element('login_auto')

    # 不合法登录用户名错误提示语
    def get_login_name_error(self):
        return self.fe.get_element('login_name_error')

    # 不合法登录密码错误提示语
    def get_login_password_error(self):
        return self.fe.get_element('login_password_error')

    # 不合法验证码错误提示语
    def get_captcha_code_error(self):
        return self.fe.get_element('login_captcha_error')

    # 登录名或者密码验证不通过提示语
    def get_verify_login_error(self):
        return self.fe.get_element('verify_login_error')


if __name__ == "__main__":
    register_url = 'http://localhost:9090/exam-place/login'
    driver = webdriver.Chrome()
    driver.get(register_url)
    lp = LoginPage(driver)
    lp.get_login_name_placeholder()
    lp.get_login_password_placeholder()
    lp.get_captcha_code_placeholder()
    driver.close()
