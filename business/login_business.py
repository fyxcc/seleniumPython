#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from handle.login_handle import LoginHandle
from selenium import webdriver
from time import sleep


class LoginBusiness(object):
    def __init__(self, driver):
        self.lh = LoginHandle(driver)

    # 正常登录
    def common_login(self, name, password, file_name):
        self.lh.send_login_name(name)
        self.lh.send_login_password(password)
        if len(file_name) != 0:
            self.lh.send_login_captcha(file_name)
        self.lh.click_login_btn()

    # 数据驱动整合代码
    def login_function(self, username, password, file_name, assertCode, assertText):
        self.common_login(username, password, file_name)
        if len(assertCode) != 0:
            if self.lh.get_user_text(assertCode, assertText) is None:
                return False
            else:
                print("用例通过")
                return True

    # 判断是否注册成功
    def success_or_fail(self):
        if self.lh.get_login_btn_text() is None:
            return True
        else:
            return False


if __name__ == "__main__":
    login_url = 'http://localhost:9090/exam-place/login'
    driver = webdriver.Chrome()
    driver.get(login_url)
    rb = LoginBusiness(driver)
    print(rb.login_function('fyxcc', '121212', 'D:/pythonWork/autoTest/image/verify_login_error.png',
                            'verify_login_error', '1212'))
    sleep(3)
    driver.close()
