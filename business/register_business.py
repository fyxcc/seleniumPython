#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from handle.login_handle import LoginHandle
from selenium import webdriver
from time import sleep


class RegisterBusiness(object):
    def __init__(self, driver):
        self.rh = LoginHandle(driver)

    # 正常登录
    def common_register(self, register_email, nickname, password, file_name):
        self.rh.send_register_email(register_email)
        self.rh.send_register_nickname(nickname)
        self.rh.send_register_password(password)
        self.rh.send_register_captcha(file_name)
        self.rh.click_register_btn()

    # 数据驱动整合代码
    def register_function(self, email, username, password, file_name, assertCode, assertText):
        self.common_register(email, username, password, file_name)
        if self.rh.get_user_text(assertCode, assertText) is None:
            return False
        else:
            print("注册邮箱输入错误")
            return True

    # 判断是否注册成功
    def success_or_fail(self):
        if self.rh.get_register_btn_text() is None:
            return True
        else:
            return False

    # 邮箱错误
    def register_email_error(self, register_email, nickname, password, file_name):
        self.common_register(register_email, nickname, password, file_name)
        if self.rh.get_user_text('register_email_error', "请输入有效的电子邮件地址") is None:
            return False
        else:
            print("注册邮箱输入错误")
            return True

    # 用户昵称错误
    def register_nickname_error(self, register_email, nickname, password, file_name):
        self.common_register(register_email, nickname, password, file_name)
        if self.rh.get_user_text('register_nickname_error', "字符长度必须大于等于4，一个中文字算2个字符") is None:
            return False
        else:
            print("用户昵称错误")
            return True

    # 用户密码错误
    def register_password_error(self, register_email, nickname, password, file_name):
        self.common_register(register_email, nickname, password, file_name)
        if self.rh.get_user_text('register_password_error', "最少需要输入 5 个字符") is None:
            return False
        else:
            print("用户密码错误")
            return True

    # 验证码错误
    def captcha_code_error(self, register_email, nickname, password, file_name):
        self.common_register(register_email, nickname, password, file_name)
        if self.rh.get_user_text('captcha_code_error', "验证码错误") is None:
            return False
        else:
            print("验证码错误")
            return True


if __name__ == "__main__":
    register_url = 'http://www.5itest.cn/register'
    driver = webdriver.Chrome()
    driver.get(register_url)
    rb = RegisterBusiness(driver)
    # rb.captcha_code_error('1243589@163.com', 'pass123', 'test@123', 'sds')

    sleep(3)
    driver.close()
